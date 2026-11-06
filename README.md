# Pautas de Accesibilidade para o Contido Web (WCAG) 2.2 — tradución ao galego

> **English summary.** This repository holds an *unofficial draft* Galician
> translation of [WCAG 2.2](https://www.w3.org/TR/2024/REC-WCAG22-20241212/)
> (W3C Recommendation, 12 December 2024) — the first WCAG translation into
> Galician. All 199 pieces are translated; external human review is pending.
> Our goal is to propose it as a W3C Candidate Authorized Translation.
> Contributions welcome — see `CONTRIBUTING.md`. Read the current draft at
> `work/export/index.html` (open it locally or serve the folder over HTTP).

## Que é

Borrador da **primeira traducción das WCAG ao galego** — non existe ningunha,
autorizada nin non oficial, en ningunha versión. Tradúcese o documento
completo: os 86 criterios de éxito vixentes, as definicións do glosario
normativo, a introdución, a sección de conformidade e os recoñecementos (199
pezas, listadas en `docs/checklist.md`).

É unha tradución **non oficial**: non está revisada nin avalada polo W3C. A
única versión oficial e normativa é a
[orixinal inglesa](https://www.w3.org/TR/WCAG22/).

## Quen a impulsa

**[Jesús Quintana Fernández](https://a11y.es)**, fundador de
[a11y.es](https://a11y.es/), como Lead Translation Organization proposto.
Anuncio público de intención enviado á lista
[`w3c-translators`](https://lists.w3.org/Archives/Public/w3c-translators/2026OctDec/0002.html)
do W3C o 20 de outubro de 2026.

## Fonte

A **Recomendación inglesa do 12 de decembro de 2024**: repositorio
[`w3c/wcag`](https://github.com/w3c/wcag), tag `WCAG22-20241212`. A copia de
traballo está en `source/` (excluída de Git). Para reproducila:

```sh
git clone --depth 1 --branch WCAG22-20241212 https://github.com/w3c/wcag source
```

## Estado

| Peza | Estado |
|---|---|
| 87 criterios de éxito + 102 definicións + índice + luminancia + input purposes + fixup.js + recoñecementos | ✅ traducidos (199/199) |
| Corrección humana (redonda a redonda) | 🔄 feita sobre o borrador; continua |
| Revisión lingüística e técnica externa | ⏳ **pendente** — buscamos revisores |
| Validadores W3C (markup, ligazóns, CSS, i18n) | ⏳ na entrega |

O estado por ficheiro está en `docs/checklist.md`; as decisións terminolóxicas
fechadas, en `docs/glosario-gl.md` (canónico — o control de coherencia grepa
contra el).

## Obxectivo

Preparar a **Candidata a Tradución Autorizada** (*Candidate Authorized
Translation*) segundo a
[Policy for Authorized W3C Translations](https://www.w3.org/2005/02/TranslationPolicy):
a política permite propoñer unha tradución voluntaria existente como
candidata, que pasa por un período de revisión pública de polo menos 30 días
antes de ser endosada polo W3C e publicada en w3.org.

## Colaboración — buscamos revisores

- **Revisores técnicos** (accesibilidade): verificar que cada criterio di o
  que di o orixinal.
- **Revisores lingüísticos** (galego): terminoloxía, estilo, coherencia coa
  normativa RAG/Termigal.
- **Organizacións representativas** (universidades, entidades do ámbito da
  lingua e da accesibilidade): o grupo de interese que a política W3C esixe
  para unha tradución autorizada.

Ver `CONTRIBUTING.md`.

## Como participar

Abre unha **incidencia** co formato: apartado afectado, texto actual,
proposta e xustificación (con cita do orixinal inglés se procede). As
correccións de texto non necesitan pull request — valen as incidencias; os
mantedores aplícannas e rexístranas no glosario canónico.

## Como ler e xerar o documento

**Ler o borrador actual**: abre `work/export/index.html` nun navegador (con
`work/export/fixup.js` e `work/export/guidelines.css` ao lado), ou serve a
carpeta por HTTP:

```sh
cd work/export
python3 -m http.server 8080
# http://localhost:8080/index.html
```

**Xerar o export** (reproducible):

```sh
# 1) inline determinista dos data-include (o servidor solto falla fetches ao azar)
python3 tools/inline_preview.py work/guidelines/index.html work/guidelines work/guidelines/index-inlined.html

# 2) servir e capturar o render (ReSpec esixe HTTP; o HTML final vén do render)
cd work/guidelines && python3 -m http.server 8080
# abrir http://localhost:8080/index-inlined.html e gardar o DOM renderizado
# (existe un receptor de exemplo en tools/export_helpers.py)

# 3) post-proceso (cabaceira, sotd, UI, disclaimer; autocomproba restos de inglés)
python3 tools/make_export.py

# 4) comprobación da entrega contra a publicación congelada
python3 tools/check_translation.py
```

A entrega final ao W3C (paso 6.3 da política) son tres ficheiros:
`index.html`, `relative-luminance.html` e `fixup.js` — ademais do
`guidelines.css` para a lectura local.

## Estrutura do repositorio

```
├── README.md                  Este documento
├── LICENSE.md                 Licencia W3C do documento + condicións da tradución
├── CONTRIBUTING.md            Como propoñer correccións
│
├── work/                      Fontes e recursos da tradución
│   ├── guidelines/            Fragmentos editables (sc/, terms/, index…)
│   ├── acknowledgements/      Recoñecementos
│   ├── css/ script/ biblio.js Infraestrutura ReSpec
│   ├── fixup.js               3 cadeas de UI do sitio orixinal
│   └── export/                Borrador HTML para ler e revisar
│       ├── index.html · relative-luminance.html · fixup.js · guidelines.css
│
├── docs/
│   ├── glosario-gl.md         Terminología inglés–galego (canónica)
│   ├── checklist.md           Estado de tradución e revisión
│   └── baseline-qa/           Auditoría base do orixinal (referencia de calidade)
│
└── tools/                     Xeración e comprobacións
    ├── inline_preview.py      Inline determinista dos data-include
    ├── make_export.py         Post-proceso do export (autocomprobación)
    ├── check_translation.py   Entrega vs publicación congelada
    └── gen_checklist.py       Regenera docs/checklist.md
```

`docs/sbs/` (fichas EN|ES|GL) e `docs/es-sidar/` (caché da referencia
española 2.0 de Fundación Sidar) son **material de traballo local**: non se
reparten neste repositorio porque conteñen texto dunha tradución allea con
copyright propio (dispoñibles baixo solicitude).

`source/` (copia inglesa do tag) está excluída de Git; descargable coa orde
de arriba.

## Licencia

Documento orixinal © W3C baixo o
[W3C Document License](https://www.w3.org/copyright/document-license-2023/).
Tradución © 2026 Jesús Quintana Fernández baixo a mesma licencia. Ver
[LICENSE.md](LICENSE.md).
