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
| Who will handle what | How will we share parental and household duties? | How much parental leave will we take? · What is our postpartum plan? |
| How we'll get enough sleep | How will we help the baby sleep? | Where will the baby sleep? · How will we handle lack of sleep, hormones, and/or postpartum depression? |
| Deciding the "right way" to parent | What aspects of our upbringing will we replicate, and what will we avoid? | What are the values we want to pass on? · How will we share our culture and/or religion with our child? |
| Making time for ourselves | How will we make time for ourselves as a couple? | How will we make time for ourselves as individuals? |
| All of the above | — (no single worry → Fallback) | — |

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
2. What aspects of our upbringing will we replicate, and what will we avoid?
3. Who will be the legal guardian if something happens to us?
4. How will we handle lack of sleep, hormones, and/or postpartum depression?
5. Should we make a will before the baby is born?
6. How will we respond if there's birth trauma?
7. How will we approach spending time with extended family?
8. Do we want health screenings — even if they reveal something hard?
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
- **B:** Who will be in the delivery room? · What aspects of our upbringing will we replicate,
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

## Flags (carried, still open)

- **Counts don't reconcile across screens** — Reveal implies 45 (4 + 41); the Customize mock
  implies 44 (and sums to 50, short of the 51 library). Lock one plan-total source.
- **Upbringing title** appears in a third phrasing on the live mock ("What will we keep from
  how we were raised…"); standardize to canonical or bless it as a reveal-only display
  variant. This doc uses the canonical title.
