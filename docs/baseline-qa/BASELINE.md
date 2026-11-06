# Baseline QA del fuente (2026-11-05)

Fuente: `source/guidelines/index.html` @ WCAG22-20241212 (1dfe1647)

- **a11ytoolkit audit (estático, es): score 96/100 — 0 high, 0 medium, 2 low**
- Detalle completo: `audit-fuente.json`

**La traducción debe mantener score ≥ 96 y nunca introducir un hallazgo
high/medium nuevo.** Los 2 low del fuente sirven para verificar que la
traducción no los agrava (mismo número o menos, nunca más).

QA completo en tiempo de entrega: validadores W3C oficiales (Link, Markup,
CSS, i18n) + este audit + diff de ids/anchors vs fuente.
