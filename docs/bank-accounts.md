# Bank accounts

Chapter one, and my genuine favorite: this is the chapter where the LLC stops being a heap of good intentions and becomes **a place where money lives.** One morning in early November 2026, six weeks after a state said I was a real company, this was me: EIN letter open on one screen, the credit union's business desk open on the other. Ninety minutes later, the LLC had its own home.

Here's everything I learned that morning, minus the part where my transit reader died on an expired debit card.

## Step zero: get the EIN first

An **EIN** (Employer Identification Number) is your LLC's social-security-number-without-the-medical-records-weirdness — a nine-digit federal ID that banks, the IRS, and basically everyone will use to identify the business.

The beautiful part: it's **free, from the IRS, in about fifteen minutes.**

1. Go to [IRS.gov — apply for an EIN](https://www.irs.gov/businesses/small-businesses-self-employed/get-an-employer-identification-number). It is an official IRS page; the interview is free and online and does **not** require you to be an *employer* — the "employers" in the name are a history lesson, not a requirement.
2. Answer the plain-English questions: sole member LLC, no employees yet, taxes filed under my own name. The questions sound scarier than the answers.
3. When finished, you get the **CP 575** letter — the confirmation PDF. **Download it immediately** (the session will not show it again) and put it in your LLC folder forever.

> **Beware the copycat sites.** Non-official "EIN filing services" charge $50-$300 for what the IRS gives away free. One rule, one time: only ever start from irs.gov.

If you ever need a second copy of the letter, the IRS will re-issue one by mail or fax (the SS-4 archives). But a five-second PDF backup now beats a letter-sized panic later. Keep it in a folder named exactly like the LLC, backed up in two places.

## The one rule of this whole chapter

Here is the rule, engraved in my head, on a sticky note, and in the constitution of this household:

> **Business money lives in business accounts. Personal money lives in personal accounts. Nothing crosses without a record saying why.**

Why do people hammer on this? Three pleasant reasons:

1. **It protects the LLC's actual point.** A single-member LLC's liability shield mostly matters because the company is recognizably *its own thing* — "a distinct entity" is the phrase lawyers use. If every dollar sloshes freely between your personal account and the LLC's, courts can (and do) treat the company and you as one blob, which quietly undoes everything the filing bought you. It's called *commingling*, and it's the first thing discussed in any LLC-meets-lawsuit story you've ever heard. Separate accounts are the cure, and they're free.
2. **It makes your ledger trivially honest.** A clean business account is a complete list of business money events, ready for any tool — our ledger eats it in one CSV. (See [cashflow-simple-ledger](../cashflow-simple-ledger).)
3. **Tax season becomes an afternoon**, not archaeology.

## Picking a bank, like choosing a gym

Almost any bank or credit union will take your business. What actually matters for a solo LLC in year one:

| Question to ask the bank | Why it matters |
|---|---|
| Is there a **monthly fee**, and can it be waived? | Many accounts waive fees with a minimum balance ($100-$500 is common) or with no conditions at all. |
| Does the account **earn a little interest**? | Whatever money sits in your tax pot (see below) should be quietly earning rent. |
| Is **online transfer** out to my personal account free? | You will pay yourself monthly. That transfer is the most-used button in the building. |
| Can I **export transactions as CSV**? | Lets the ledger import directly. My non-negotiable. |
| Do you offer **free sub-accounts or savings** for the business? | You'll want a second parking place for money already reserved for taxes. |
| Is there a **relationship banker I can actually name**? | When the day comes that the account does something weird, a named human beats a queue system by an hour, every time. |

Both local credit unions and big national banks worked fine for me — the credit union answered questions on day two and printed the confirmation letter same-day, and I genuinely like them. Split the decision however you like; no one audits a debit card choice.

## What to bring: the honest checklist

Banks differ — **call ahead and ask what they need** — but pack these and you'll almost always be complete:

- [ ] **EIN letter** (the CP 575 from the IRS)
- [ ] **Articles of Organization** (the state-approved PDF from Indiana's INBiz filing — filed for me here with [INBiz](https://inbiz.in.gov/))
- [ ] **Operating agreement** — even a one-pager. If you skipped one, write a simple single-member one before you go; it costs one evening and banks love it.
- [ ] **Your own government ID** (the member is the company, so *you* are the signatory)
- [ ] **Something physical with the LLC's name** — a card, a letter that came to your address care-of the LLC, or simply nothing: many banks don't need this. Ask.
- [ ] **Initial deposit money** (often $25-$100; your state's minimums are set by the bank, not the state)

That's the paperwork for a single-member LLC — no other humans, no DBA (unless you filed an assumed business name, in which case bring that form too), no registered agent paperwork (Indiana's list already knows who that is).

## The two-pot system

Here is the single best thing I set up that morning, and I would build it again if I launched a hundred LLCs:

- **Pot 1 — checking.** Everything flows in here, and ordinary costs flow back out. This is the LLC's everyday wallet.
- **Pot 2 — tax savings.** A separate savings sub-account with **no card, no check** access. Every pay-yourself period, a percentage of profit moves here, *labeled for taxes only*. It is not savings. It is not a piggy bank. It is the IRS's and Indiana DOR's money, parked. The [taxes chapter](taxes.md) says what percentage to move into it.

Money in pot 2 does one thing: it makes April a review, not a scramble. People who set up pot 2 sleep at night. People who don't, meet the phrase "where would I even get…" in month ten.

## The pay-yourself loop

This is the everyday rhythm, and it's beautifully boring:

1. **Money comes in** — a book sale, a tool purchase, royalties. It goes to pot 1, labeled in your ledger with what it was.
2. **Twice a month (my schedule; yours can run monthly), pay yourself:** move a fixed amount to your personal account, and move the tax percentage into pot 2 — the percentage lives in the [taxes chapter](taxes.md).
3. **Record the two transfers** in the ledger: one as a pay-yourself event (**not a business expense** — it's just money crossing desks inside your own universe), the other as a move into the tax pot, same category every time.
4. **Pay the LLC's real expenses** (software, printing, insurance) from pot 1 with a dedicated card, never your personal one, even when it's easier. When they *will* happen to you — everyone — the fix is one line: reimburse yourself from pot 1 and record it the same way.

Notice what's missing: **an S-corp election, payroll services, a bookkeeper on retainer.** A single-member LLC in year one needs two accounts and a rhythm. Ask about more elaborate structures when the numbers or your [professional's triggers](professionals.md) say so.

## The small, harmless wobbles you'll have (and their one-line fixes)

- *I used the wrong card at the espresso place.* Reimburse from pot 1, record it, move on. A rare mistake recorded is a bookkeeping footnote; a habit of it is a subject for the annual review.
- *A customer still pays me by Venmo under my personal name.* Set up the business profile (or ask them to switch to check/Zelle to the business account), and record each historical event honestly as you migrate.
- *I want to buy something purely personal with business money.* You always can — but it is a **draw** (pay-yourself event), not an expense. Wrong category, messy taxes. Keep the log honest, order the sandwich with your personal card.
- *What if the account balance dips?* Then pot 1 needs a bare float of a few hundred dollars. Operating float, not savings — the account's calcium level, not the nest egg.

## One quiet option, mentioned because it exists

Homeowners-insurance folks and policy nerds talk about **business-use riders** on personal cards and house policies here. It exists, and no: it is *not* the same as the separate-business-account discipline. It fills potholes; it doesn't build the road. The accounts matter more. (The [insurance chapter](insurance.md) handles the road properly.)

## Your next steps

- [ ] EIN applied for, **CP 575 downloaded** into the LLC folder (and a second backup)
- [ ] Two business accounts open: checking (pot 1) + tax savings (pot 2)
- [ ] Ledger set up with both accounts — see [cashflow-simple-ledger](../cashflow-simple-ledger) or the [record habits chapter](records.md)
- [ ] A recurring twice-monthly calendar nudge named "pay yourself + tax pot"
- [ ] Bookmark saved: [IRS EIN page](https://www.irs.gov/businesses/small-businesses-self-employed/get-an-employer-identification-number) and [INBiz](https://inbiz.in.gov/)

Printable version of all the setup steps: [the first-30-days checklist](first-30-days.md).

*Orientation only — never legal, tax, or financial advice. Bank products and fees vary; ask your bank, and read its actual fee schedule before signing anything.*
