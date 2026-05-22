# v4 changelog

v4 implements the design decisions surfaced during the v3 review. v3 remains
in the repo as the reviewed baseline (no further changes will be made to it).

## Summary of v3 → v4 changes

- **Topic state model:** five states for regular topics (Not started · Your turn · Waiting · Pending · Resolved) plus Locked for prediction cards. Replaces the previous four-state model.
- **Screen 20 redesign:** two reflection options (Resolved · Needs more work), selection required, single "Submit →" CTA. "Talk about it" and "Revisit later" merged into "Needs more work."
- **Snapshot UI cut:** "Original answers" toggle removed from Screen 22. Data retained server-side but not surfaced.
- **Dual view toggle (Category / Stage):** added to Screen 13 (Topic List) and Screen 11 (Progress).
- **Progress screen overhaul:** stacked per-group bars; chaos meter hidden until 3 reveals; alignment % hidden until 5 reveals.
- **Settings additions:** Q1 journey-stage update row in Pacing section.
- **Edit-while-waiting:** "Change my answers" affordance on Screens 18 and 15 Waiting state.
- **Re-answer flow mechanics:** paired round with 14-day expiry; V1.1 will add a unilateral-vs-paired choice.
- **Prediction Cards eligibility:** only shown to users with a future milestone date.
- **No time-gating in V1** except Prediction Cards.
- **Paywall feature list unified** between Screens 08 and 26.
- **Unpaid returning user routing:** Personalized Results → Manage Topics → Paywall.
- **Topic time estimate:** Empty Home shows range ("5–10 minutes"); Topic Intro stats become dynamic per-topic.
- **Visual consistency:** Topics icon 📚 everywhere; partner status "Linked ✓"; American spelling; sample user "Alex"; area code 972.
- **Slider initial state:** ghosted thumb at midpoint instead of fully hidden.

## What's deferred to v1.1 (intentionally out of scope in v4)

- Re-answer flow choice: "update just your answers" vs "start the discussion over"
- Full Q1 update UX with "Rebuilding your plan…" animation and diff screen
