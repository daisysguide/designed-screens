# Daisy's Guide v3 — Design Decisions Log

A complete record of the design decisions made while reviewing the v3 designed
screens. Use this as the source of truth when updating the spec docs and when
briefing Rocketech.

The decisions are grouped thematically rather than in the order they were made.
Many original questions expanded into multi-part calls — those are captured
together below.

---

## 1. Topic state model

**Final state taxonomy** for regular topics:

| State | When | Visual treatment |
|---|---|---|
| Not started | Neither has answered | Neutral dot, "Not started" pill |
| Your turn | Partner answered, you haven't | Purple dot, filled purple "Your turn" pill, topic name bold |
| Waiting | You answered, partner hasn't | Gray dot, "⏳ Waiting" neutral pill |
| Pending | Both answered + revealed, but user hasn't marked Resolved | (new pill — to spec visually) |
| Resolved | Both answered + revealed, user picked Resolved on Screen 20 | Green checkmark pill |

Plus one special state for Prediction Cards only:

| Locked | Prediction card before reveal date | 🔒 muted pill, non-interactive |

**Sort priority on Topic List:** Your turn → Not started → Waiting → Pending → Resolved → Locked.

**"Talk about it" + "Revisit later" merged into "Needs more work"** on Screen 20.
Single optional reminder toggle replaces the two separate options.

**Screen 20 (Post-Reveal Reflection) redesign:**
- Two reflection options (Resolved · Needs more work)
- Selection is **required** — primary CTA disabled until one is picked
- Primary CTA renamed to **"Submit →"**
- After Submit → navigate to **Home** (user picks next move from the "Up next" card)
- Old "Next topic →" and "Back to home" buttons go away

**"Conversation list" feature is cut** (was Decision 12). The Pending state on
Topic List + the new stacked bars on Progress cover this need without a separate
list surface.

---

## 2. No time-gating in V1 (except Prediction Cards)

Personalization in V1 = which topics are hidden/shown via Manage Topics. **No
temporal sequencing.**

This drops a large content-modeling investment (per-topic temporal triggers were
going to need definition for all 51 topics).

**V1 ships a single default sort order on Topic List.** The Guided timeline vs
Self-directed choice (formerly Q8 in onboarding) and the corresponding
sort-order toggle are **cut from V1**. Sort behavior is fixed in V1; revisit in
a future version if/when the guided-timeline content model is built.

**Prediction Cards stay in V1** as the only time-gated feature. Their reveal
date is auto-calculated as **due date + 3 months** (or birth date + 3 months for
"Baby is already here" users with babies under 3 months old).

**Prediction Cards eligibility:** show only to users with a future milestone
(reveal date > today). This naturally:
- Includes: Currently pregnant · Expecting again · Baby is here < 3 months old
- Excludes: Trying (or thinking about trying) · Baby is here > 3 months old

For excluded users, Prediction Cards just don't appear in their plan. No
"perpetually locked" weirdness. When a user updates Q1 (see Decision 11),
Prediction Cards naturally appear on the re-filter.

---

## 3. Dual view (Category · Stage) on Topic List AND Progress

Toggle in the header: `[ By category | By stage ]`. Default: By category
(mirrors the book's TOC).

Mirror the book's alt-TOC for the stage labels. Same toggle UX on Screen 13
(Topic List) and Screen 11 (Progress). Each screen remembers its own toggle
state independently — users think about navigation and progress differently.

**Milestone celebration trigger** (Screen 11): currently fires when a category
reaches 100%. After adding stages, also fire when a full stage reaches 100%.
Same animation, two triggers.

---

## 4. Progress screen detail

**Stacked per-category (and per-stage) bars** showing the state breakdown within
each group. Three segments visible per bar:

```
[████ resolved | ▓▓ pending | ░░ not started]
```

(In-progress = Your turn + Waiting could share the in-progress color, or split.
Probably collapse for visual clarity — four segments gets noisy at small sizes.)

**Top stats row stays simple:** Complete · Remaining · Aligned. The detailed
breakdown lives in the per-group bars below.

---

## 5. Screen 15 Topic Intro — 4 states

Aligned with the new state model:

| State | Partner status line | Primary CTA |
|---|---|---|
| Not started | "Jordan hasn't answered yet either." | "Start answering →" |
| Your turn | "Jordan finished — your turn." | "Start answering →" or "Continue answering →" |
| Waiting | "Waiting on Jordan to finish." | None (no primary action) + "Change my answers" affordance |
| Ready to reveal | "Jordan finished — ready to reveal." | "See your results →" |

**Edits allowed during Waiting until partner submits.** Add a quiet "Change my
answers" link on both Screen 18 (Waiting for Partner) and Screen 15 Waiting
state. Tapping routes through Screens 17 → 17b with previous answers pre-filled.

Screen 18 keeps "Your answers are locked in 🔒" as the headline but adds a
subtle line: *"Need to change something? You can edit until [partnerName]
finishes."*

**Mid-edit collision with partner's submit:** let the user finish their edit.
Partner's submit queues; reveal waits for the both-fresh-submitted state.

---

## 6. Re-answer flow

**Model: paired re-answer round** (V1 default).
- Initiator submits re-answer → topic enters "[name] re-answered, waiting for partner" state
- Partner gets notification; if they re-answer, both have new answers → new reveal plays (Screen 19 again)
- Original reveal remains canonical until partner joins
- Race condition (both initiate simultaneously): timestamp wins, second tap reinterpreted as joining

**Expiry: 14 days.** If partner doesn't re-answer within 14 days, the attempt
expires and topic returns to its prior Completed state.

**V1.1 planned upgrade:** offer the initiator a choice — *"update just your
answers"* (unilateral) vs *"start the discussion over"* (paired re-round).

---

## 7. Snapshot feature

**Cut the user-facing snapshot in V1.** When a couple re-answers, the new
answers become canonical. Screen 22's "Original answers" toggle is removed.
Screen 21's copy drops the *"your previous answers will be saved so you can see
how your thinking evolved"* line.

**Retain the data server-side** for future-proofing. Doesn't affect V1 spec but
keeps the option open for a later "view history" feature.

---

## 8. Note step (Screen 17 / 17b reconciliation)

Final spec — base is 17b, with several overrides from 17:

| Element | Spec |
|---|---|
| Heading | "Anything else [partnerName] should know?" (17b) |
| Sub-text | "[partnerName] sees this after you both complete this topic." (17) |
| Textarea bg | White (17) |
| Min-height | 120px, expanding to 240px (17b) |
| Placeholder | "Your thoughts, context, or questions for later…" (17) |
| Char limit | Hard 280, enforced with `maxlength` (17) |
| Counter | "N characters remaining", turns red below 50 left (17) |
| Submit label | "Submit →" (17) |

`[partnerName]` is templated — production swaps in the partner's actual name.

---

## 9. Paywall feature list (canonical, used everywhere)

- Your personalized topic plan
- Side-by-side answer reveal for every topic
- A couples summary for every topic, written for you two
- Expert-written guide for every topic
- Both partners, one purchase

Used on Screen 08 (Paywall) and Screen 26 (Payment Failure) — same list both
places. The "for you two" framing in bullet 3 echoes the AI summary card on
Screen 19, keeping language coherent.

---

## 10. Q1 journey-stage update in Settings

**V1: minimal flow.** Add an "I'm in a different stage now" row in
Settings → Pacing. Tapping opens a Q1 picker; choosing a new stage may collect a
follow-up date (due date for Pregnant/Expecting Again, birth date for Baby here).
Save → silently re-run topic filtering against the new stage. No diff screen.

**V1.1: full flow.** Same Q1 update, plus a brief "Rebuilding your plan…"
moment (reusing Screen 03's animation) and a results screen showing
added/removed topics before saving.

---

## 11. Unpaid returning user routing

Logged-in user without a completed purchase → routed to
**Personalized Results → Manage Topics → Paywall**.

Skip the "Building your plan" animation (Screen 03) since their plan already
exists — just open Screen 07. The re-engagement sequence rebuilds emotional
context before the paywall ask.

---

## 12. Empty state and edge case handling

**Chaos meter (Screen 11):** Hide until 3 reveals. The meter is a playful
easter egg; making it appear once earned preserves the surprise.

**Alignment % (Screens 10, 11):** Hide until 5 reveals. Small samples produce
noisy numbers that could mislead couples about their dynamic. Below 5 reveals,
the stat tile is suppressed (Home: single-tile, Progress: 2-column top stats).

**Empty Home partner variants (Screen 24):** Spec all three (Linked · Invite
pending · No partner) by mirroring Screen 10's variants.

**Empty Topic List chips (Screen 25):** Removed. Matches Screen 13's no-chips
approach. Filtering UI is unnecessary on top of category/stage grouping.

---

## 13. Slider initial state

**Ghosted thumb at midpoint as visual affordance.** Faded thumb at position 5,
value display hidden. On first interaction, thumb solidifies and value appears.

The ghosted state signals "this is interactive" while clearly communicating
"you haven't answered yet." Avoids anchoring at a meaningful default while
solving the discoverability problem.

---

## 14. Copy and visual consistency

**Bottom nav Topics icon:** 📚 (books) everywhere. Replaces the 📋 clipboard on
Screen 10. When real icons replace placeholders, use `ti-book` or `ti-book-2`.

**Partner status copy:** Just "Linked ✓" everywhere with the avatar and name.
No timestamps ("Active 2h ago" cut), no conditional action language.

**Spelling:** American English. Global find-replace of "personalised" →
"personalized."

**Nudge frequency options:** Daily · A few times a week · Weekly · Don't nudge
me. Same set in Quiz Q7 and Settings.

**Topic time estimate:**
- Empty Home: *"about 5–10 minutes"* (range — honest about variability)
- Topic Intro stats card: dynamic per-topic. Each topic carries its own
  `articleReadMinutes` and `quizMinutes` fields. Read time can auto-derive
  from article word count (200 wpm standard).

**Sample data persona:** User = **Alex** (gender-neutral). Partner stays
Jordan. Both gender-neutral. Update Screen 24's "Taylor" to "Alex"; standardize
"Sarah" across other screens to "Alex."

**Sample phone area code:** 972 (Dallas).

---

## 15. App Store compliance

**7-day refund promise stays.** Implementation via App Store Connect refund API
(iOS 15+) + a support process that handles refund requests when users email
guarantee@daisysguide.com. Flag for Rocketech: backend integration with the
App Store refund API is required.

**Screen 26 payment retry CTAs simplified.** Drop "Try a different payment
method" (doesn't work cleanly on iOS). Replace with just **"Try again"** as
primary, plus the existing restore-purchase link and contact-support link.

---

## 16. Log out

**Single tap, no confirm.** The asymmetry with Delete account (which has a
bottom-sheet confirmation) is intentional and fine — log out is fully
recoverable, delete account is not.

---

## Implementation flags for Rocketech

A few decisions imply schema or integration work worth surfacing explicitly:

- **Topic schema additions:** `stage` field (for dual-view grouping),
  `articleReadMinutes`, `quizMinutes`, `type` (`regular` | `prediction`),
  `revealOffsetMonths` (for prediction cards).
- **Topic state machine:** five states for regular topics, plus Locked for
  prediction cards.
- **Pending → Resolved transition:** users can switch a topic's reflection
  status at any time from Screen 22.
- **Q1 update flow (V1):** schema needs to support re-running topic filtering;
  user profile mutation triggers re-filter.
- **Re-answer flow:** new "re-answer pending" state with 14-day expiry timer.
  Snapshot of old answers retained server-side (no UI).
- **Edit-while-waiting:** existing question flow supports pre-filled state on
  return; no new screens, but routing logic needs to be additive.
- **App Store Connect refund API integration** + support inbox process for
  refund requests.
- **Chaos meter and alignment % visibility gating:** count revealed topics,
  threshold logic (3 for chaos, 5 for alignment).
- **Prediction card eligibility filter:** only include in plan when
  `revealDate > today`.

---

## What's next

1. Update each affected screen file in `designed-screens/v3/` to reflect these
   decisions. (Many screens need copy and behavior updates.)
2. Re-run the Claude Code / Cursor fix prompt for the definitive bugs (still
   valid — none of those were affected by these decisions).
3. Hand the updated v3 spec + this decisions log + the schema implications to
   Rocketech for the build.
