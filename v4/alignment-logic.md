# Daisy's Guide — Topic Alignment Logic

*How the per-topic quiz works, how each question type produces an alignment score, and how those roll up to a topic result. Reference for content, design, and engineering. Current as of the screen-design pass — this supersedes the earlier draft.*

*This doc is the **spec**. For the **process** of authoring and reviewing a book's quiz (template schema, question-type choices, the round-based review workflow, and the engineering gotchas), see `daisys-guide-quiz-authoring-playbook.md`.*

---

## The guiding principle

The app helps two partners understand where they **align with each other** — it never tells them there's a right or wrong answer. Nothing should read as *"great, you got it right"* or *"oops, try again."* A disagreement isn't a failure; it's the conversation the product exists to surface.

## How a topic works

Each topic has 3–5 questions. One is the **spine** — the single most decision-relevant question, weighted heaviest and led with on the reveal. Both partners answer independently; when the second submits, the topic resolves to one of three states plus a written "For You Two" summary. An optional **free-text note** lets each partner add context for the other — it is never scored; it's fuel for the conversation.

## Two kinds of question: alignment vs information-sharing

Every question is one of two kinds, and the kind decides how a *difference* between partners is treated.

- **Alignment questions** ask *what should we do* — a joint decision (where to give birth, how to handle sleep, who's in the delivery room). This is the default. They're scored for agreement, feed the weighted average, and can carry the **weakest-link veto** — a single big gap can pull the whole topic down a band.
- **Information-sharing questions** ask *what's true of you* — a disclosure, not a decision (how much leave you'd take, how much personal time you need, how you'd want to be supported in a hard moment). A difference here is something each partner should *learn*, not resolve, so it must never read as disagreement.

In the data this is a single tag: **`self_report = yes`** marks an information-sharing question; blank means an alignment question. Information-sharing questions behave two ways:

- **Scored disclosure** — still feeds the weighted average (a wide gap nudges the band) but is **excluded from the weakest-link veto**, and the "For You Two" narration frames it as *"you each want something different, and now you know,"* never as a conflict.
- **Pure disclosure (weight 0)** — shown and narrated, never scored. Used where the raw answer is non-diagnostic of agreement — e.g. the t44 "how much like the way you were raised" opener, where two different childhoods make the raw gap meaningless.

An information-sharing question can be the **spine** (the leave, personal-time, and depletion spines are). When it is, the spine gives up the veto and a separate **alignment question** in the topic — usually the joint-coordination one ("how will we make sure we each get it") — carries it, so every topic still anchors on something the couple actually decides together.

## The question types and how each scores 0–1

There are **four scored input types** — slider, single-select, multi-select, and ranking — plus the optional free-text note, which isn't scored. Single-select carries **two scoring rules** (ordered and unordered), so there are **five scoring rules** in total, one per bullet below.

- **Slider** — a spectrum with two labeled ends. The range is **per-question** (e.g. 1–5 or 0–10); the score normalizes by whatever the range is, so any range works. Score = how close the two values are, with a **tolerance band set proportional to the range** so a small gap still counts as fully aligned. (At a very short range a slider is effectively a discrete scale — that's fine, just be deliberate about slider vs. ordered single-select, and remember the tolerance has to scale with the range or "fully aligned" gets too loose.)
- **Single-select, ordered** — pick one from a sequence (timeframes, amounts, places on a spectrum). Score = how close the two chosen positions are.
- **Single-select, unordered** — pick one from discrete options with no inherent order. Score = match (1) or no-match (0), with optional **partial-credit** pairs for options that are partly aligned.
- **Multi-select** — pick any that apply. Score = **weighted overlap** (shared picks ÷ total distinct picks). Individual items can be weighted so a contentious one counts more toward the score.
- **Ranking** — order a short list by priority. Score = **rank-similarity** (normalized Spearman footrule): how far apart the two orderings are overall, with **every position weighted equally by distance moved** — it's position-agnostic. So an item one partner ranks first and the other ranks last is penalized heavily (large distance), while any small reordering, top *or* bottom, counts as minor. Identical orderings score 1.0; reversed score 0.0. We chose this plain measure over a **top-weighted** one deliberately: for these topics, two partners who broadly agree on what matters — give or take some ordering — should read as aligned, and we don't want to over-penalize a near-miss at the very top. (If we ever decide the #1 slot must dominate regardless of distance, that's a position-weighted variant — a real change to the formula, not the current behavior.)

## Four cross-cutting rules

- **Deferrals.** Some answers mean "we haven't actually decided" — *Decide later, Unsure, Haven't thought about it.* These are tagged so the question always lands in **Worth a conversation**, even if both partners pick the same one. Agreeing to defer isn't alignment.
- **Perspectival ("who") questions** use absolute references — *Partner A / Partner B*, with the app substituting real names — never "me / you." Otherwise two identical "me" answers would look aligned when they're really both claiming the same role, which is a conflict.
- **Information-sharing vs alignment.** See *Two kinds of question* above. The mechanical effect on scoring: information-sharing (`self_report`) questions are **excluded from the weakest-link veto**, and some are **weight 0** (shown and narrated, never scored). Everything else is an alignment question and scores normally, veto included.

- **Presentation order.** For **ranking** and **unordered single-select / multi-select**, show the options in randomized order so there's no implied "right" answer to anchor on. **Ordered single-selects and sliders keep their fixed order/direction** — there the sequence *is* the signal, so it must not be shuffled.

## From questions to a topic state

Each question's 0–1 score rolls up to a **weighted topic average**, with the spine weighted heaviest, mapped to one of three states: **Fully aligned / Mostly aligned / Worth a conversation.** Thresholds are tunable, not fixed in stone.

One override — the **weakest-link rule** — applies to every type, ranking included: a **single large disagreement can pull the whole topic down a level** even when the average is high. We never let averaging hide a real gap — that gap is the point.

## The "For You Two" summary

After both partners submit, we generate one short, brand-voice paragraph describing where they line up and where they differ — leading with the biggest gap, framed warmly, never judgmentally.

- **Code decides the alignment; the model only writes the words.** Scores and states are computed by the logic above. The model is handed that result plus both partners' answers and asked only to narrate it, so the badge and the paragraph can never disagree.
- **Generated once, then cached;** regenerated if a partner re-answers; never pre-written (the combinations are effectively infinite); with a templated fallback if generation fails.
- **Ranking is the hardest type to narrate** ("you both put kindness first but split on independence"), so the summary prompt needs extra care on the ranking topic (currently one).

## Who owns what

- **Content** — writes the questions, options, spine flags, item weights (`{w:N}`), and deferral tags (`{defer}`) in the template.
- **Engineering** — implements the five scoring rules, the deferral and weakest-link logic, partner-name substitution for perspectival questions, and the cached summary generation.
- **Design / brand** — the reveal language, the three-state framing, and the voice of the summary prompt.

---

## Appendix — worked examples & engine constants (revised 2026-07-21, from the reference implementation)

*This appendix pins the spec above to the exact algorithm, a single table of constants, and worked numeric cases that double as the scoring engine's (backend#413) table-driven test vectors. It is derived from the **reference implementation** — the embedded JS in `daisys-guide-alignment-preview-full.html` (`scoreSlider` / `scoreOrdered` / `scoreUnordered` / `scoreMulti` / `scoreRanking` / the rollup + weakest-link) — reconciled against this spec and the live Notion content (367 questions across 94 topics, pulled 2026-07-21). It supersedes the earlier "proposed constants" draft, which guessed several values wrong. Constants are **engine config** (Supabase/code), tunable, deliberately not stored in Notion; the preview exposes the thresholds and the weakest-link toggle as live controls.*

### The engine, exactly (from the reference impl)

```
band(s):      s ≥ 0.80 → Fully;  s ≥ 0.50 → Mostly;  else Worth       (levels: Worth=0, Mostly=1, Fully=2)

slider:       d = |a − b|;  if d ≤ tol → 1;  else 1 − (d − tol)/(range − tol)   (tol is per-question, raw units; range = max − min)
ordered SS:   1 − |i − j| / (n − 1)                                   (NO tolerance)
unordered SS: a == b → 1;  declared partial-credit pair → its score;  else → 0
multi:        Σ w(shared picks) / Σ w(union of picks)                 (per-item weight, default 1)
ranking:      1 − Σ|posA − posB| / floor(n² / 2)                      (identical → 1.0, reversed → 0.0)
deferral:     single-select only — if either pick is a deferral option, s = min(s, 0.25)

rollup:       avg = Σ(sᵢ · weightᵢ) / Σ(weightᵢ)                       (weight-0 questions contribute nothing → excluded from the average)
weakest-link: worst = min band-level over the veto-eligible questions;
              if band(avg) − worst ≥ 2  →  lower the topic one band
```

Because band-levels are only {0, 1, 2}, `band(avg) − worst ≥ 2` can hold in exactly one situation: **the average is Fully (2) and some veto-eligible question is Worth (0)**. So the weakest-link only ever demotes **Fully → Mostly** — it never turns Mostly into Worth. "A single Worth-band question" means a question scoring **below 0.50** (the Mostly threshold), deferrals (capped at 0.25) included.

### Constants (engine config — tunable, not in Notion)

| Constant | Value | Notes |
| --- | --- | --- |
| Fully threshold | **≥ 0.80** | Preview default; live-adjustable 0.50–0.95. |
| Mostly threshold | **≥ 0.50** | Preview default; live-adjustable 0.20–0.79. |
| Deferral cap | **0.25** | `s = min(s, 0.25)` when a deferral option is picked (single-select). Lands the question in Worth. |
| Weakest-link | **band-distance ≥ 2 → drop one band** | Toggleable; net effect Fully→Mostly only. |
| Weights | **spine 2 · standard 1 · pure-disclosure 0** | From the Notion `Weight` column. In the live content: `{1: 270, 2: 94, 0: 3}`, and `is_spine` ⟺ `weight = 2` exactly. |

Values **read from Notion content**, not config: per-question `Tolerance` (raw units — currently always `1`, i.e. 0.10 of range on the 0–10 sliders and 0.167 on the 1–7 sliders), `is_spine`, `Weight`, `self_report`, `Question Type`, `Is Ordered`, options + `Item Weight` (default 1; a few 2/3), per-pair partial scores (live values in use: `0.5` ×69, `0.3` ×9, `0.0` ×1), and deferral tags (rare — 1 option across 1,019).

### The `self_report` veto — NOT implemented by the reference preview

The preview's rollup computes `worst` over **every** question, so it does **not** model the information-sharing rule from §"Two kinds of question." The production engine (backend#413) must, and this spec is authoritative where they disagree:

- A `self_report` question is **excluded from the `worst` scan** (the weakest-link veto). It still feeds the weighted average (unless it is weight-0, in which case it is excluded from the average too).
- When the **spine is `self_report`**, the spine gives up the veto and a designated **alignment** question in that topic carries it — so `worst` is taken over the topic's alignment questions.
- Consequence to expect while testing against the preview: on the **20 `self_report` questions** — including the 3 `self_report` spines `t47-q2`, `t49-q1`, `t51-q1` — the preview's bands read conservative and will not match production. That is the known gap, not a bug in either.

### Worked examples — per-type unit scores (test vectors)

| Type | Inputs | Computation | `s` |
| --- | --- | --- | --- |
| Slider (0–10, tol 1) | a=5, b=5 | d=0 ≤ tol | **1.000** |
| Slider (0–10, tol 1) | a=5, b=6 | d=1 ≤ tol | **1.000** |
| Slider (0–10, tol 1) | a=5, b=7 | 1 − (2−1)/(10−1) | **0.889** |
| Slider (0–10, tol 1) | a=2, b=8 | 1 − (6−1)/9 | **0.444** |
| Slider (0–10, tol 1) | a=0, b=10 | 1 − (10−1)/9 | **0.000** |
| Slider (1–7, tol 1) | a=1, b=4 | 1 − (3−1)/(6−1) | **0.600** |
| Slider (1–7, tol 1) | a=1, b=7 | 1 − (6−1)/5 | **0.000** |
| Ordered SS (n=4) | i=2, j=2 | 1 − 0/3 | **1.000** |
| Ordered SS (n=4) | i=2, j=1 | 1 − 1/3 | **0.667** |
| Ordered SS (n=4) | i=3, j=0 | 1 − 3/3 | **0.000** |
| Unordered SS | Hospital / Hospital | exact match | **1.000** |
| Unordered SS | Hospital / Birth center (pair 0.5) | partial-credit pair | **0.500** |
| Unordered SS | pair scored 0.3 | partial-credit pair | **0.300** |
| Unordered SS | Hospital / Home (no pair) | no match | **0.000** |
| Unordered SS | either pick = "Decide later" | min(s, 0.25) | **0.250** |
| Multi | {x,y} / {x,y} | 2/2 | **1.000** |
| Multi | {x,y} / {x} | union 2, shared 1 | **0.500** |
| Multi | {x,y} / {x,z} | union 3, shared 1 | **0.333** |
| Multi (y has `{w:3}`) | {x,y} / {x} | shared w 1 / union w 4 | **0.250** |
| Ranking (n=4) | [0,1,2,3] / [0,1,2,3] | d=0 | **1.000** |
| Ranking (n=4) | [0,1,2,3] / [1,0,2,3] | 1 − 2/8 | **0.750** |
| Ranking (n=4) | [0,1,2,3] / [3,2,1,0] | 1 − 8/8 | **0.000** |

### Worked examples — topic rollup

Each row: per-question `(s, weight)` → weighted average `A` → band-by-average → weakest-link? → **final computed band**.

1. **Identical → Fully.** spine slider (5,5)=`(1.0, 2)`; std unordered match=`(1.0, 1)`; std multi identical=`(1.0, 1)`. `A = 4/4 = 1.000` → Fully. `worst = Fully(2)`; `2 − 2 = 0` → no drop. **Fully aligned.**
2. **Reversed spine ranking → Worth.** spine ranking reversed=`(0.0, 2)`; std slider (5,5)=`(1.0, 1)`. `A = (0 + 1)/3 = 0.333` → Worth. (Already Worth; band-distance moot.) **Worth a conversation.**
3. **Partial-credit → Mostly.** spine unordered, pair scored 0.5=`(0.5, 2)`; std slider (4,4)=`(1.0, 1)`; std ordered (2,2)=`(1.0, 1)`. `A = (1.0 + 1.0 + 1.0)/4 = 0.750` → Mostly. `worst = Mostly(1)` (the 0.5); `1 − 1 = 0` → no drop. **Mostly aligned.**
4. **Deferral → demotes Fully to Mostly.** spine slider (5,5)=`(1.0, 2)`; std slider (5,6)=`(1.0, 1)`; std single-select where a partner picked *Decide later* → capped=`(0.25, 1)`. `A = (2.0 + 1.0 + 0.25)/4 = 0.8125` → Fully by average, **but** the deferred question is Worth(0), so `2 − 0 = 2` → drop one band → **Mostly aligned.** (The deferred question itself bands Worth.)
5. **One big gap → demotes Fully to Mostly (weakest-link).** spine slider (5,5)=`(1.0, 2)`; three standards all `(1.0, 1)`; one standard slider (1–7 scale, 1 vs 7)=`(0.0, 1)`. `A = (2.0 + 3.0 + 0.0)/6 = 0.833` → Fully by average, **but** `worst = Worth(0)`, `2 − 0 = 2` → **Mostly aligned.**
6. **`self_report` excluded from the veto → stays Fully.** spine slider (5,5)=`(1.0, 2)`; three std `(1.0, 1)`; one **`self_report`** slider with a wide gap=`(0.0, 1)`. `A = (2.0 + 3.0 + 0.0)/6 = 0.833` → Fully. `worst` is taken over veto-eligible questions **only**, so the `self_report` 0.0 is skipped → `worst = Fully(2)`, `2 − 2 = 0` → **Fully aligned.** (Were it counted — as the preview wrongly does — `worst` would be 0 and the topic would drop to Mostly. This is the difference the veto-exclusion makes.)
7. **`self_report` spine → veto handed off.** spine is `self_report`, well-aligned=`(1.0, 2)` (excluded from the veto); the designated **alignment** coordination question=`(0.0, 1)`; three std alignment questions `(1.0, 1)`. `A = (2.0 + 0.0 + 3.0)/6 = 0.833` → Fully. The self_report spine is skipped in `worst`, but the alignment carrier is Worth(0) → `worst = 0`, `2 − 0 = 2` → **Mostly aligned.** The veto still fires — carried by the alignment question, not the spine.

### What is locked vs. config vs. content

- **Locked** (shape): the five rule formulas, the weighted-average rollup, the weakest-link **band-distance** override, the `self_report` exclusion + spine-veto handoff, the deferral cap, and the three-state output.
- **Config** (this appendix's numbers, in `_shared/alignment.ts`, tunable without a migration): the `0.80` / `0.50` thresholds, `DEFER_SCORE = 0.25`, and the weakest-link `≥ 2` / one-band rule.
- **Content** (authored in Notion, authoritative): per-question `Tolerance`, `is_spine`, `Weight`, `self_report`, type, ordering, options, per-pair partial scores, item weights, deferral tags.
- **No mockup impact:** engineering math, no `v4/*.html` mockup renders these numbers.
