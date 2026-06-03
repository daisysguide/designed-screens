# Daisy's Guide — Topic Alignment Logic

*How the per-topic quiz works, how each question type produces an alignment score, and how those roll up to a topic result. Reference for content, design, and engineering. Current as of the screen-design pass — this supersedes the earlier draft.*

---

## The guiding principle

The app helps two partners understand where they **align with each other** — it never tells them there's a right or wrong answer. Nothing should read as *"great, you got it right"* or *"oops, try again."* A disagreement isn't a failure; it's the conversation the product exists to surface.

## How a topic works

Each topic has 3–5 questions. One is the **spine** — the single most decision-relevant question, weighted heaviest and led with on the reveal. Both partners answer independently; when the second submits, the topic resolves to one of three states plus a written "For You Two" summary. An optional **free-text note** lets each partner add context for the other — it is never scored; it's fuel for the conversation.

## The question types and how each scores 0–1

There are **four scored input types** — slider, single-select, multi-select, and ranking — plus the optional free-text note, which isn't scored. Single-select carries **two scoring rules** (ordered and unordered), so there are **five scoring rules** in total, one per bullet below.

- **Slider** — a spectrum with two labeled ends. The range is **per-question** (e.g. 1–5 or 0–10); the score normalizes by whatever the range is, so any range works. Score = how close the two values are, with a **tolerance band set proportional to the range** so a small gap still counts as fully aligned. (At a very short range a slider is effectively a discrete scale — that's fine, just be deliberate about slider vs. ordered single-select, and remember the tolerance has to scale with the range or "fully aligned" gets too loose.)
- **Single-select, ordered** — pick one from a sequence (timeframes, amounts, places on a spectrum). Score = how close the two chosen positions are.
- **Single-select, unordered** — pick one from discrete options with no inherent order. Score = match (1) or no-match (0), with optional **partial-credit** pairs for options that are partly aligned.
- **Multi-select** — pick any that apply. Score = **weighted overlap** (shared picks ÷ total distinct picks). Individual items can be weighted so a contentious one counts more toward the score.
- **Ranking** — order a short list by priority. Score = **rank-similarity** (normalized Spearman footrule): how far apart the two orderings are overall, with **every position weighted equally by distance moved** — it's position-agnostic. So an item one partner ranks first and the other ranks last is penalized heavily (large distance), while any small reordering, top *or* bottom, counts as minor. Identical orderings score 1.0; reversed score 0.0. We chose this plain measure over a **top-weighted** one deliberately: for these topics, two partners who broadly agree on what matters — give or take some ordering — should read as aligned, and we don't want to over-penalize a near-miss at the very top. (If we ever decide the #1 slot must dominate regardless of distance, that's a position-weighted variant — a real change to the formula, not the current behavior.)

## Three cross-cutting rules

- **Deferrals.** Some answers mean "we haven't actually decided" — *Decide later, Unsure, Haven't thought about it.* These are tagged so the question always lands in **Worth a conversation**, even if both partners pick the same one. Agreeing to defer isn't alignment.
- **Perspectival ("who") questions** use absolute references — *Partner A / Partner B*, with the app substituting real names — never "me / you." Otherwise two identical "me" answers would look aligned when they're really both claiming the same role, which is a conflict.
- **Presentation order.** For **ranking** and **unordered single-select / multi-select**, show the options in randomized order so there's no implied "right" answer to anchor on. **Ordered single-selects and sliders keep their fixed order/direction** — there the sequence *is* the signal, so it must not be shuffled.

## From questions to a topic state

Each question's 0–1 score rolls up to a **weighted topic average**, with the spine weighted heaviest, mapped to one of three states: **Fully aligned / Mostly aligned / Worth a conversation.** Thresholds are tunable, not fixed in stone.

One override — the **weakest-link rule** — applies to every type, ranking included: a **single large disagreement can pull the whole topic down a level** even when the average is high. We never let averaging hide a real gap — that gap is the point.

## Computed alignment vs current standing (the editable status)
The rollup above produces the computed alignment — the honest read of the two answer sets. That's the default, but the status is editable, and the edited value is what the rest of the app shows.

- One status per topic, shared. Either partner can change it, **unilaterally and instantly, in both directions** — there is no propose-and-confirm handshake.
- **Reopen** any topic and it returns to **Worth a conversation** — the one-tap consent valve: if either person still wants to talk, it's worth a conversation. **Settle** restores the topic's **computed** value, with one exception: a topic whose computed value was Worth a conversation settles to **Mostly aligned** (a genuinely-divergent topic that's been talked through — it can't settle back to Worth, and it can never reach Fully, which is computed-only). So a Fully-computed topic that's reopened and then settled returns to Fully, not Mostly.
- **Provenance is preserved** — the computed value, who changed it, and when. Returning a topic to its computed value clears the override.
- **Downstream uses the current value.** The Progress distribution and the Topics states reflect this **current standing** (computed alignment as adjusted), not the raw answer-alignment. The "For You Two" summary still describes the answers; the badge is the couple's current call on them.

We deliberately do **not** carry a second resolved/unresolved axis. Resolution is merged into this single status — a settled topic reads "Mostly aligned," an open one "Worth a conversation." A separate to-do axis fought the anti-checklist ethos and doubled the display.

## The "For You Two" summary

After both partners submit, we generate one short, brand-voice paragraph describing where they line up and where they differ — leading with the biggest gap, framed warmly, never judgmentally.

- **Code decides the alignment; the model only writes the words.** Scores and states are computed by the logic above. The model is handed that result plus both partners' answers and asked only to narrate it, so the badge and the paragraph can never disagree.
- **Generated once, then cached;** regenerated if a partner re-answers; never pre-written (the combinations are effectively infinite); with a templated fallback if generation fails.
- **Ranking is the hardest type to narrate** ("you both put kindness first but split on independence"), so the summary prompt needs extra care on the ranking topics (currently two).

## Who owns what

- **Content** — writes the questions, options, spine flags, item weights (`{w:N}`), and deferral tags (`{defer}`) in the template.
- **Engineering** — implements the five scoring rules, the deferral and weakest-link logic, partner-name substitution for perspectival questions, and the cached summary generation.
- **Design / brand** — the reveal language, the three-state framing, and the voice of the summary prompt.
