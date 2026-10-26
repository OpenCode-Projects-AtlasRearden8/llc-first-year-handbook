# Simple record habits

The tax professional version of this chapter is called "bookkeeping" and costs money. The version I live is called **"the ten-minute week"** and costs a paperclip's worth of attention. This chapter is that version — the habits that keep your money story true day by day, so that taxes, loans, and "wait, which app did I actually renew?" always have an answer sitting in a file.

The *tool* here is deliberately small. For recording the flow itself, my recommendation — the one this whole handbook was written to complement — is **[cashflow-simple-ledger](../cashflow-simple-ledger)**, our tiny local-first CLI that keeps books in one portable CSV you own forever. No cloud, no subscription, no "the company holding my books went out of business." Every habit below works with a spreadsheet or a notebook too. The tool is replaceable. The habits are not.

## The one-ledger rule

One business, one ledger, one place every dollar is written down. Not two apps and a shoebox and a memory of "I think that was March." The moment a transaction has a second "official" home, accuracy dies in committee.

What belongs in the ledger:

- **Everything through the business accounts** — income, expenses, transfers between pots, pay-yourself moves
- **Everything that should have been through the business account** — like that espresso you caught with your personal card (record it as a reimbursement; fixes itself in one line)
- **Nothing personal.** Your groceries, your rent, your FFXIV subscription: invisible to the LLC. If you buy something you use both for work and life... that's where professional advice is worth it later; for now, note it and ask (see [when to call a pro](professionals.md)).

## The ten-minute week

Same time every week — my slot is **Friday 9:00 a.m. with coffee**, yours is whenever energy exists. The slot goes on the calendar permanently. It's short enough that "no motivation today" cannot hold it hostage.

1. **Open the bank and card accounts** (2 min). Anything new since last week?
2. **Enter or import anything missing** (3-4 min). With the `cashflow` CLI, imports are dedupe-aware — re-downloading the same CSV twice adds nothing twice. My category rules file fills most names in automatically.
3. **Photos of receipts shot this week** (1 min). Drop into this quarter's folder, matching the entry date. Done.
4. **One glance at the category totals** (2 min). Anything surprise? Anything trending up fast? (Skip the deep analysis; the [money dates](money-dates.md) handle judgment.)
5. **Close the laptop** (0 min, but do it). Not tax time. Not strategy time. Just clean.

That's it. Ten minutes. The entire "bookkeeping" racket of dread is just ten minutes times fifty-two weeks, never skipped, never crammed.

## The four-folder year

Receipts and papers live in a folder structure any human can navigate blind:

```text
ASDALE-DYNAMICS-LLC/
  2026-Q4/receipts/     ← phone photos, named 2026-11-05-printer-ink
  2026-Q4/statements/   ← downloads of monthly statements
  2026-Q4/invoices/     ← what clients were sent
  2027.../
  legal/                ← Articles, EIN letter, insurance policies, agent letters
  taxes/                ← what you'll hand a professional, when that day comes
```

- **Phone-photo every receipt** the moment it exists. Paper is a liability equal to its chance of being crumpled in a coat pocket forever. Paper-based receipts fade (thermal ones fade in a drawer within a couple of years) — photo at purchase time.
- **Quarter folders get closed** at the year-end [money date](money-dates.md) with a glance. Four times a year you spend one minute opening the right new folder. That's the whole filing system.
- **Keep at least three years** before deleting anything — tax records are commonly recommended to be kept three to six years, and longer for some situations; keeping more storage than that costs basically nothing, so the modern move is: keep everything, delete nothing, storage is cheap.

## The starter categories

Categories are the vocabulary of your year. Twelve is the sweet spot: enough to see trends, few enough that sorting stays instinctive. My working set (adjust to your life — the ledger doesn't care what they're called; only regular use matters):

| Category | What lands here |
|---|---|
| `Book Income` | KDP royalties, direct sales, guides |
| `Tool Income` | App/template sales, licenses, tips |
| `Software` | Editor licenses, hosting, AI tools, cloud |
| `Printing/Postage` | Proof copies, ISBN costs, shipping |
| `Ads` | Anything that buys attention |
| `Education` | Books, courses, classes that make the LLC better |
| `Professional Fees` | CPA, lawyer, agent services — future you |
| `Insurance` | The policies from the [insurance chapter](insurance.md) |
| `Fees` | Bank fees, payment processor cuts |
| `Mileage` | Business miles — logged in the log below |
| `Tax Pot` | The transfers that set money aside for [estimates](taxes.md) |
| `Transfers` | Money moving between *my own* accounts — never a taxed event, sorted by this category in every report |

Two guardrails, learned the boring way:

- The same purchase, same category, every time. Consistency beats perfection. If printer ink sometimes is `Software`, tax export day becomes a puzzle.
- `Uncategorized` is a **to-do pile, not a sin**. Leave it, fix the weekly ritual, and the pile never grows past a receipt or two.

## The mileage log (the tiny one)

Business driving is the record everyone means to keep and nobody does, because most tutorials suggest sub-hundred-row spreadsheets dated with the sun's position. The fix is smallness:

- One line the **moment you park**: `date · from → to · why · miles`
- Note it in your phone's notes or the ledger note field — either lives fine
- Tally once per quarter at the [money date](money-dates.md), not at tax time
- The [IRS mileage-rate page](https://www.irs.gov/tax-professionals/standard-mileage-rates) keeps the current per-mile number; that page is the round number you use, and the IRS document is the source, always

What counts as a business mile is one of those "clear in spirit, detailed in law" things — the text of the rules lives with the IRS and any professional (see [professionals](professionals.md)). The habit, though — write it down — is 100% yours and 100% free.

## Paying yourself, on record

One difference that trips one-person LLCs: **paying yourself is not an expense.**

When a single-member LLC pays you, the default tax treatment is "you and the LLC are the same taxpayer." The company didn't buy anything from you; money just crossed between your own pockets. So in the ledger it gets its own category (`Owner Draw` or use `Transfers` with the note "pay yourself") — and never lands in an expense category, because expenses lower profit and draws don't. That single distinction is most of the accounting learning you need in year one.

Two more, while we're being plain:

- **Single-member LLC by default is a "disregarded entity"** — legal speak for "the IRS sees straight through the wrapper, right onto your 1040 Schedule C." Very convenient. Very real. (If you later elect something else, that's a [pro conversation](professionals.md).)
- **Profit is income minus expenses — not income minus everything you moved out.** The two-pot system and this chapter exist so that sentence never surprises you.

## The backup, and then the end

- The ledger CSV lives in the `ASDALE-DYNAMICS-LLC` folder, synced/backed up in at least two places (my copy: laptop + a USB stick rotated monthly + git). Losing a whole year of books to a broken laptop is the only accounting disaster one person can actually have.
- Any paper you must keep (the EIN letter original, insurance certificates) lives in `legal/`, scanned into the same folder tree. The scanned copy is the working copy; the paper is the relic.

Then it's Friday again, ten minutes again, and your year quietly has receipts.

## Your next steps

- [ ] Ten-minute week on the calendar, forever
- [ ] Folder tree created; phone can photo straight into it (or into an app that syncs)
- [ ] Starter categories chosen and named once, permanently
- [ ] Mileage log format chosen (notes app is fine), tally date pinned to the [money dates](money-dates.md)
- [ ] Ledger test-driven with one income entry and one expense — see [cashflow-simple-ledger](../cashflow-simple-ledger)

*Orientation only — never legal, tax, or financial advice. Which records the law requires you to keep, and exactly how long, is a question for the IRS documents and a professional when it matters.*
