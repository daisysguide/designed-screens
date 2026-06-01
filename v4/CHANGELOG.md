# v4 changelog

v4 implements the design decisions surfaced during the v3 review. v3 remains
in the repo as the reviewed baseline (no further changes will be made to it).

## Summary of v3 → v4 changes

- **Topic state model:** five states for regular topics (Not started · Your turn · Waiting · Pending · Resolved) plus Locked for prediction cards. Replaces the previous four-state model.
- **Screen 21 redesign:** two reflection options (Resolved · Needs more work), selection required, single "Submit →" CTA. "Talk about it" and "Revisit later" merged into "Needs more work."
- **Snapshot UI cut:** "Original answers" toggle removed from Screen 23. Data retained server-side but not surfaced.
- **Dual view toggle (Category / Stage):** added to Screen 14 (Topic List) and Screen 12 (Progress).
- **Progress screen overhaul:** stacked per-group bars; chaos meter hidden until 3 reveals; alignment % hidden until 5 reveals.
- **Settings additions:** Q1 journey-stage update row in Pacing section.
- **Edit-while-waiting:** "Change my answers" affordance on Screens 19 and 16 Waiting state.
- **Re-answer flow mechanics:** paired round with 14-day expiry; V1.1 will add a unilateral-vs-paired choice.
- **Prediction Cards eligibility:** only shown to users with a future milestone date.
- **No time-gating in V1** except Prediction Cards.
- **Paywall feature list unified** between Screens 09 and 27.
- **Unpaid returning user routing:** Personalized Results → Manage Topics → Paywall.
- **Topic time estimate:** Empty Home shows range ("5–10 minutes"); Topic Intro stats become dynamic per-topic.
- **Visual consistency:** Topics icon 📚 everywhere; partner status "Linked ✓"; American spelling; sample user "Alex"; area code 972.
- **Slider initial state:** ghosted thumb at midpoint instead of fully hidden.

## What's deferred to v1.1 (intentionally out of scope in v4)

- Re-answer flow choice: "update just your answers" vs "start the discussion over"
- Full Q1 update UX with "Rebuilding your plan…" animation and diff screen

## Dated changes

### 2026-05-31

- **Screen 12 (Progress) — full redesign ported in.** Phone mockup rebuilt from `12-progress-redesign.html`; spec panel rewritten against `screen-12-progress-spec.md`. Out: 3-column "74% Aligned" stats slab, "We're good / Needs work / In progress" stacked per-category bar, chaos meter, header-mounted grouping toggle. In: completion lede + 10px bar; alignment distribution card (state-aware note, 14px bar, hybrid "Worth a conversation" row with revisit list); inline grouping toggle as the section header for breakdown (52px tap-target rows, 8px bar, navigate to that group's accordion on Topics); badges with dashed teaser; in-between and empty states. Progress ends after badges — easter egg moves to Home (Screen 11). Doc-page state switcher added above the phone for reviewers (Populated · Balanced · Mostly settled · Orange-heavy · All orange · All aligned · In-between · Nothing answered). Page-desc reworded. The scoping bug (Screen 12 living under `body.page-22`) is left in place per CLAUDE.md repo-hygiene note — the new Progress styles overwrite the existing `body.page-22 .screen-root` block; the eventual `page-22 → page-12` rename will happen in the dedicated page-NN sweep that also fixes Screen 14 (`page-12 → page-14`).

### 2026-05-28

- **Screen 08 (Personalized Results) — Conversation Preview labels unified:** all section labels now share a single style (small uppercase `purple-500`), identical across the personalized and fallback states. The "from your answers" vs "curated" distinction is carried by dot color + wording, never by label color.
- **Screen 08 — scope line reworded:** "Plus N more, across all 7 areas of parenting prep." → "Plus N more, with expert guidance for everything ahead."
