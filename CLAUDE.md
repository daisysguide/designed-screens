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
HTML file — all new work happens in `v4/`.

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

### Scope for per-screen reviews

When applying changes from a per-screen review prompt (e.g., a prompt
generated from reviewing a single screen in Claude chat), scope edits to
that screen's HTML file only. Don't make changes to:
- CSS class names or selectors
- `styles.css` or the design system
- `nav.js`, `index.html`, or other shared files
- Body classes on other screen files

These are repo-wide concerns that a single-screen review can't see the
implications of. If a per-screen prompt asks you to make a cross-screen
change, flag it and ask before proceeding. Cross-screen concerns get
their own dedicated tasks.

## Repo hygiene TODOs

- The v4 body classes (`.page-NN`) don't match screen numbers —
  historical drift (e.g., Screen 03 = `.page-07`, Screen 04 = `.page-01`,
  Screen 06 = `.page-03`). Worth a dedicated sweep to align body classes
  with screen numbers across all v4 files. Do not absorb into other
  tasks — needs its own pass since renames have cross-file CSS
  implications.