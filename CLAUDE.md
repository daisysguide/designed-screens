# CLAUDE.md

## How to work in this repo

After completing any task that modifies files:
1. Run any verification steps included in the task description.
2. Stage and commit with a descriptive multi-line message.
3. Report commit hash + verification results.

Prefer editing existing files over creating new ones. If a task seems to
require a new file, double-check whether an existing file should be edited
instead and flag the decision before proceeding.

Screen mockups live in versioned directories at the repo root: `v1/`,
`v2/`, `v3/` (all frozen) and `v4/` (active). Each screen is a single
HTML file. The root also contains the original v1 set of screen files;
treat those as frozen too — all new work happens in `v4/`.

`dg-v3-decisions-log.md` (root) is the authoritative source for design
rationale; its v3 name is kept as a historical record and it continues
to apply through v4. `v4/CHANGELOG.md` is a quick-reference summary of
changes — consult the decisions log when you need the "why" behind a
decision.

For `v4/` work:
- Never create new screen files unless I explicitly ask. If a task
  seems to require one, ask first.
- When updating a spec on a screen, also update the visual mockup at the
  top of that screen to match. Spec tables and mockups drift apart easily.
- After completing changes, run grep verification for any "old copy"
  strings that should no longer appear, and report results.