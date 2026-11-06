# Glosario EN → GL — referencia canónica del proyecto

> **VALIDADO por Jesús (2026-11-06): este glosario es vinculante.** Cada
> decisión nueva se añade aquí ANTES de entrar en un borrador; el QA de
> coherencia grepa contra este fichero. El endoso EXTERNO (ILG / coalición)
> queda pendiente como formalidad de la ruta CAT — si la coalición propone
> un cambio, se actualiza aquí primero y después los borradores.
> Marcas: ✅ cerrado · ⚠️ abierto para la revisión externa (mientras tanto,
> la forma GL escrita en la fila es LA QUE SE USA).

## Principios y estructura

| EN | GL proposta | | Nota |
|---|---|---|---|
| Web Content Accessibility Guidelines (WCAG) | Pautas de Accesibilidade para o Contido Web (WCAG) | ✅ | continuidade con «Pautas» (Sidar/CAT) |
| guideline | pauta | ✅ | |
| principle | principio | ✅ | |
| Success Criterion (SC) | criterio de éxito | ✅ | manter «SC»/numeración (1.1.1…) en inglés |
| Level A / AA / AAA | Nivel A / AA / AAA | ✅ | «Level» → «Nivel» (tradúcese SIEMPRE); as LETRAS A/AA/AAA quedan sen traducir |
| conformance | conformidade | ✅ | |
| conforms / meeting a SC | cumpre / cumprir con | ⚠️ | |
| requirement | requisito | ✅ | |
| advisory technique | técnica consultiva | ⚠️ | |
| sufficient technique | técnica suficiente | ✅ | |
| failure (technique) | fallo (técnica) | ✅ | |

## Principios (nombres)

| EN | GL proposta | |
|---|---|---|
| Perceivable | Perceptible | ✅ |
| Operable | Operable | ✅ |
| Understandable | Comprensible | ⚠️ |
| Robust | Robusto | ✅ |

## Actores y tecnología

| EN | GL proposta | | Nota |
|---|---|---|---|
| user agent | axente de usuario | ✅ | |
| assistive technology (AT) | tecnoloxía de asistencia | ⚠️ | alternativa: «tecnoloxía de apoio» (Xunta); confirmar |
| author | autor | ✅ | |
| content | contido | ✅ | |
| web page | páxina web | ✅ | |
| web site / set of web pages | sitio web / conxunto de páxinas web | ✅ | |
| programmatically determined | determinado programaticamente | ⚠️ | |
| accessibility-supported | compatibilidade coas tecnoloxías de asistencia | ⚠️ | termo difícil; prioridade ILG |
| platform | plataforma | ✅ | |
| technology (web technology) | tecnoloxía (tecnoloxía web) | ✅ | |
| user | usuario / usuaria | ⚠️ | estilo inclusivo = decisión ILG |
| disability | discapacidade | ✅ | |

## Contenidos y medios

| EN | GL proposta | | Nota |
|---|---|---|---|
| text alternative | alternativa textual | ✅ | |
| non-text content | contido non textual | ✅ | |
| time-based media | medio tempodependente | ⚠️ | alineado con Sidar («tempodependiente»); decisión de tanda 1 |
| audio-only / video-only | só audio / só vídeo | ✅ | |
| captions | subtítulos | ✅ | |
| audio description | audiodescrición | ✅ | |
| transcript | transcrición | ✅ | |
| data table | táboa de datos | ✅ | |
| link | ligazón | ✅ | |
| label | etiqueta | ✅ | |
| error | erro | ✅ | |
| heading | encabezado | ⚠️ | alternativa «cabeceira»; confirmar |
| keyboard interface | interfaz de teclado | ✅ | singular «interfaz» por decisión de Jesús; plural «interfaces» |
| keyboard shortcut | atallo de teclado | ✅ | |
| focus | foco | ✅ | |
| focus indicator | indicador de foco | ✅ | termo novo 2.2 |
| pointer | punteiro | ⚠️ | |
| dragging movement | movemento de arrastre | ✅ | termo novo 2.2 |
| target (pointer) | obxectivo | ✅ | decisión de Jesús 6-nov: «diana» descartada; aplica a 2.5.5/2.5.8 |
| minimum bounding box | caixa delimitadora mínima | ✅ | termo novo 2.2 |
| perimeter | perímetro | ✅ | termo novo 2.2 |
| cognitive function test | proba de función cognitiva | ⚠️ | termo novo 2.2 |
| session | sesión | ✅ | |
| relative luminance | luminancia relativa | ✅ | |
| contrast ratio | razón de contraste | ⚠️ | alternativa «proporción»; confirmar |
| CSS pixels | píxeles CSS | ⚠️ | «CSS pixels» con lang="en"? confirmar convención |
| viewport | viewport | ⚠️ | manter EN con lang="en" ou traducir? confirmar |
| zoom | zoom | ✅ | manter (uso xeral) |
| orientation | orientación | ✅ | |
| input purpose | finalidade da entrada | ⚠️ | input-purposes.html |
| consistent help | axuda consistente | ✅ | |
| redundant entry | entrada redundante | ✅ | |
| accessible authentication | autenticación accesible | ✅ | |
| language of a page | lingua da páxina | ⚠️ | «lingua» vs «idioma» = decisión ILG |

## NUNCA se traducen (con lang="en" se aparecen en texto)

- Todos os **ids** e anchors
- **WCAG**, **W3C**, **ARIA**, **HTML**, **CSS**, **URI/URL**, **UTF-8**
- Nomes de produtos e tecnoloxías: ReSpec, fixup.js, JavaScript
- Numeración de SC (1.1.1 … 4.1.1), niveis A/AA/AAA
- Título orixinal EN na cabeceira do disclaimer
- Referencia ao LTO no disclaimer
- Contido de `acknowledgements/` referente a NOMES de persoas
- Palabras reservadas de exemplos de código

## Cadena UI de fixup.js (únicas 3 cadeas)

| EN | GL proposta |
|---|---|
| Collapse Sidebar | Contraer a barra lateral |
| Pop Out Sidebar | Despregar a barra lateral |
| Jump to Table of Contents | Ir ao índice de contidos |

## Cadena UI do export (pasos 5)

| EN | GL proposta |
|---|---|
| Permalink | Ligazón permanente |
| Referenced in: | Mencionado en: |
| Understanding | Comprender |
| How to Meet | Como cumprir |
| Table of Contents | Índice de contidos |

## Decisións da tanda 1 (P1, 29 SC — borrador G 5-nov, a correxir por Jesús/ILG)

| EN | GL usada no borrador | Nota |
|---|---|---|
| time-based media | medio tempodependente | aliñado con Sidar («tempodependiente») — fila principal actualizada |
| extended audio description | audiodescrición estendida | «estendida» (RAG) non «extendida» |
| Reflow | Reaxuste | ⚠️ alternativa: manter «Reflow» con lang="en" |
| viewport | viewport (sen traducir) | usado na nota de 1.4.10 |
| scroll | scroll (sen traducir) | verbo/nome común técnico |
| Large Text / Large-scale | Texto Grande / a gran escala | |
| logotypes | logotipos | |
| mechanism | mecanismo | |
| foreground / background | primeiro plano / fondo | |
| decibel | decibelio | |
| justified | xustificado | |
| layout | disposición | |
| human languages | linguas humanas | «lingua» confirmar con ILG |
| scripts (writing) | escrituras | |
| dithering | tramado (dithering) | con parentese EN na primeira mención |
| pointer hover | paso do punteiro | |
| keyboard focus | foco de teclado | |
| input error | erro de entrada | |
| sub-menus / nonmodal popups | submenús / ventás emerxentes non modais | |
| tooltips | tooltips (sen traducir) | |
| Dismissible / Hoverable / Persistent (dt) | Descartable / Se pode pousar o punteiro / Persistente | ⚠️ o segundo é descritivo; alternativa «Permite o hover» |
| Guideline X / Success Criterion X.Y.Z / Conformance Requirement | Pauta X / Criterio de Éxito X.Y.Z / Requisito de Conformidade | textos de link traducidos, hrefs intactos |
| New (clase change, soamente 2.2) | Novo | usar cando apareza |

## Decisións da tanda 2 (P2, 34 SC — borrador G 6-nov, a correxir por Jesús/ILG)

| EN | GL usada no borrador | Nota |
|---|---|---|
| No Keyboard Trap | Sen Trampa de Teclado | |
| keystroke | pulsación de tecla | |
| timings | temporizacións | |
| path of the user's movement | traxectoria do movemento da persoa usuaria | |
| down-event / up-event | sen traducir (termos técnicos normativos) | ⚠️ alternativa «evento de pulsación/liberación» |
| Turn off | Desactivar | ✅ unificado por Jesús 6-nov en TODOS os contextos (1.4.7 sonos tamén: «Apagar» retirado) |
| Remap | Reasignar | corrección aceptada en la quinta ronda |
| Timing Adjustable | Temporización Axustable | |
| time limit | límite de tempo | |
| Extend | Estender | RAG estender |
| Real-time event | evento en tempo real | |
| space bar | barra espaciadora | ⚠️ «barra espazadora» variante |
| Pause, Stop, Hide | Pausar, Deter, Ocultar | |
| blinking | parpadeante / parpadeo | |
| auto-updating | actualización automática | |
| preload | precarga | |
| frozen | conxelado | |
| postponed / suppressed | aprazadas / suprimidas | ✅ corrección de Jesús 6-nov (era «apalazadas», non existe) |
| emergency | emerxencia | |
| Re-authenticating | Reautenticación | |
| Timeouts | Tempos Límite | ⚠️ alternativa «Tempos de inactividade» |
| user inactivity | inactividade de usuario | |
| minor | menor de idade | |
| flash | flash (invariable) | ⚠️ plural: «tres flash» |
| threshold | limiar | |
| flickering | tremelicita | |
| Bypass Blocks | Saltar Bloques | |
| Focus Order | Orde do Foco | RAG «orde» |
| Link Purpose (In Context / Link Only) | Propósito da Ligazón (No Contexto / Só a Ligazón) | |
| ambiguous to users in general | ambiguo para as persoas usuarias en xeral | |
| Multiple Ways | Múltiples Vías | |
| Section Headings | Encabezados de Sección | |
| Focus Not Obscured | Foco Non Ocultado | ⚠️ alternativa «Foco Non Oculto» |
| author-created content | contido creado pola persoa autora | |
| Focus Appearance | Aparencia do Foco | |
| sub-component | subcompoñente | |
| glow | resplandor | |
| anti-aliasing | suavizado de bordos (anti-aliasing) | primeira mención con EN |
| drop-down menu | menú despregable | |
| grid | grella | |
| Pointer Gestures | Xestos de Punteiro | |
| path-based gesture | xesto baseado en traxectoria | |
| single pointer | único punteiro | |
| Pointer Cancellation | Cancelación do Punteiro | |
| Up Reversal (dt) | Reversión ao Soltar | ⚠️ |
| Target Size | Tamaño do Obxectivo | ✅ decisión de Jesús 6-nov (era ⚠️ «diana»); borradores 2.5.5/2.5.8 xa alineados |
| pointer inputs | entradas de punteiro | |
| bounding box | caixa delimitadora | |
| sliders / color pickers | deslizadores / seleccionadores de cor | |
| Concurrent Input Mechanisms | Mecanismos de Entrada Concomitantes | ⚠️ alternativa «de entrada simultánea» |
| Motion Actuation | Activación por Movemento | |

## Decisións da tanda 3 (P3, 21 SC — borrador G 6-nov, a correxir por Jesús/ILG)

| EN | GL usada no borrador | Nota |
|---|---|---|
| Language of Page / of Parts | Lingua da Páxina / Lingua das Partes | segue o ⚠️ do glosario (lingua vs idioma) |
| passage | pasaxe | |
| vernacular | vernáculo | |
| Unusual Words | Palabras Inusuais | |
| idioms / jargon | modismos / xerga | ⚠️ modismos |
| expanded form | forma expandida | |
| lower secondary education level | nivel de educación secundaria inferior | |
| supplemental content | contido complementario | |
| Pronunciation | Pronuncia | |
| On Focus / On Input | Ao Recibir o Foco / Na Entrada | |
| change of context | cambio de contexto | |
| setting (UI component) | axuste | |
| Consistent Navigation / Identification / Help | Navegación/Identificación/Axuda Consistente | |
| same relative order | mesma orde relativa | |
| Change on Request | Cambio a Petición | turn off → desactivar (unificado) |
| serialized | serializada | |
| page variation / CSS break-point | variación de páxina / punto de ruptura CSS | |
| Error Identification / Suggestion | Identificación de Erros / Suxestión de Erro | |
| Error Prevention (Legal, Financial, Data / All) | Prevención de Erros (Legal, Financeiro, Datos / Todo) | |
| legal commitments | compromisos legais | |
| user-controllable | controlable polo usuario | |
| Reversible / Checked / Confirmed (dt) | Reversible / Verificado / Confirmado | |
| submission | envío | |
| context-sensitive help | axuda sensible ao contexto | |
| human contact details/mechanism | datos/mecanismo de contacto humano | |
| self-help option | opción de autoaxuda | |
| auto-populated | autocompletada | |
| puzzle | quebracabezas | |
| password managers | xestores de contrasinais | |
| cognitive burden | carga cognitiva | |
| Object Recognition / Personal Content (dt) | Recoñecemento de Obxectos / Contido Persoal | |

## Decisións da tanda 4 (P4, 3 SC — borrador G 6-nov, a correxir por Jesús/ILG)

| EN | GL usada no borrador | Nota |
|---|---|---|
| Parsing (Obsolete and removed) | Análise (Obsoleto e retirado) | 4.1.1 obsoleto — tradúcese igualmente, segue no documento |
| role (termo normativo 4.1.x) | función | ⚠️ IMPORTANTE: a comunidade ARIA di «rol»; Sidar 2.0 usaba «función». DECIDIR: función vs rol |
| programmatically set | establecido programaticamente | |
| notification of changes | notificación dos cambios | |
| Status Messages | Mensaxes de Estado | |
| script (en texto) | script (sen traducir) | |

## Decisións da fase TERMS (102 dfn — borrador G 6-nov, a correxir por Jesús/ILG)

| EN | GL usada no borrador | Nota |
|---|---|---|
| id/data-lt dos dfn | SEN TOCAR (inglés) | regra dura: anchors match; só o texto visible se traduce |
| abbreviation | abreviatura | siglas (initialisms) e acrónimos diferenciados |
| accessibility supported | con compatibilidade coas tecnoloxías de asistencia | forma adxectiva longa nos termos; nos SC usouse «con compatibilidade coas tecnoloxías de asistencia» |
| ASCII art | arte ASCII | |
| screen magnifier | lente de aumento de pantalla | ⚠️ alternativa «magnificador» |
| screen reader | lector de pantalla | |
| sip/puff | sopro/suxión | |
| rely upon | basearse en | «relied upon» = «nas que se basea» |
| contrast ratio formula | fórmulas intactas | L1/L2, sRGB etc. só prosa traducida |
| general/red flash thresholds | limiares de flash xeral e de flash vermello | flashs invariable no plural |
| initialism / acronym | sigla / acrónimo | |
| Closed/Open Captions | subtítulos pechados/abertos (con EN na primeira mención) | |
| broadcast delay | retraso de emisión | |
| keyboard interface | interfaz de teclado | MouseKeys sen traducir; decisión posterior de Jesús |
| legal commitments | compromisos legais | |
| link purpose | propósito da ligazón | |
| mechanism | mecanismo | |
| navigated sequentially | navegada secuencialmente | |
| viewport | viewport (sen traducir, termo definido) | excepción á nota da tanda 1: como é o TERMO definido, o dfn queda «viewport» |
| programmatically determined | determinado programaticamente | (determinable programaticamente) |
| process | proceso | |
| pure decoration | decoración pura | |
| real-time event | evento en tempo real | |
| relied upon | basearse en | |
| role | función | ⚠️ vixente a decisión de tanda 4 (función vs rol) |
| satisfies a success criterion | cumpre un criterio de éxito | |
| supplemental content | contido complementario | |
| synchronized media | medios sincronizados | |
| target | obxectivo | decisión de Jesús 6-nov |
| down-event/up-event | sen traducir | |
| single pointer | único punteiro | estilete para stylus |
| style property | propiedade de estilo | |
| state | estado | hover/select sen traducir na enumeración |
| user inactivity | inactividade de usuario | |
| motion animation | animación de movemento | |
| minimum bounding box | caixa delimitadora mínima | |
| perimeter | perímetro | fórmulas intactas |
| web page | páxina web | |

## Revisión de Jesús no preview (6-nov)

| Termo/cuestión | Decisión | Estado |
|---|---|---|
| testable | **comprobable** (era «probable», ERRO sistemático: probable=likely ≠ testable) | ✅ corrixido en index (6×+comprobabilidade); «probablemente» en 3.2.6 é CORRECTO (=likely) |
| user need | necesidades das persoas usuarias (era «necesidades de usuaria», concordanza rota) | ✅ |
| escríbense / fornécese / fornécense | verbos con enclítico correctos (escriben+se, fornecer+se) | ✅ |
| de modo que | **de xeito que** (preferencia de Jesús) | ✅ 5× corrixido |
| em-dash — | eran MÍOS (o fonte usa « - »); revertidos os 10 do index; o de user-agent vén do fonte e QUEDA | ✅ |
| metodología/evaluaronse | metodoloxía/avaliaronse (galegismos) | ✅ |
| internacionalmente | CORRECTA así; «internacioalmente» semella errata — NON aplicado | ⚠️ confirmar con Jesús |
| interface | **interfaz — APLICADA** (2ª orde expresa de Jesús 6-nov, 47×/29 ficheros; plural «as interfaces»); o pushback RAG/Termigal queda rexistrado para ILG | ✅ decidida |
| Guidelines / Success Criterion | TRADÚCENSE (Pautas / Criterio de Éxito); en inglés quedan SOLO: nome propio «Accessibility Guidelines Working Group», sotd (lang=en), nomes históricos citados no changelog (lang=en), e a UI/cabeceira de ReSpec (tradúcese no paso 5 do how-to: «translate the .head») | ✅ política documentada |

## Segunda rolda de revisión de Jesús (6-nov, cos seus picks)

| Termo | Decisión | Estado |
|---|---|---|
| user need | **dos usuarios** (non «persoas usuarias») — marca a dirección do ⚠️ usuario/usuaria | ✅ 2× |
| escríbense | **redáctanse** (preferencia de Jesús) | ✅ |
| Success Criterion | **criterio de éxito MANTIDO** — pick de Jesús coa recomendación (tradición Sidar ES 2.0 + catalán authorized «criteris d'èxit» + glosario validado); descartado «criterio de aceptación» | ✅ pechado |
| fornecer | **proporcionar en TODO** (pick de Jesús; 53×/23 ficheros con conxugación: fornécese→proporciónase, fornécense→proporciónanse…) | ✅ global |

## Decisións do EXPORT (6-nov, tras preguntas de Jesús sobre o inglés)

| Cuestión | Decisión | Evidencia |
|---|---|---|
| sotd (Estado do documento) | **TRADÚCESE** (revertida a miña decisión de mantelo en EN) | catalán authorized («Estat d'aquest document») + Sidar ES tradúceno |
| cabeceira .head | toda en galego: Recomendación do W3C do… / Esta versión / Última versión publicada / Último esborrany do editor / Historia / Comentarios | catalán authorized + Sidar; o how-to paso 5 esixe «translate the .head» |
| data de publicación | 12 de decembro de 2024 (ReSpec deuna «diciembre» — fallback es — corrixida no export) | |
| ToC | Índice de contidos | glosario UI |
| Understanding / How to Meet | Comprender X / Como cumprir X (levan o nome do SC/pauta) | catalán: «Com s'interpreta / Com es compleix» |
| Permalink / Referenced in | Ligazón permanente / Mencionado en: | |
| queda en inglés | nome propio AG WG, empresas, URLs w3.org, lang="en" citado (changelog histórico, título orixinal no disclaimer, legal funders) | mesmo criterio có catalán authorized |
| export v1 | work/export/index.html — audit 88/100, 0 high (só FP lang="sm" do propio motor, presente no EN orixinal) | |

## Terceira rolda de revisión (6-nov, preview export)

| Termo | Decisión | Estado |
|---|---|---|
| Nova funcionalidade | **Novas funcionalidades** | ✅ |
| seguranza | **seguridade** (13×; «seguranza» retirada do corpus) | ✅ global |
| «Preténdese que… tamén cumpren» | **tamén cumpran** (subjuntivo obrigado polo verbo rexente; «cumpren» indicativo NO resto, ex.: «os sitios que cumpren… tamén cumpren» sen gatillo) | ✅ |
| do nivel de volume | **do nivel do volume** | ✅ |
| secno xerado «Success Criterion 1.1.1» | **Criterio de Éxito 1.1.1** (wcag.js REESCRIBE o número; tradúcese no export) | ✅ |
| Note xerado (span ×47) | **Nota** (ReSpec xera o marcador; tradúcese no export) | ✅ |
| Guidelines restantes | bibliografía + nome propio AG WG → EN (mesmo criterio) | ✅ documentado |
| «impresión grande» (GL 1.1) | vén de *«such as large print, braille, speech, symbols or simpler language»*; alternativa Sidar: «letra ampliada» | ⚠️ a pick de Jesús |

## Cuarta rolda de revisión (6-nov, export)

| Termo | Decisión / orixe | Estado |
|---|---|---|
| producease (2.5.2) | ERRO meu: era o imperfecto; correcto **prodúcese** (presente de producir, con acento) | ✅ |
| contrasinal | **feminino** (orde de Jesús: «unha contrasinal», 5×; ⚠️ NOTA para ILG: o dicionario da RAG recolleo como MASCULINO — «o contrasinal», por «sinal» m.; arbitrará a revisión externa) | ✅ aplicado + ⚠️ ILG |
| automaticamente | CORRECTO sen tilde: en galego os adverbios en -mente non levan acento (norma RAG; o español «automáticamente» non aplica). Corpus: 11×, ningunha con acento | ✅ sen cambio |
| RFC2119 keys (MAY, MUST…) | **NO se traducen**: son as palabras clave DEFINIDAS polo RFC; o propio texto explica «tal e como se amosan aquí»; Sidar mantívoas igual | ✅ sen cambio |
| «Ademais» sen tilde | CORRECTO: a acentuación galega só acentúa agudas terminadas en vogal/-n/-s; as palabras graves rematadas en -s NON levan tilde (a diferenza do español). Compara «tamén», que sí (aguda en -n) | ✅ sen cambio |
| disclaimer LTO | **«Tradución liderada por Jesús Quintana (a11y.es)»** (orde de Jesús) | ✅ |
| Tres Flash ou Por Debaixo do Limiar (2.3.1) | literal de «Three Flaves or Below Threshold». ⚠️ NOTA estilo: os títulos usan maiúscula inglesa (Title Case) herdada; o galego natural usaría minúscula («Tres flash ou por debaixo do limiar») — decisión de estilo para a rolda ILG en TODO o documento | ⚠️ ILG |
| bug «aparecen in all maiúsculas» | bug do make_export.py (comentario ReSpec partía a frase) → «aparecen en maiúsculas» | ✅ |

## Quinta rolda: revisión dunha IA externa (validada por G + fixes de G, 6-nov)

**Lingüístico aplicado** (decisións da IA externa, aceptadas):
cumple/cumplir→cumpre/cumprir (restos casteláns meus), cuyo→cuxo, personas→persoas,
accesibilidad→accesibilidade, a o que→ao que, (o funcionalidade)→(ou funcionalidade),
demonístrese→demóstrase, andes→estantes (web-page), padróns→**patróns**,
remapear→**reasignar**, gatillo→**disparador**, tooltip→**nota emerxente** (⚠️「tooltip»
estaba decidido sen traducir — a IA externa traduciu; queda a decisión da última rolda),
padding→**recheo**, plugin→**complemento**, soportado→**compatible/admitido**, Female→Feminino,
profesións/IEC/citas EN marcadas lang="en", MathML mtext and→e, relative-luminance xml:lang=gl.

**Estrutural (a IA externa diagnosticou ben, G reconstruíu os datos)**:
- IDs x… TRADUCIDOS xerados por wcag.js rompían «do not translate ids» — RESTAURADOS ao EN
  (mapa posicional render EN↔GL: 134 entradas en tools/original-heading-ids.json; o mapa da
  IA externa tiña os valores ben pero emparellados MAL — renomeaba ids orixinais: sotd→table-of-contents)
- doclinks Understanding/quickref con slug galego (143 rotos) → restaurados (97 entradas)
- **python -m http.server DROPEA fragmentos ao azar** (respec-offender-data-include-failed;
  renders con SCs desaparecidos) → tools/inline_preview.py pre-inlina os 192 includes (determinista, 0 fallos)
- **id="conformance" explícito na sección creaba unha sección fantasma** (5.1 Conformidade,
  renumeración 5.1.2.1) → sección anónima coma o fonte + renome conformidade→conformance no export
  (how-to cumprido, numeración EN exacta: 5.1/5.2/5.2.1)
- editores W3C ORIXINAIS restaurados en respec-config (o how-to di «translate the editors list»,
  non substituíla — o equipo de tradución vive no disclaimer; erro meu anterior)
- fixup.js con estrutura i18n {en, gl} (correcto)
- wcag.js só inxecta os bloques canónicos (As-well/RFC) se a sección ten id → agora inxéctaos
  make_export.py coas nosas versións galegas; a nosa frase RFC2119 do fonte sobrevive

**Flujo canónico de export**: inline_preview.py → captura (receptor POST) → make_export.py
(self-check). Marcador final: 0 ids fóra do EN, 0 duplicados, 87 SC, 101 dfn, 0 doclinks GL,
biblio 13, audit 88/100 0 high; paridade corpus 190/190.

## Correcciones de la revisión del 6 de noviembre de 2026

Autorizadas por Jesús al pedir resolver todos los hallazgos de la revisión.
Se mantienen las preferencias anteriores, incluido «interfaz», «obxectivo»,
«criterio de éxito» y el género femenino de «contrasinal» pendiente de revisión externa.

| EN / cuestión | GL / decisión |
|---|---|
| synchronized visual and/or text alternative | alternativa visual e/ou textual sincronizada; la sincronización es obligatoria en ambos casos |
| resumed | retomado; nunca «reprendido» |
| relied upon | basearse en; el sujeto es el cumplimiento o la conformidad, no la tecnología |
| flashing | sucesión de flash; «flash» se mantiene invariable en plural |
| pattern | patrón; aplicar también en singular |
| bidding | poxando |
| spoon | culler; «cullerada» significa una cantidad |
| provide | proporcionar en todas sus formas, conforme a la decisión anterior |
| Remap | Reasignar también en los encabezados |
| definition / Activate to close this dialog | definición / Activar para pechar este diálogo |
| Note 1, Note 2… | Nota 1, Nota 2… |
| bibliografía y proceso W3C | conservar las referencias y las fechas del original publicado del 12 de diciembre de 2024 |

Los resultados de la quinta ronda eran históricos y no acreditaban un export
limpio: la revisión posterior encontró 98 referencias sin destino, tres IDs de
encabezado distintos del original y textos generados sin traducir. Las nuevas
comprobaciones deben cotejarse con el HTML inglés publicado, además del tag.
