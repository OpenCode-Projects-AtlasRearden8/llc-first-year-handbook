# STATUS

## What was built

**The First-Year LLC Handbook** — a manual for surviving *and enjoying* the first year of a single-owner LLC, written from the author's own launch (Asdale Dynamics, LLC, an Indiana LLC formed October 2026). Plain English, warm, ADHD-friendly, local-first.

### Content (`docs/` — 8 chapters + 4 checklists, ~2,000 lines of markdown)

- `index.md` — the promise, the first-year arc, the three habits, the family map (complements — does not repeat — both sibling projects)
- `bank-accounts.md` — free IRS EIN (five-second CP 575 backup), picking a bank, honest bring-list, the **two-pot system** (checking + untouchable tax savings), the pay-yourself loop, harmless wobbles and one-line fixes
- `records.md` — the one-ledger rule, the ten-minute week, the four-folder year, starter categories (12), the tiny mileage log, paying yourself on record (single-member LLC is a disregarded entity, in plain words)
- `money-dates.md` — the 90-minute **quarterly** money date: seven-question agenda, five-number scoreboard, gentle three-sprint ADHD version, what does *not* happen at a money date. Deliberately the deeper sibling of the playbook's monthly money-date
- `taxes.md` — why estimated taxes exist (no employer withholding), the three levels (federal income, ~15.3% self-employment, Indiana 2.95% state + county), the **round-number pot** (25–30% of net profit with a $10,000 worked example), the safe harbor as two ladders, the four due dates (April/June/September/January + 15), free payment routes
- `insurance.md` — buying order (GL → BOP → E&O → media → cyber → health/disability), what the author-educator actually needs (E&O for published advice; disclaimers soften, they don't stop claims), seven quoting questions, comparably honest ballparks, what to skip in year one
- `annual-report.md` — Indiana's **biennial** Business Entity Report (every other year, anniversary month, $31 online / $50 mail, 90-day early window, administrative dissolution after five months overdue — all verified at the [SOS source](https://www.in.gov/sos/business/business-entity-reports) in late 2026), the yearly ritual that orbits it, registered-agent arrangements, and the FinCEN **BOI** status as verified October 2026 (U.S. companies permanently exempt per the August 11, 2026 final rule)
- `professionals.md` — ten triggers, the roles table (bookkeeper vs tax preparer vs CPA vs EA vs attorney vs agent), arriving prepared, the first-call script, the two-question triage, and the AI boundary ("AI prepares; professionals decide")
- `checklists/` — `first-30-days.md` (four sittings), `quarterly-money-date.md` (print-and-fill agenda), `year-end.md`, plus `index.md`. All checkbox-styled, printable

### Tooling

- `build.py` — zero-dependency (Python stdlib only) static site generator: markdown → styled HTML with sidebar nav, prev/next, link rewriting, checkbox rendering, and a link/fragment verifier that **fails the build on broken internal links**. One real fix over the house template: task-list `[ ]` boxes now render as spans instead of escaped markup
- `tests/test_build.py` — 21 pytest tests (see below)
- `site/` — generated output (gitignored), self-contained, no external assets

### Meta

- `LICENSE` — MIT, copyright line exactly "Copyright (c) 2026 Asdale Dynamics, LLC"
- `README.md` — run instructions, chapter table, complements both siblings, credits Asdale Dynamics, LLC
- No secrets, API keys, or personal data anywhere (a test enforces a leak scan). Local-first: no accounts, no network at build or run time.
- Committed as the existing git identity (Dylan Asdale), plain message, no trailers. Never pushed; no remote.

## How to run it

```bash
python3 build.py                      # build the static site into site/
python3 build.py --check              # build + verify all links, then clean up (0 artifacts)
python3 -m pytest tests/ -q           # full test suite
python3 -m http.server -d site 8000   # browse the built site at http://localhost:8000
```

Requires Python 3.9+ (stdlib only) to build. Tests need pytest (present in this environment).

## Verification results (all run in this repo, final state)

| Check | Result |
|---|---|
| `python3 build.py` | OK — 12 pages, all internal links verified |
| `python3 build.py --check` | OK — built + verified + cleaned up, `site/` removed |
| `python3 -m pytest tests/ -q` | **21 passed** |
| Markdown → HTML spot-check | No markup leaks (`**`, fenced code, escaped spans) in any rendered page |
| Generated-site size | 12 self-contained HTML pages, inline CSS, zero external assets |
| Secret-leak scan (tests) | No key/SSN/private-key shapes in any tracked file |
| License/README checks (tests) | Exact copyright line present in both; README credits the LLC |
| Git | `git init` + single plain commit; no push, no remote, no co-author trailer |

## Known gaps (honest)

- **Every number is education-grade.** Tax percentages, the safe-harbor ladder, and the pot rule are the standard round numbers people use — not a computation of this reader's tax. Each chapter hard-links the IRS/Indiana DOR/FinCEN source pages, and the disclaimers say "never legal, tax, or financial advice" on every page and in the build footer.
- **Indiana-specific figures verified at launch (Oct 2026):** BER fee $31 online / $50 mail, biennial cadence, 90-day pre-window, dissolution at 5 months overdue; state income tax 2.95% (2026) heading to 2.90% (2027); BOI exemption per the Aug 2026 FinCEN final rule. Fees and rates drift — the chapters point to the live sources rather than pinning numbers.
- **The sibling repos are linked by relative path** (`../cashflow-simple-ledger`, `../small-business-ai-playbook`), which only resolves when the repos sit side by side (as they do in this lab). Inside the built site, those become plain external-style links and are intentionally skipped by the link verifier.
- **Marketing/site** chapter deliberately absent — that ground belongs to *small-business-ai-playbook* (marketing calendar, reply templates); duplication was a design constraint, not an oversight.
- The first-person launch anecdotes (credit union morning, quoting evening) are written from experience but anonymized to a name-free level — no personal data anywhere in the repo.

## Deferred / follow-ups

- Optional combined single-page "print handbook" page (all chapters in one HTML for papercutting) — build.py makes it easy to add.
- Could pin a `pyproject.toml` + make target if the repo ever gains more tooling; not needed at this size.
