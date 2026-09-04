# Daisy's Guide — Plan Reveal: What to Surface (by quiz answer)

> **Purpose:** the answer → topic map for the post-quiz Plan Reveal card. Given the
> initiator's quiz answers, this says exactly which topics appear in each of the card's two
> sections, plus the fill and fallback logic and worked examples. Screen anatomy/copy/states
> live in the mock; this doc is the **content selection logic.**
>
> Companion to `topic-filtering-and-sort-logic.md`, which produces the **active plan** this
> card draws from. Both sections draw only from that active plan — **a pre-excluded topic
> never appears here.**

---

## The card, briefly

Two sections, **~4 topics total**:

- **A · "Starting with what you told us"** (purple dots) — reflects the initiator's Q7 worries.
- **B · "…and a few couples don't see coming"** (gray dots) — curated high-stakes topics they
  didn't flag.

Footer: "Plus **{active plan total − shown}** more."

---

## Section A — driven by Q7 ("What are you nervous about?")

Surface the **primary topic of each worry the initiator named**, in the order below, up to 2.

| Q7 worry | Primary topic surfaced | Backups (if primary is pre-excluded or already shown) |
|---|---|---|
| Who will handle what | How will we share parental and household duties? | How much parental leave will we take? · How will we plan for recovery after birth? |
| How we'll get enough sleep | How will we help the baby sleep? | Where will the baby sleep? · How will we handle postpartum depression and the harder parts of new parenthood? |
| Deciding the "right way" to parent | What aspects of our upbringing will we replicate and what will we avoid? | What are the values we want to pass on? · How will we share our culture and/or religion with our child? |
| Making time for ourselves | How will we make time for ourselves as a couple? | How will we make time for ourselves as individuals? |
| All of the above | — (no single worry → Fallback) | — |

> **These titles are matched literally against published content.** The implementation looks
> each one up in a dictionary keyed on the topic's published `question_name`, so a title that
> differs by a single character selects nothing and the worry silently falls through to its
> backup — or, for a curated entry, is skipped. Three titles in this doc drifted exactly that
> way and shipped broken (daisysguide/ios#865): a comma, a straight apostrophe, and an em dash.
> When a topic is renamed in Notion, this doc and `PersonalizedResultsView` both have to move
> with it. Two entries below still name no published topic at all and are pinned as known
> failures in `PublishedContentTests`.

Rules:
- **One topic per named worry** (variety), max 2. Two worries → 2 topics; one worry → 1.
- Order = the Q7 option order above (tunable).
- If a worry's primary topic is pre-excluded or already shown, drop to its first eligible
  backup.
- "All of the above" or skip → no Section A → **Fallback.**

---

## Section B — curated "don't see coming" pool

Walk this ranked pool and surface the first entries that are **(a)** in the active plan,
**(b)** not already in Section A — until the card reaches 4 total. Prefer entries relevant to
the user's current stage.

Ranked pool (content owns the final order):

1. Who will be in the delivery room?
2. What aspects of our upbringing will we replicate and what will we avoid?
3. Who will be the legal guardian if something happens to us?
4. How will we handle postpartum depression and the harder parts of new parenthood?
5. Should we make a will before the baby is born?
6. How will we respond if there’s birth trauma?
7. How will we approach spending time with extended family?
8. Do we want health screenings, even if they reveal something hard?
9. What are the values we want to pass on?
10. Do we have life insurance, and is it enough?

These are the heavy / non-obvious ones. Obvious topics — names, nursery, gear — deliberately
stay **out** of this section; they aren't "surprising."

---

## Fill logic

Target **4 topics total.**
- Fill Section A first (≤ 2, from worries).
- Section B fills the remainder up to 4.
- So: 2 worries → **2 + 2** · 1 worry → **1 + 3** · 0 worries → **0 + 4** (Fallback).

---

## Fallback (no Q7 signal)

Q7 skipped, or "All of the above" only. Drop Section A and its label; show **4 topics from the
Section B pool** under the "…don't see coming" framing alone. Headline / subhead / footer
unchanged.

---

## Worked examples

**1 · The screenshot user** — Q7 = *who-handles-what* + *making-time*; pre-birth, 45-topic plan
- **A:** How will we share parental and household duties? · How will we make time for
  ourselves as a couple?
- **B:** Who will be in the delivery room? · What aspects of our upbringing will we replicate
  and what will we avoid?
- **Footer:** "Plus 41 more."

**2 · One worry** — Q7 = *enough-sleep* only
- **A:** How will we help the baby sleep?
- **B:** Who will be in the delivery room? · Upbringing topic · Legal guardian
- **Footer:** plan − 4.

**3 · Fallback** — Q7 skipped
- **A:** —
- **B:** Delivery room · Upbringing · Legal guardian · Postpartum/PPD
- **Footer:** plan − 4.

**4 · Baby-here** — Q7 = *who-handles-what*; birth cluster pre-excluded
- **A:** How will we share parental and household duties?
- **B:** Upbringing · Legal guardian · Postpartum/PPD  *(delivery room skipped — pre-excluded)*
- **Footer:** plan − 4.

---

## Flags

### Resolved

- **Counts** — locked to **51 library / 45 plan / 6 hidden** across Reveal (08), Topics (14), and Manage Topics (15); the footer "Plus 41 more" reconciles (45 − 4). 51 and the 45/6 split are both verifiable against published content: exactly six topics carry a `stage` of `second` or `third`, and 51 − 6 = 45.
- **Topic titles** — every topic title in this doc and in the Screen 08 / 14 / 15 mocks is now byte-identical to the published `questions.question_name` in production. Until 2026-09-04 they were not. Six were mis-transcribed — a serial comma added to the upbringing title, a straightened apostrophe in the birth-trauma title, a comma written as a dash in the prenatal-screening title, an inserted article in each of the two name titles and in the milestones title, and a truncated babysitters title — and four named topics that do not exist in the library at all. Two of the four were copied into the app's `PersonalizedResultsView`, where a title-keyed lookup matched nothing and the affected cards silently fell through to filler.

  The two that were identified and corrected sat in the ordered "Us" group at exactly the positions of orders 46 and 49, which is what identifies them: "What is our postpartum plan?" stood in for `postpartum-recovery` and "How will we handle lack of sleep, hormones, and/or postpartum depression?" for `postpartum-mental-health`. Both real topics were absent from every mock.

### Open

Recorded rather than fixed, because each needs a decision rather than a transcription.

- **Section A's worry → topic mapping and Section B's ranked order have no recorded owner.** "Content owns the final order" is asserted here with nothing corroborating it. Before building on this mapping, confirm it reflects a decision someone made.
- **Three titles in Screen 15's hidden lists have no published counterpart** and are left in place: "Will the baby attend a religious school?", "How will we approach religious holidays as a family?", and "How will we co-parent across two households?". Unlike the two above there is no positional evidence identifying what they were meant to be.
- **`topic-filtering-and-sort-logic.md` does not exist.** The header defers the plan-construction rules to it, and the pre-exclusion rule two of the worked examples turn on is exactly what it was deferring to.
- **The fallback label contradicts the mock.** This doc says the fallback reuses the "…don't see coming" framing; `08-personalized-results.html` and the shipped app both use a third label, "A few you'll want to sit down for".
- **Worked examples 1 and 2 surface a pre-excluded topic.** Under the only reading of "45 plan / 6 hidden" the data supports, example 1 surfaces `sharing-duties` (`stage = second`) and example 2 surfaces `sleep-help` (`stage = third`), both of which that plan would hide — against this doc's own opening rule.
- **The stage-preference rule in Section B cannot run.** Eight of its nine published entries have no `stage` value; 41 of the 51 library topics have none.
- **"nursery" is not a topic.** The contrast used to justify the pool — "names, nursery, gear" — names one item that has never been in the library.
