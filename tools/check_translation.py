#!/usr/bin/env python3
"""Check the complete delivery against WCAG22-20241212 and its published IDs."""
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / 'tools/original-published-data.json').read_text())
DELIVERY = ROOT / 'work/export'
document = BeautifulSoup((DELIVERY / 'index.html').read_text(), 'html.parser')

ids = Counter(node['id'] for node in document.select('[id]'))
assert all(count == 1 for count in ids.values()), 'Duplicate IDs'
assert set(ids) == set(DATA['ids']) | {'traducion-gl'}, 'Published IDs differ'
assert not document.select('.respec-offending-element, .remove, [data-include]'), 'ReSpec errors or unfinished export'
assert not document.select('a:not([href])'), 'Unresolved link'
for node in document.select('a[href^="#"]'):
    assert unquote(node['href'][1:]) in ids, node['href']
for node in document.select('[aria-labelledby], [aria-describedby]'):
    for attribute in ('aria-labelledby', 'aria-describedby'):
        for target in node.get(attribute, '').split():
            assert target in ids, (attribute, target)
assert Counter(node['href'] for node in document.select('a.internalDFN')) == Counter(
    item['href'] for item in DATA['dfn_references']), 'Definition reference targets differ'
for item in DATA['dfn_references']:
    assert document.find(id=item['id'])['href'] == item['href'], item

wcag = json.loads((ROOT / 'source/guidelines/wcag.json').read_text())
criteria = [sc for principle in wcag['principles'] for guideline in principle['guidelines']
            for sc in guideline['successcriteria']]
assert len(criteria) == 87
for criterion in criteria:
    section = document.find(id=criterion['id'].split(':')[1])
    assert section and section.select_one('h4 .secno'), criterion['id']
    assert section.select_one('h4 .secno').get_text(' ', strip=True) == 'Criterio de Éxito ' + criterion['num']
assert len(document.select('dfn')) == 101

for filename in ('index.html', 'relative-luminance.html'):
    text = (DELIVERY / filename).read_text(encoding='utf-8')
    page = BeautifulSoup(text, 'html.parser')
    assert page.html['lang'] == page.html['xml:lang'] == 'gl', filename
    for node in page.select('[src], a[href], link[href]'):
        url = node.get('src', node.get('href', ''))
        parts = urlsplit(url)
        if not parts.scheme and not parts.netloc and parts.path:
            target = DELIVERY / unquote(parts.path)
            if target.is_dir():
                target = target / 'index.html'
            assert target.is_file(), (filename, url)
            if parts.fragment:
                linked_page = BeautifulSoup(target.read_text(), 'html.parser')
                assert linked_page.find(id=unquote(parts.fragment)), (filename, url)
assert (DELIVERY / 'guidelines.css').read_bytes() == (ROOT / 'source/guidelines/guidelines.css').read_bytes()

for node in document.select('.note-title, [aria-label], .head'):
    text = node.get('aria-label', '') + node.get_text(' ', strip=True)
    assert not re.search(r'\bNote(?:\s+\d+)?\b|Permalink for|Activate to close this dialog|Former editors:|\bEditors:|\bUntil\b', text), text[:160]
assert '20250818' not in str(document.find(id='sotd'))
assert 'pointerevents4' not in str(document.find(id='references'))

def numbers(path):
    soup = BeautifulSoup(path.read_text(), 'html.parser')
    for node in soup(['script', 'style']):
        node.decompose()
    return Counter(value.lstrip('0') or '0' for value in
                   re.findall(r'(?<![\w])\d*\.?\d+(?::\d+)?', soup.get_text(' ', strip=True)))

for translated in (ROOT / 'work/guidelines').rglob('*.html'):
    original = ROOT / 'source' / translated.relative_to(ROOT / 'work')
    assert numbers(original) == numbers(translated), ('Numerical difference', translated)
    a = BeautifulSoup(original.read_text(), 'html.parser')
    b = BeautifulSoup(translated.read_text(), 'html.parser')
    assert Counter(n['id'] for n in a.select('[id]')) == Counter(n['id'] for n in b.select('[id]')), translated

print('OK: 87 criteria, 101 definitions, 401 glossary references; original IDs, numbers, languages and delivery files verified.')
