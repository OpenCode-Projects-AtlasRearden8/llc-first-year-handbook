# The First-Year LLC Handbook

A manual for surviving **and enjoying** the first year of running a single-owner LLC — written from the author's own launch: **Asdale Dynamics, LLC, an Indiana LLC formed in October 2026.** Plain English, step by step, like a friend explaining paperwork over coffee — the style [dylanasdale.github.io](https://dylanasdale.github.io) uses for AI.

**Orientation only, never legal, tax, or financial advice.** Every chapter says so, every chapter points to the official source (IRS.gov, INBiz, Indiana DOR), and the last chapter tells you exactly when a licensed professional takes over.

## What's inside

| Chapter | Covers |
|---|---|
| [Start here](docs/index.md) | The promise, the map, the three habits that carry the year |
| [Bank accounts](docs/bank-accounts.md) | Free EIN, business checking, the two-pot system, paying yourself |
| [Simple record habits](docs/records.md) | The ten-minute week, the four-folder year, starter categories, mileage |
| [Quarterly money dates](docs/money-dates.md) | The 90-minute, four-times-a-year ritual — with an ADHD-friendly three-sprint version |
| [Estimated taxes](docs/taxes.md) | Round-number set-asides, the safe harbor in plain words, the four due dates |
| [Insurance starters](docs/insurance.md) | GL → BOP → E&O → media → the personal-side gaps, in buying order |
| [The annual-report ritual](docs/annual-report.md) | Indiana's *biennial* Business Entity Report, registered agent, the BOI footnote |
| [When to call a pro](docs/professionals.md) | Ten triggers, the roles sorted, the first-call script, what to bring |
| Checklists | [First 30 days](docs/checklists/first-30-days.md), [quarterly money date](docs/checklists/quarterly-money-date.md), [year end](docs/checklists/year-end.md) |

## Run it

Everything is markdown + a zero-dependency Python build script. No accounts, no API keys, no cloud. Local-first.

```bash
python3 build.py            # build the static site into site/
python3 build.py --check    # build, verify every internal link, then clean up (CI-style test)
python3 -m pytest tests/ -q # full test suite
python3 -m http.server -d site 8000  # optional: browse at http://localhost:8000
```

Requires Python 3.9+ (stdlib only) to build; tests additionally use pytest. The chapters under `docs/` read fine as plain markdown; the `site/` output is for reading or hosting anywhere static.

## Relationship to its siblings

This handbook **complements, and deliberately does not repeat**, two other Asdale Dynamics, LLC projects:

- **[cashflow-simple-ledger](../cashflow-simple-ledger)** — the *tool*: a local-first CLI that tracks income and expenses in one portable CSV, with bank-CSV imports and a tax-season export. This handbook's [record habits chapter](docs/records.md) is the *habit* around that tool.
- **[small-business-ai-playbook](../small-business-ai-playbook)** — the *co-pilot*: a monthly money-date, decision journal, and SOPs for running a one-person LLC with AI. This handbook's quarterly money date is that chapter's deeper, slower sibling.

Between the three: the ledger tracks the money, the playbook helps you think, and this handbook keeps the state, the IRS, the calendar, and the insurance company quietly on your side.

## Colophon

Copyright (c) 2026 Asdale Dynamics, LLC. Released under the MIT license (see [LICENSE](LICENSE)). Built from local markdown files by `build.py` — no secrets, no personal data, no build-time network calls.
