# Blackroad OS Finance Pack (Gen-0)

FinancePack-Gen-0 scaffolds a finance operations toolkit with ledgers, Python models, TS agents, and workflow templates. Everything is text-first for easy review and automation.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python br_fin.py import ledgers
python br_fin.py forecast cash-flow --months 3
```

Render workflow templates:

```bash
pnpm i
pnpm ts-node lib/template.ts workflows/monthly-close.yaml.hbs > .github/workflows/close.yml
```

## Components
- **Ledgers**: CSV double-entry examples under `ledgers/`.
- **CLI**: `br_fin.py` for imports, reconciliation, and forecasting.
- **Models**: Pydantic schemas for ledger entries and budgets.
- **Agents**: TypeScript utilities for forecasting and template rendering.
- **Workflows**: Handlebars YAML templates for recurring finance actions.

## Notes
- Keep files under 120 lines; use Mermaid for diagrams when needed.
- TODO(fin-pack-next): multi-currency support, Stripe webhook agent, SEC filing generator.
