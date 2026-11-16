# Preguntas abertas para a revisión externa: WCAG 2.2 galego

> Última actualización: 9-nov-2026, tras a rolda de QA machine (0 violacións:
> castelanismos, em-dashes, tooltips, drift do glosario = limpo; o verificador
> `tools/check_translation.py` pasa: 87 criterios, 101 dfn, 401 referencias).
>
> Este documento é a axenda da rolda de revisión externa (ILG / universidade /
> profesionais). Cada termo está **usado así no corpus** (o borrador é
> consistente); a pregunta é se a forma galega máis idónea é outra. O glosario
> (`docs/glosario-gl.md`) segue a ser o contrato: aquí só se decide, o corpus
> actualízase despois.

## Bloque A: decisións principais (cambian moitas ocurrencias)

| # | EN | Usada no corpus | Alternativa | Risco do cambio |
|---|---|---|---|---|
| A1 | role (normativo 4.1.x) | **función** | «rol» (comunidade ARIA; Sidar 2.0 usaba «función») | alto: dfn + SC 4.1.2 |
| A2 | assistive technology | **tecnoloxía de asistencia** | «tecnoloxía de apoio» (uso Xunta) | alto: todo o documento |
| A3 | accessibility supported | **con compatibilidade coas tecnoloxías de asistencia** | forma máis curta? | alto: dfn longa e crítica |
| A4 | user | **persoas usuarias** / usuarios (mixto: «user need» = «dos usuarios») | unificar estilo inclusivo | alto: ~centos de casos |
| A5 | language (of a page) | **lingua** | «idioma» | medio |
| A6 | heading | **encabezado** | «cabeceira» | medio |
| A7 | contrast ratio | **razón de contraste** | «proporción de contraste» | medio |
| A8 | viewport | **viewport** (sen traducir) | traducir? | medio: dfn + 1.4.10 |
| A9 | time-based media | **medio tempodependente** | (alineado con Sidar ES) | medio |
| A10 | pointer | **punteiro** | (ningún) | baixo |
| A11 | screen magnifier | **lente de aumento de pantalla** | «magnificador» | baixo |
| A12 | cognitive function test | **proba de función cognitiva** | (ningún) | baixo |

## Bloque B: alternativas menores (unha palabra, risco baixo)

| # | EN | Usada | Alternativa proposta |
|---|---|---|---|
| B1 | conforms / meeting a SC | cumpre / cumprir con | (ningún) |
| B2 | advisory technique | técnica consultiva | (ningún) |
| B3 | programmatically determined | determinado programaticamente | «determinable» |
| B4 | Understandable | Comprensible | (ningún) |
| B5 | input purpose | finalidade da entrada | (ningún) |
| B6 | CSS pixels | píxeles CSS | «píxeles CSS» con lang="en"? |
| B7 | space bar | barra espaciadora | «barra espazadora» |
| B8 | Timeouts | Tempos Límite | «Tempos de inactividade» |
| B9 | Focus Not Obscured | Foco Non Ocultado | «Foco Non Oculto» |
| B10 | Concurrent Input Mechanisms | Mecanismos de Entrada Concomitantes | «de entrada simultánea» |
| B11 | down-event / up-event | sen traducir | «evento de pulsación/liberación» |
| B12 | Reflow | Reaxuste | manter «Reflow» lang="en" |
| B13 | Dismissible/Hoverable/Persistent | Descartable / Se pode pousar o punteiro / Persistente | segundo dt descritivo |
| B14 | Up Reversal | Reversión ao Soltar | (ningún) |
| B15 | flash (plural) | invariable «tres flash» | (ningún) |
| B16 | idioms / jargon | modismos / xerga | (ningún) |
| B17 | tooltips | nota emerxente (5ª rolda; corpus 2× en 1.4.13) vs «tooltip» (glosario tanda 1: sen traducir) | **CONFLITO DOCUMENTAL entre roldas: o corpus xa é consistente («nota emerxente»); resolver a fila do glosario** |
| B18 | hover (verbo/nome) | «paso do punteiro» / «hover» mixto | unificar |

## Bloque C: estilo global (decisión única, afecta ~70 títulos)

Os títulos dos criterios usan **Title Case** herdado do inglés («Tamaño do
Obxectivo (Mínimo)», «Sen Trampa de Teclado»). O galego natural usa minúscula:
«Tamaño do obxectivo (mínimo)». Inventariado 9-nov: **70 h4 en Title Case vs 18
coa minúscula natural** (os 18 son monopalabra ou con numeral). Decidir UNHA
norma para todo o documento antes de que comece a revisión (cambiala despois
dobra o custo).

## Bloque D: pendentes específicos de Jesús

| # | Cuestión | Estado |
|---|---|---|
| D1 | «internacionalmente» (SotD): a IA externa sospeitou errata por «internacioalmente»; o corpus usa a forma correcta | confirmar que queda así |
| D2 | «impresión grande» (SC 1.1) vs «letra ampliada» (Sidar) | pick persoal |
| D3 | «contrasinal» feminino («unha contrasinal», orde 6-nov): a RAG recolleo MASCULINO | mantense feminino; a ILG arbitra |

## Como revisar (protocolo)

1. **Fonte**: `w3c/wcag` tag `WCAG22-20241212`; copia en `source/`. Comparación
   lado a lado xerada en `docs/sbs/` (`tools/gen_sbs.py`).
2. **Contrato terminolóxico**: `docs/glosario-gl.md`. As decisións ✅ están
   fechadas; este documento lista as ⚠️ abertas.
3. **Prioridade de lectura**: (1) `guidelines/index.html` (intro +
   conformidade, ~40 % do texto normativo), (2) as dfn máis citadas
   (content, page, technology, conforming alternate version, accessibility
   supported), (3) os 9 SC novos de 2.2, (4) resto de SC 2.0.
4. **Verificación machine**: `uv run --with beautifulsoup4 python
   tools/check_translation.py` debe seguir en OK após calquera cambio.
5. **Onde se reporta**: un issue por termo do bloque A; os do bloque B en
   lote; o título de cada issue = fila deste documento (A1, B3…).
6. **Nunca tocar**: ids/anchors, numeración, fórmulas, RFC2119 (MUST/SHOULD),
   nomes propios en inglés citados, código de exemplos.
