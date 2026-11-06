#!/usr/bin/env python3
"""Build the Galician delivery (how-to step 5) from ReSpec's HTML export.

Input : an unmodified HTML export from ReSpec (UI export or respec.toHTML()).
        Pass its path as the first argument. DOM captures are not recommended.
Output: the same file post-processed: ReSpec chrome stripped, .head +
        generated sotd + section annotations + dfn panels + UI strings in
        Galician, translation disclaimer inserted. Idempotence is NOT
        guaranteed: always run over a fresh capture.

Usage: python3 tools/make_export.py /path/to/raw-export.html
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from export_helpers import finish_export, copy_companions

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "work" / "export" / "index.html"

ABBR = '<abbr title="World Wide Web Consortium">W3C</abbr>'


def rep(t: str, old: str, new: str, expect: int = 1) -> str:
    c = t.count(old)
    assert c >= expect, f"ANCHOR ({c}) missing: {old[:70]!r}"
    return t.replace(old, new)


def load_json(name: str):
    return json.loads((ROOT / "tools" / name).read_text(encoding="utf-8"))


HEADING_IDS = load_json("original-heading-ids.json")
DOCLINK_SLUGS = load_json("original-doclink-slugs.json")


def restore_heading_ids(t: str) -> str:
    """Put the original English ReSpec-generated heading IDs back (x1-1-...)."""
    ids = sorted(HEADING_IDS, key=len, reverse=True)
    alt = "|".join(re.escape(i) for i in ids)
    pat = re.compile(
        r'(<section\b[^>]*\bid="(' + alt + r')"[^>]*>.*?<h[234]\b[^>]*\bid=")([^"]+)(")',
        re.S,
    )
    return pat.sub(lambda m: f"{m.group(1)}{HEADING_IDS[m.group(2)]}{m.group(4)}", t)


def restore_doclink_urls(t: str) -> str:
    """Restore the original English Understanding/quickref URLs in doclinks."""
    ids = sorted(DOCLINK_SLUGS, key=len, reverse=True)
    alt = "|".join(re.escape(i) for i in ids)
    pat_u = re.compile(
        r'(<section\b[^>]*\bid="(' + alt + r')"[^>]*>.*?<div class="doclinks">.*?Understanding/)([^"?#]+)(\.html)',
        re.S,
    )
    t = pat_u.sub(lambda m: f"{m.group(1)}{DOCLINK_SLUGS[m.group(2)]}{m.group(4)}", t)
    pat_q = re.compile(
        r'(<section\b[^>]*\bid="(' + alt + r')"[^>]*>.*?<div class="doclinks">.*?quickref/#)([^"?#]+)(")',
        re.S,
    )
    t = pat_q.sub(lambda m: f"{m.group(1)}{DOCLINK_SLUGS[m.group(2)]}{m.group(4)}", t)
    return t


def remove_balanced(t: str, marker: str) -> str:
    i = t.find(marker)
    if i < 0:
        return t
    depth = 0
    for m in re.finditer(r"<div\b|</div>", t[i:], re.S):
        depth += -1 if m.group(0) == "</div>" else 1
        if depth == 0:
            return t[:i] + t[i + m.end():]
    return t


def replace_paragraph_containing(t: str, anchor: str, new_p: str) -> str:
    """Swap the whole <p>...</p> that contains `anchor` for `new_p`."""
    i = t.find(anchor)
    assert i > 0, f"anchor non atopada: {anchor[:60]!r}"
    s = t.rfind("<p>", 0, i)
    e = t.find("</p>", i) + len("</p>")
    assert 0 < s < e
    return t[:s] + new_p + t[e:]


def main() -> int:
    raw = Path(sys.argv[1]) if len(sys.argv) > 1 else TARGET
    t = raw.read_text(encoding="utf-8")
    assert 'lang="gl"' in t[:200], "a captura non é a vista galega"

    # -- 1) chrome de ReSpec fora -------------------------------------------
    t = remove_balanced(t, '<div id="respec-ui"')
    for pat in (r'<script[^>]*respec-w3c"[^>]*>\s*</script>', r'<script[^>]*wcag\.js"[^>]*>\s*</script>',
                r'<script[^>]*respec-config\.js"[^>]*>\s*</script>', r'<script[^>]*biblio\.js"[^>]*>\s*</script>',
                r'<link[^>]*sources\.css[^>]*>'):
        t = re.sub(pat, "", t)
    t = rep(t, '<script src="https://www.w3.org/scripts/TR/2021/fixup.js"></script>',
               '<script src="fixup.js"></script>')

    # -- 2) cabeceira .head ---------------------------------------------------
    t = rep(t, "W3C Recommendation", "Recomendación do W3C")
    t, count = re.subn(r'(<time\b[^>]*datetime="2024-12-12"[^>]*>)[^<]*',
                       r'\g<1>do 12 de decembro de 2024', t, count=1)
    assert count == 1, "publication date missing"
    t = t.replace('"generatedSubtitle": "W3C Recommendation 12 de diciembre de 2024"',
                  '"generatedSubtitle": "Recomendación do W3C do 12 de decembro de 2024"')
    t = rep(t, "More details about this document", "Máis detalles deste documento")
    t = rep(t, "This version:", "Esta versión:")
    t = rep(t, "Latest published version:", "Última versión publicada:")
    t = rep(t, "Latest editor's draft:", "Último borrador do editor:")
    t = rep(t, "Previous Recommendation:", "Recomendación anterior:")
    t = rep(t, "History:", "Historia:")
    t = rep(t, "Implementation report:", "Informe de implementación:")
    t = rep(t, "Commit history", "Historial de commits")
    t = rep(t, "Errata:", "Erratas:")
    t = rep(t, "Errata exists", "Existen erratas")
    t = rep(t, "new issue", "nova incidencia")
    t = rep(t, "open issues", "incidencias abertas")
    t = rep(t, "Feedback:", "Comentarios:")
    t = rep(t, "See also", "Véxase tamén")
    t = rep(t, "<strong>translations</strong>", "<strong>traducións</strong>")

    # -- 3) sotd xerado (galego, marcado conservado) --------------------------
    t = re.sub(
        r"<p><em>This section describes the status.*?</em>\s*</p>",
        "<p><em>Esta sección describe o estado deste documento no momento da súa publicación. "
        f"Pódese atopar unha lista das publicacións actuais do {ABBR} e a última revisión deste "
        f"informe técnico no <a href=\"https://www.w3.org/TR/\">índice de estándares e borradores do {ABBR}</a>.</em></p>",
        t, count=1, flags=re.S)
    t = re.sub(
        r"<p>\s*This document was published by the.*?</p>",
        f"<p>Este documento foi publicado polo <a href=\"https://www.w3.org/groups/wg/ag\">Accessibility Guidelines Working Group</a> como "
        "unha Recomendación usando a "
        "<a href=\"https://www.w3.org/policies/process/20231103/#recs-and-notes\">vía de Recomendacións</a>. </p>",
        t, count=1, flags=re.S)
    t = replace_paragraph_containing(
        t, "recommends the wide deployment",
        f"<p>O {ABBR} recomenda o despregamento amplo desta especificación como estándar para a Web.</p>")
    t = replace_paragraph_containing(
        t, "Recommendation is a specification that, after extensive",
        f"<p>Unha Recomendación do {ABBR} é unha especificación que, tras un amplo proceso de consenso, "
        f"está avalada polo {ABBR} e os seus Membros, e supón compromisos dos membros do Grupo de Traballo de "
        "<a href=\"https://www.w3.org/policies/patent-policy/#sec-Requirements\">licenzas sen regalías</a> "
        "para as implementacións.</p>")
    # Preserve the published normative section; do not inject additional wording.
    # bloque RFC2119 xerado (só cando wcag.js o inxecta; se non, a nosa frase fonte queda)
    if "The key words" in t:
        t = rep(t, "The key words", "As palabras clave")
        t = rep(t, "in this document\n        are", "neste documento\n        han")
        t = rep(t, " to be interpreted as described in", " interpretarse como se describe en")
        t = rep(t, "when, and only when, they appear", "cando, e só cando, aparecen")
        t = rep(t, "capitals, as shown here.", "maiúsculas, tal e como se amosan aquí.")
        t = rep(t, " in all\n        maiúsculas", " en maiúsculas")
    t = re.sub(
        r"<p>\s*This document was produced by a group.*?</p>",
        f"<p>Este documento foi producido por un grupo que opera baixo a "
        f"<a href=\"https://www.w3.org/policies/patent-policy/\">Política de Patentes do {ABBR}</a>. "
        f"O {ABBR} mantén unha "
        "<a rel=\"disclosure\" href=\"https://www.w3.org/groups/wg/ag/ipr\">lista pública de calquera divulgación de patentes</a> "
        "feita en relación coas entregables do grupo; esa páxina tamén inclúe instrucións para divulgar unha patente. "
        "Unha persoa que teña coñecemento real dunha patente que crea que contén "
        "<a href=\"https://www.w3.org/policies/patent-policy/#def-essential\">Reclamacións Esenciais</a> "
        "debe divulgar a información de acordo coa "
        f"<a href=\"https://www.w3.org/policies/patent-policy/#sec-Disclosure\">sección 6 da Política de Patentes do {ABBR}</a>.</p>",
        t, count=1, flags=re.S)
    t = re.sub(
        r"<p>\s*This document is governed by the.*?</p>",
        "<p>Este documento réxese polo "
        f"<a id=\"w3c_process_revision\" href=\"https://www.w3.org/policies/process/20231103/\">Documento de Proceso do {ABBR} do 3 de novembro de 2023</a>.</p>",
        t, count=1, flags=re.S)

    # -- 4) encabezados + anotacións + apéndices ------------------------------
    t = rep(t, ">Abstract<", ">Resumo<", 2)
    t = rep(t, ">Status of This Document<", ">Estado deste documento<", 2)
    t = t.replace("Jump to Table of Contents", "Ir ao índice de contidos")
    t = rep(t, ">Table of Contents<", ">Índice de contidos<", 1)
    t = rep(t, ">References<", ">Referencias<", 2)
    # as subseccións de Referencias só aparecen cando wcag.js injecta as citas
    # normativas canónicas (sección anónima → non ocorre); tradúcense se existen
    if "Normative references" in t:
        t = rep(t, "Normative references", "Referencias normativas", 1)
    if "Informative references" in t:
        t = rep(t, "Informative references", "Referencias informativas", 1)
    t = rep(t, "This section is non-normative.", "Esta sección non é normativa.", 4)
    for L in "ABC":
        t = t.replace(f"Appendix {L}", f"Apéndice {L}")

    # -- 5) strings UI (how-to paso 5) ----------------------------------------
    # xerados por wcag.js/ReSpec (non existen no fonte)
    t = rep(t, '<bdi class="secno">Success Criterion ', '<bdi class="secno">Criterio de Éxito ', 40)
    t = rep(t, "<span>Note</span>", "<span>Nota</span>", 30)
    t = t.replace("Understanding Success Criterion ", "Comprender o Criterio de Éxito ")
    t = t.replace("How to Meet Success Criterion ", "Como cumprir o Criterio de Éxito ")
    t = rep(t, "Permalink for this Section", "Ligazón permanente para esta sección", 10)
    assert t.count(">Understanding ") >= 90 and t.count("How to Meet ") >= 80
    t = re.sub(r'<div class="doclinks">.*?</div>',
               lambda match: match[0].replace(">Understanding ", ">Comprender ")
                                     .replace("How to Meet ", "Como cumprir "),
               t, flags=re.S)
    assert t.count("Permalink for ") + t.count(">Permalink<") > 200
    t = t.replace(">Permalink</", ">Ligazón permanente</").replace("Permalink for ", "Ligazón permanente para ")
    t = rep(t, "Ligazón permanente para Section ", "Ligazón permanente para a sección ", 100)
    t = rep(t, "Referenced in:", "Mencionado en:")
    t = t.replace("Not referenced in this document.", "Non mencionado neste documento.")
    t = t.replace("Links in this document to definition: ", "Ligazóns neste documento á definición: ")
    t = t.replace("Guideline ", "Pauta ")
    t = t.replace("(Level ", "(Nivel ")
    t = t.replace("Collapse Sidebar", "Contraer a barra lateral")
    t = t.replace("Pop Out Sidebar", "Despregar a barra lateral")
    t = t.replace('aria-label="Select a color scheme"', 'aria-label="Seleccionar un esquema de cores"')
    t = t.replace(">light<", ">claro<")
    t = t.replace(">dark<", ">escuro<")
    t = t.replace('title="theme toggle icon"', 'title="icona para alternar o tema"')

    # how-to: a sección de Conformidade debe ter id="conformance"; o render
    # auto-xera "conformidade" (título GL) — renomézase id e hrefs internos
    t = t.replace('id="conformidade"', 'id="conformance"')
    t = t.replace('href="#conformidade"', 'href="#conformance"')

    # -- 5b) ids de cabeceira e doclinks en inglés ----------------------------
    t = restore_heading_ids(t)
    t = restore_doclink_urls(t)


    # -- 6) disclaimer de tradución -------------------------------------------
    DISCLAIMER = f'''<section id="traducion-gl" class="introductory">
      <h2 lang="en">Web Content Accessibility Guidelines (WCAG) 2.2</h2>
      <p><strong lang="en">Lead translating organization:</strong> <strong>a11y.es</strong> — Jesús Quintana,
      <a href="https://a11y.es/">https://a11y.es/</a>, <a href="mailto:hola@a11y.es">hola@a11y.es</a> (proposta).</p>
      <h2>Tradución ao galego</h2>
      <p>Esta é unha tradución ao galego do documento
      <a href="https://www.w3.org/TR/2024/REC-WCAG22-20241212/" lang="en">Web Content Accessibility Guidelines (WCAG) 2.2</a>,
      Recomendación do W3C do 12 de decembro de 2024. A presente tradución pode conter erros ou
      imprecisións. A única versión oficial e normativa do documento é a orixinal en inglés,
      dispoñible no sitio web do {ABBR}:
      <a href="https://www.w3.org/TR/2024/REC-WCAG22-20241212/" lang="en">https://www.w3.org/TR/2024/REC-WCAG22-20241212/</a>.</p>
      <p>Tradución liderada por Jesús Quintana (<a href="https://a11y.es/">a11y.es</a>) como
      <i lang="en">Lead Translation Organization</i> (proposta), co obxectivo de presentala como
      <i lang="en">Candidate Authorized Translation</i> segundo a
      <a href="https://www.w3.org/2005/02/TranslationPolicy" lang="en">Policy for Authorized W3C Translations</a>.</p>
    </section>
    '''
    t = re.sub(r"(<body\b[^>]*>)", r"\1\n" + DISCLAIMER, t, count=1)
    # -- 7) control final -------------------------------------------------------
    leftovers = {s: t.count(s) for s in (
        "W3C Recommendation<!--", "12 de diciembre", "This version:", "More details",
        "esborrany", ">Abstract<", ">Status of This Document<", "How to Meet ", "Referenced in:",
        "Not referenced in this document.", "This section is non-normative.", "Normative references",
        "Permalink for this Section", "This section describes the status", "This document was published",
        "recommends the wide deployment", "As well as sections marked", "The key words",
        "para Section ", ">Note</span>", "Success Criterion ", "Guideline ",
        "(Level ", "Collapse Sidebar", "Pop Out Sidebar", "Select a color scheme", "theme toggle icon")}
    bad = {k: v for k, v in leftovers.items() if v}
    if bad:
        print("RESTOS EN:", bad, file=sys.stderr)
        return 1
    t = finish_export(t)
    TARGET.write_text(t, encoding="utf-8")
    copy_companions(TARGET.parent)
    print(f"export OK: {len(t)} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
