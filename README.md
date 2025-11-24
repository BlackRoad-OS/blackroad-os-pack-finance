# BlackRoad OS Finance Pack

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![Status](https://img.shields.io/badge/status-active-green)
![Pack](https://img.shields.io/badge/pack-finance-purple)

Financial operations pack for the BlackRoad OS ecosystem. Provides agents and tools for budgeting, reconciliation, forecasting, and financial reporting.

## Overview

The Finance Pack is a vertical pack within the BlackRoad OS ecosystem that handles all financial operations, from budget management to transaction reconciliation and forecasting.

### Pack ID
`pack.finance`

### Agents

| Agent | ID | Description |
|-------|-----|-------------|
| **Budgeteer** | `agent.budgeteer` | Budget management and allocation tracking |
| **Reconcile** | `agent.reconcile` | Transaction reconciliation and variance detection |
| **Forecast** | `agent.forecast` | Financial forecasting and trend analysis |
| **Audit** | `agent.audit` | Compliance verification and duplicate detection |

## Installation

### Prerequisites
- Python >= 3.10
- Node.js >= 18.0.0
- npm >= 9.0.0

### Install Dependencies

```bash
# Python dependencies
pip install -r requirements.txt

# Node.js dependencies
npm install
```

## Usage

### Python CLI

```bash
# Show pack information
python br_fin.py info

# List available agents
python br_fin.py list

# Run specific agent
python br_fin.py run budgeteer check budget-001 5000.00

# Get help
python br_fin.py help
```

### TypeScript Build

```bash
# Build TypeScript code
npm run build

# Run tests
npm test

# Lint code
npm run lint
```

## Agent Examples

### Budgeteer

```python
from agents.budgeteer import Budgeteer
from decimal import Decimal

# Check if expense fits budget
result = budgeteer.check_budget('budget-001', Decimal('5000.00'))
print(f"Approved: {result['approved']}")
print(f"Remaining: {result['remaining']}")
```

### Reconcile

```python
from agents.reconcile import Reconcile
from datetime import datetime
from decimal import Decimal

# Reconcile account
result = reconcile.reconcile_account(
    'account-001', 
    Decimal('100000.00'),
    datetime(2024, 1, 1),
    datetime(2024, 1, 31)
)
print(f"Balanced: {result['is_balanced']}")
print(f"Variance: {result['variance']}")
```

### Forecast

```typescript
import { Forecast } from './agents/forecast';

const forecast = new Forecast();
const result = forecast.simpleMovingAverage(data, 3);
console.log(`Predicted: ${result.predicted}`);
console.log(`Trend: ${result.trend}`);
```

## Directory Structure

```
blackroad-os-pack-finance/
├── agents/           # Finance agents (budgeteer, reconcile, forecast, audit)
├── lib/              # Utility libraries (csv_utils, template)
├── models/           # Data models (ledger_entry, budget_model, types)
├── scripts/          # Build and maintenance scripts
├── configs/          # Configuration files
├── .github/          # GitHub workflows and issue templates
├── pack.yml          # Pack manifest
├── br_fin.py         # Python CLI entry point
├── package.json      # Node.js package configuration
├── requirements.txt  # Python dependencies
├── tsconfig.json     # TypeScript configuration
└── README.md         # This file
```

## Integration

### With Other Packs

- **pack.infra-devops**: Deployment automation
- **pack.research-lab**: Financial ML models
- **blackroad-os-api**: REST endpoints
- **blackroad-os-web**: UI components

### External Services

- Stripe (payments)
- QuickBooks (accounting)
- Plaid (banking data)

## Development

### Running Tests

```bash
# Python tests
pytest -v

# TypeScript tests
npm test
```

### Building

```bash
# Build TypeScript
npm run build

# Run post-build tasks
python scripts/postbuild.py
```

## Deployment

The Finance Pack is designed to deploy on:
- **Railway**: For API and agent services
- **Cloudflare Workers**: For edge functions

## Contributing

See issue templates in `.github/ISSUE_TEMPLATE/`:
- Feature requests: `feature_request.md`
- Bug reports: `bug_report.md`
- New agent proposals: `agent_proposal.md`

### Labels

Use these labels for issues/PRs:
- `team:finance` - Finance team
- `type:feature` - New feature
- `type:bug` - Bug fix
- `type:agent` - New agent
- `pack:finance` - Finance pack
- `prio:P0/P1/P2` - Priority

## Security

**Never commit:**
- API keys or tokens
- Credentials or secrets
- Binary files or proprietary data

See `.gitignore` for excluded patterns.

## License

MIT

## Maintainers

- Team: Finance
- Team: Operator

## Registry

This pack is registered in:
- `blackroad-os-agents/registry/packs.yml`
- Individual agents in `blackroad-os-agents/registry/agents.json`

---

Part of the **BlackRoad OS** ecosystem.

For more information, visit:
- [BlackRoad OS Core](https://github.com/BlackRoad-OS/blackroad-os-core)
- [BlackRoad OS Agents](https://github.com/BlackRoad-OS/blackroad-os-agents)
- [BlackRoad OS Docs](https://github.com/BlackRoad-OS/blackroad-os-docs)