# Como colaborar / Cómo colaborar / How to contribute

Grazas por axudar a que as WCAG 2.2 teñan a súa primeira tradución ao galego.
Esta é a primeira da historia e pretende chegar a ser **Candidata a Tradución
Autorizada** do W3C, así que a calidade é o obxectivo número un.

## Que se necesita

- **Revisión técnica de accesibilidade**: persoas que dominen WCAG e poidan
  comprobar que cada criterio di exactamente o que di o orixinal en inglés.
- **Revisión lingüística**: falantes de galego con formación en tradución
  (a industria, o [Instituto da Lingua Galega](https://ilg.usc.gal/) e o
  [programa Mancomún](https://mancomun.gal/) da Xunta son as referencias que
  buscamos incorporar formalmente).
- **Organizacións representativas**: entidades de persoas usuarias da lingua e
  de persoas con discapacidade que queiran formar parte do grupo de revisión
  que a política W3C esixe para unha Tradución Autorizada.

## Como propoñer correccións

Abre unha [incidencia](https://github.com/kinti/wcag22-gl/issues/new) con este
formato (permite avaliar e aplicar rápido):

```
Apartado:        2.4.7 Foco Visible / Glosario «contrasinal» / §5 Conformidade
Texto actual:    «...texto galego tal como está agora...»
Proposta:        «...texto galego que propoñes...»
Xustificación:   por que (norma RAG, Termigal, sentido do orixinal EN,
                 práctica da accesibilidade en galego, ...)
Referencia EN:   cita curta do orixinal inglés, se procede
```

Podes enviar lotes (unha incidencia por pauta ou capítulo). Non precises
abrir un pull request para correccións de texto: valen as incidencias; os
mantedores aplican e rexistran no glosario canónico
(`docs/glosario-gl.md`), que é o documento que fai cumprir o control de
coherencia.

## Normas do proxecto (as duras do W3C)

- **Non se traducen os ids nin se toca o CSS** — as áncoras do orixinal e da
  tradución deben coincidir.
- Todo o texto que permaneza en inglés levara `lang="en"`.
- A orixinal inglesa é a única versión normativa: calquera emenda debe
  xustificarse contra ela, non contra outra tradución.
- O glosario (`docs/glosario-gl.md`) é canónico: un cambio de termo entra
  alí primeiro e logo propágase.

## Como xerar o documento

Ver `README.md` § «Como ler e xerar o documento»: preview determinista,
captura do render e `tools/make_export.py` (auto-comproba restos de inglés).

## Ruta cara á Tradución Autorizada

1. Esta tradución voluntaria proponse como *Candidate Authorized
   Translation* (a política W3C permite promocionar unha tradución existente).
2. Período de revisión pública de polo menos 30 días en lista dedicada.
3. Decisión do W3C → publicación con endoso + páxina de erratas permanente.
