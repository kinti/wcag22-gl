"""Normalize a ReSpec export against the frozen 2024 W3C publication."""
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json
import re
import shutil

from bs4 import BeautifulSoup, Comment

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / 'tools/original-published-data.json').read_text())
HEADINGS = json.loads((ROOT / 'tools/original-heading-ids.json').read_text())


def finish_export(text: str) -> str:
    soup = BeautifulSoup(text, 'html.parser')
    # Runtime controls lose their event listeners in a DOM capture. Let fixup.js
    # recreate them, using the same stylesheet set as the published original.
    for node in soup.select('base, #toc-nav, #respec-ui, #respec-ui-styles, #respec-highlight-vars'):
        node.decompose()
    for node in soup.select('link[rel="stylesheet"]'):
        if node.get('href') in (
            'https://www.w3.org/StyleSheets/TR/2021/base.css',
            'https://www.w3.org/StyleSheets/TR/2021/dark.css',
        ):
            node.decompose()
    for comment in soup.find_all(string=lambda value: isinstance(value, Comment)):
        if re.match(r'-?\d+\.\d+%', str(comment)):
            comment.extract()

    replacements = {
        'Editors:': 'Editores:', 'Former editors:': 'Editores anteriores:',
        'Until': 'Ata', 'julio': 'xullo', 'marzo': 'marzo',
        'pull requests': 'solicitudes de incorporación de cambios',
        'liability': 'responsabilidade', 'trademark': 'marcas rexistradas',
        'document use': 'uso do documento', 'rules apply.': 'son aplicables.',
    }
    for node in soup.select('.head')[0].find_all(string=True):
        if not isinstance(node, Comment):
            value = str(node)
            for old, new in replacements.items():
                value = value.replace(old, new)
            if value.strip() == 'and':
                value = value.replace('and', 'e')
            node.replace_with(value)
    months = ('xaneiro', 'febreiro', 'marzo', 'abril', 'maio', 'xuño',
              'xullo', 'agosto', 'setembro', 'outubro', 'novembro', 'decembro')
    for node in soup.select('.head time[datetime]'):
        year, month, day = map(int, node['datetime'].split('-'))
        prefix = 'do ' if 'dt-published' in node.get('class', []) else ''
        node.clear()
        node.string = f'{prefix}{day} de {months[month-1]} de {year}'

    # ReSpec's live bibliography must not silently select newer specifications.
    references = BeautifulSoup(DATA['references_html'], 'html.parser').section
    for node in references.find_all(string=True):
        if not isinstance(node, Comment):
            value = str(node).replace('Informative references', 'Referencias informativas')
            value = value.replace('Normative references', 'Referencias normativas')
            if value.strip() == 'References':
                value = value.replace('References', 'Referencias')
            node.replace_with(value)
    for node in references.select('dd'):
        node['lang'] = 'en'
    soup.find(id='references').replace_with(references)

    renamed = {}
    for section in soup.select('section[id]'):
        heading = section.find(re.compile(r'^h[1-6]$'), recursive=False)
        wrapper = section.find('div', class_='header-wrapper', recursive=False)
        if heading is None and wrapper:
            heading = wrapper.find(re.compile(r'^h[1-6]$'))
        if heading and section['id'] in HEADINGS:
            old = heading.get('id')
            heading['id'] = HEADINGS[section['id']]
            if old and old != heading['id']:
                renamed[old] = heading['id']
    for link in soup.select('a[href^="#"]'):
        if link['href'][1:] in renamed:
            link['href'] = '#' + renamed[link['href'][1:]]

    expected = defaultdict(list)
    for reference in DATA['dfn_references']:
        expected[reference['href']].append(reference['id'])
    actual = defaultdict(list)
    for link in soup.select('a[href^="#dfn-"]:not(.self-link)'):
        actual[link['href']].append(link)
    wanted = Counter({key: len(value) for key, value in expected.items()})
    found = Counter({key: len(value) for key, value in actual.items()})
    if wanted != found:
        raise ValueError(f'Definition references differ: missing={wanted-found}, extra={found-wanted}')
    renamed_refs = {}
    for target, links in actual.items():
        definition = soup.find(id=target[1:])
        description = definition.find_parent('dt').find_next_sibling('dd').find('p')
        for link, original_id in zip(links, expected[target]):
            if link.get('id') and link['id'] != original_id:
                renamed_refs[link['id']] = original_id
            link['id'] = original_id
            link['class'] = ['internalDFN']
            link['data-link-type'] = 'dfn'
            if description:
                link['title'] = description.get_text(' ', strip=True)
    for link in soup.select('a[href^="#ref-for-"]'):
        if link['href'][1:] in renamed_refs:
            link['href'] = '#' + renamed_refs[link['href'][1:]]

    # Refresh panel reference lists after restoring English reference IDs.
    for definition in soup.select('dfn[id]'):
        panel = soup.find(id='dfn-panel-for-' + definition['id'])
        if panel is None:
            continue
        for node in list(panel.find_all(['ul', 'p'], recursive=False)):
            node.decompose()
        links = actual.get('#' + definition['id'], [])
        paragraph = soup.new_tag('p')
        paragraph.string = 'Mencionado en:' if links else 'Non mencionado neste documento.'
        panel.append(paragraph)
        if links:
            listing = soup.new_tag('ul')
            for link in links:
                section = link.find_parent('section')
                heading = section.find(re.compile(r'^h[1-6]$')) if section else None
                item = soup.new_tag('li')
                anchor = soup.new_tag('a', href='#' + link['id'])
                anchor.string = heading.get_text(' ', strip=True) if heading else 'Referencia'
                item.append(anchor); listing.append(item)
            panel.append(listing)

    for node in soup.find_all(string=True):
        if isinstance(node, Comment) or node.parent.name in ('script', 'style'):
            continue
        value = str(node)
        value = re.sub(r'\bNote(?=\s+\d+\b)', 'Nota', value)
        if value != str(node):
            node.replace_with(value)
    for node in soup.select('[aria-label], [title]'):
        for attr in ('aria-label', 'title'):
            if node.has_attr(attr):
                node[attr] = node[attr].replace('Permalink for Appendix ', 'Ligazón permanente para o apéndice ')
                node[attr] = node[attr].replace('definition:', 'a definición:')
                node[attr] = node[attr].replace('Activate to close this dialog.', 'Activar para pechar este diálogo.')
                node[attr] = node[attr].replace('Separator for header', 'Separador da cabeceira')
                node[attr] = node[attr].replace('W3C Document License', 'Licenza de documentos do W3C')

    # Proper names retained in English need a language tag when part of prose.
    for node in soup.find_all(string=re.compile('Accessibility Guidelines Working Group')):
        if node.parent.name not in ('script', 'style') and not node.find_parent(attrs={'lang': 'en'}):
            value = str(node)
            before, name, after = value.partition('Accessibility Guidelines Working Group')
            span = soup.new_tag('span', lang='en'); span.string = name
            node.replace_with(before, span, after)
    return re.sub(r'[ \t]+\n', '\n', str(soup))


def copy_companions(destination: Path) -> None:
    for filename in ('relative-luminance.html', 'guidelines.css'):
        shutil.copyfile(ROOT / 'work/guidelines' / filename, destination / filename)
    shutil.copyfile(ROOT / 'work/fixup.js', destination / 'fixup.js')
