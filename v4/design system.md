# Daisy's Guide — Design System

*Living document. No version number. Date-stamped decisions live in the CHANGELOG section at the bottom of this file.*

---

## How to use this document

The design system is the source of truth for visual and interaction decisions. Screen files in `/v4/` reference components and tokens defined here. If a screen file specifies a value that differs from this document, the screen file is wrong by default.

**Conventions:**

- Components and screens are referenced by **slug**, not by number. The Topic Intro screen is `topic-intro`, not "Screen 16." Numbers exist in filenames for sort order only — they may change. Slugs don't.
- Tokens use a **two-layer system**: primitives (`purple-500: #5f45f2`) and semantic aliases (`action-primary: purple-500`). Components reference semantic tokens.
- Spec changes go in the CHANGELOG at the bottom of this file, with a date and a one-line summary.
- Decisions get dated entries in the CHANGELOG section at the bottom of this file.

---

## Resolved decisions

All structural decisions for the v2.0 rewrite have been resolved. Date-stamped in the CHANGELOG. Summary:

| # | Decision | Outcome |
|---|---|---|
| 1 | Slider scale | 1–10 with per-question end labels |
| 2 | AI Summary card name | Renamed to "For you two" |
| 3 | Topic Card vs Topic Row | Coexist (Card = Home spotlight, Row = list) |
| 4 | Stats Display | Merged Stats Row + Stats Card into one component with `columns` and `surface` props |
| 5 | Ghost button | Added as 4th non-destructive variant |
| 6 | Dashed border | Means "supplemental or authored content distinct from main flow" (not AI-specific) |
| 7 | Topic lifecycle states | 6 states; UI labels are "Needs work" and "We're good" (data model still says pending/resolved) |
| 8 | "Needs work" color | Blue family — `blue-text-dark: #1a5170` on `status-pending-surface: rgba(159,236,250,0.40)` |
| 9 | Canonical green | `#157a46`; retire `#1c7d3e` and `#1a4d35` |
| 10 | Letter-spacing | `em` throughout |
| 11 | Price | $49 |
| 12 | Daisy Mark | Scale of sm (24px) / md (48px) / lg (80px) |

---

## Foundations

### Colors

A two-layer system. Primitives are the palette — raw hex values. Semantic tokens are meaning-based aliases that components reference. This separation lets primitive values change without touching component specs.

#### Primitive tokens — brand

| Token | Value |
|---|---|
| `purple-500` | `#5f45f2` |
| `purple-600` | `#4f37d4` |
| `purple-700` | `#3f2bb3` |
| `cream-50` | `#fbefe1` |
| `black-900` | `#1a1a1a` |
| `white` | `#ffffff` |

#### Primitive tokens — accents (soft)

| Token | Value |
|---|---|
| `orange-200` | `#ffc48c` |
| `yellow-200` | `#ffe375` |
| `green-200` | `#96f1c6` |
| `blue-200` | `#9decfa` |
| `pink-200` | `#ffadad` |

#### Primitive tokens — accents (bold)

| Token | Value |
|---|---|
| `orange-400` | `#ffad6c` |
| `yellow-400` | `#ffd755` |
| `green-400` | `#77eaaf` |
| `blue-400` | `#7fe3f7` |
| `pink-400` | `#ff9191` |

#### Primitive tokens — dark text on accent

These are the hard-coded contrast-safe darks paired with each accent's soft fill.

| Token | Value | Pairs with |
|---|---|---|
| `green-text-dark` | `#157a46` | green-400 soft fills |
| `yellow-text-dark` | `#8a6800` | yellow-400 soft fills |
| `orange-text-dark` | `#9a5500` | orange-400 soft fills |
| `pink-text-dark` | `#c0392b` | pink-400 soft fills (and as standalone error text) |
| `blue-text-dark` | `#1a5170` | blue-200 / blue-400 soft fills (Needs work state) |

#### Semantic tokens — surfaces

| Token | Value | Usage |
|---|---|---|
| `surface-page` | `cream-50` | Default page background |
| `surface-card` | `white` | Cards and content containers sitting above the page |
| `surface-nested` | `cream-50` | Elements nested inside cards (answer option backgrounds, sub-sections, note textarea bg) |
| `surface-inverse` | `black-900` | Dark sections, inverse moments |
| `surface-brand` | `purple-500` | Purple-filled sections (onboarding nudge card, primary CTAs) |
| `surface-overlay` | `rgba(26,26,26,0.50)` | Modal backdrop |

#### Semantic tokens — text

| Token | Value | Usage |
|---|---|---|
| `text-primary` | `black-900` | Body copy, headings, all default text |
| `text-secondary` | `black-900 @ 60% opacity` | Supporting text, captions, labels |
| `text-tertiary` | `black-900 @ 40% opacity` | Placeholder text, de-emphasized metadata |
| `text-on-brand` | `cream-50` | Text on purple-filled surfaces |
| `text-link` | `purple-500` | Interactive inline links |

#### Semantic tokens — actions & status

| Token | Value | Usage |
|---|---|---|
| `action-primary` | `purple-500` | Primary button fill, active states, progress fill |
| `action-primary-hover` | `purple-600` | Hover state |
| `action-primary-pressed` | `purple-700` | Pressed state |
| `border-default` | `rgba(26,26,26,0.15)` | Default borders on cards, inputs, dividers |
| `border-strong` | `rgba(26,26,26,0.30)` | Heavier borders — secondary button outlines, dashed treatments |
| `border-focus` | `purple-500` | Input focused border |
| `border-error` | `pink-400` | Input error border |
| `status-error-text` | `pink-text-dark` (`#c0392b`) | Error text/icons — WCAG AA compliant (5.7:1 on white) |
| `status-error-surface` | `rgba(255,145,145,0.12)` | Error background tint — inputs, banners |
| `status-warning` | `orange-400` | Warning states |
| `status-highlight` | `yellow-400` | Yellow reserved for highlight only |
| `status-success-surface` | `green-400` (`#77eaaf`) | Completion fill — progress bars, left borders, checkmarks |
| `status-success-text` | `green-text-dark` (`#157a46`) | Text/icons on or near green surfaces |
| `status-pending-surface` | `rgba(159,236,250,0.40)` | "Needs work" state fill — Topic Row, Progress Row segment, status pill bg |
| `status-pending-text` | `blue-text-dark` (`#1a5170`) | "Needs work" text/icons — WCAG AA on the surface above |

**Naming note:** the token names use `pending` (the data-model lifecycle state). The user-facing label is "Needs work." Don't change the token name when displaying the label — they're two different layers.

#### Retired tokens — DO NOT USE

| Retired token | Replace with |
|---|---|
| `status-error` (bare) | `status-error-text` (for text/icons) or `status-error-surface` (for backgrounds) or `border-error` (for borders) |
| `status-success` (bare) | `status-success-surface` (for fills/borders) or `status-success-text` (for text on green) |
| Raw `#c0392b` | `status-error-text` |
| Raw `#157a46` | `status-success-text` |
| `#1c7d3e` (used briefly on Progress, Settings toast) | `status-success-text` — retire this variant |
| `#1a4d35` (DS v1.0 toast color) | Retire — use `status-success-text` |

**Accessibility rule (load-bearing — has been violated before):** White text on `pink-400` (`#ff9191`) is approximately 1.75:1 contrast and fails WCAG AA. Never use this combination. The Destructive button uses `status-error-text` (dark) as its label on a `pink-400` fill. Any screen specifying white-on-pink-400 is wrong.

### Typography

Two typefaces. Grandstander for display and brand moments. DM Sans for everything else. One font for personality, one for legibility — never cross the streams.

#### Type scale

| Token | Font | Size | Weight | Letter-spacing | Line-height | Example |
|---|---|---|---|---|---|---|
| `display-lg` | Grandstander | 32px | bold | -0.02em | 38px | Sleep philosophy |
| `display-md` | Grandstander | 24px | bold | -0.02em | 30px | How do you feel about this? |
| `display-sm` | Grandstander | 20px | bold | -0.02em | 26px | Question card text, modal titles |
| `heading-lg` | DM Sans | 24px | bold | 0 | 30px | Your progress |
| `heading-md` | DM Sans | 18px | bold | 0 | 24px | Notifications |
| `body-lg` | DM Sans | 17px | regular | 0 | 26px | Long-form intro copy |
| `body-md` | DM Sans | 15px | regular | 0 | 22px | Default body |
| `body-sm` | DM Sans | 14px | regular | 0 | 21px | Reveal answer text, secondary descriptions |
| `body-xs` | DM Sans | 13px | regular | 0 | 19px | Helper text, metadata, list row values |
| `label-lg` | DM Sans | 15px | medium | 0 | 20px | Continue |
| `label-md` | DM Sans | 13px | medium | 0 | 18px | Skip this question |
| `label-sm` | DM Sans | 11px | medium | +0.05em (uppercase) | 16px | SLEEP · TOPIC 1 OF 3 |

#### What changed from v1.0

- Added `display-sm` (20px Grandstander). Used on Question Card, Modal titles, and several callout headings. Previously these were specified ad hoc as "Grandstander 20px" in screen files.
- Added `body-sm` (14px) and `body-xs` (13px). Previously these sizes were used everywhere but not in the scale, leading to drift.

#### Off-scale values currently in screens — to be retired

These appear in v4 screen files but are not in the type scale. Each one should map to the nearest scale value:

| Off-scale | Where seen | Replace with |
|---|---|---|
| Grandstander 28px (auth headings) | Sign Up, Log In, OTP | `display-md` (24px) |
| Grandstander 26px (Name Entry, Partner Linking, Paywall) | 06, 10, 09 | `display-md` (24px) |
| Grandstander 22px (Topic Intro title, Home greeting, Topic List title, Chaos Meter score) | Multiple | `display-md` (24px) or `display-sm` (20px) — pick one per screen role |
| Grandstander 18px (Empty state headings, Prediction locked state) | Multiple | `display-sm` (20px) |
| Grandstander 17px (Onboarding nudge card) | Empty Home | `display-sm` (20px) |
| Grandstander 14px (numbered step bullets) | Re-answer Flow | DM Sans `heading-md` or accept as deliberate-display-treatment exception |
| DM Sans 14px outside `body-sm`/`label-md` | Many | `body-sm` (14px regular) or `label-md` (13px medium) |
| DM Sans 13px outside `body-xs`/`label-md` | Many | `body-xs` or `label-md` |

#### Rules

- Grandstander is used exclusively for display sizes, screen titles, and brand moments. Never for body copy, labels, or button text.
- ALL CAPS is reserved exclusively for `label-sm`. Never for headings, body, or display sizes.
- Letter-spacing convention: **em throughout**. Convert any `+0.5px` etc. in screen files to em equivalents.
- Grandstander letter-spacing: `-0.02em`. DM Sans: `0` (default). `label-sm` uppercase: `+0.05em`.

### Spacing

A 4px base unit. All spacing — padding, margin, gap — uses a token from this scale. If something needs 14px, the answer is either 12 or 16. Pick the one that fits the rhythm.

| Token | Value | Usage |
|---|---|---|
| `space-1` | 4px | Tight inline gaps, icon-to-text |
| `space-2` | 8px | Small component padding, dense gaps |
| `space-3` | 12px | Default tight spacing |
| `space-4` | 16px | Default component padding, screen horizontal margin |
| `space-5` | 20px | Comfortable component padding |
| `space-6` | 24px | Default section spacing within cards |
| `space-8` | 32px | Between major sections |
| `space-10` | 40px | Generous section spacing |
| `space-12` | 48px | Between major page regions |
| `space-16` | 64px | Hero spacing (rare) |

### Border radius

The brand leans soft. Default to `radius-xl` (16px) for cards, with nested elements stepping down to `radius-lg` (12px). Pills (`radius-full`) for primary CTAs.

| Token | Value | Common usage |
|---|---|---|
| `radius-none` | 0 | Full-width dividers, very rare |
| `radius-sm` | 4px | Small badges, URL inset background |
| `radius-md` | 8px | Inputs, secondary elements |
| `radius-lg` | 12px | Nested elements inside cards (answer options, sub-cards) |
| `radius-xl` | 16px | **Default for cards and primary buttons** |
| `radius-2xl` | 24px | Hero cards, modal sheets (top corners) |
| `radius-full` | 9999px | Pills, circular buttons, avatars |

### Shadows

Mobile shadows are subtle by design. Heavy shadows feel dated and clunky on small screens. Shadows use `black-900` at low opacity (not pure black) to stay warm and consistent with the brand.

| Token | Value | Usage |
|---|---|---|
| `shadow-sm` | `0 1px 2px rgba(26,26,26,0.05)` | Inputs, subtle separation |
| `shadow-md` | `0 2px 8px rgba(26,26,26,0.06), 0 1px 2px rgba(26,26,26,0.04)` | Default card elevation |
| `shadow-lg` | `0 8px 24px rgba(26,26,26,0.10), 0 2px 4px rgba(26,26,26,0.06)` | Modals, bottom sheets, floating elements, sticky CTAs |

### Opacity & z-index

| Opacity token | Value | Usage |
|---|---|---|
| `opacity-disabled` | 40% | Disabled state for all interactive components |
| `opacity-locked` | 55% | Locked topic state |
| `opacity-overlay` | 50% | Modal backdrop, image overlays |
| `opacity-ghost` | 60% | Secondary icons, de-emphasized decorative elements |

| Z-index token | Value | Usage |
|---|---|---|
| `z-base` | 0 | Normal document flow |
| `z-raised` | 10 | Cards that float above page content |
| `z-sticky` | 200 | Bottom nav, sticky headers, sticky CTA regions |
| `z-overlay` | 400 | Modal backdrops |
| `z-modal` | 500 | Modals, bottom sheets, drawers |
| `z-toast` | 600 | Toasts and snackbars (above everything) |

---

## Navigation patterns

How navigation works at the app level. Individual screen specs reference these rules.

### Bottom nav visibility

The app has a persistent bottom nav with four destinations: **Home**, **Topics**, **Progress**, **Settings**. Shown on the four "home base" screens; hidden during focused flows.

**Bottom nav shown:** `home`, `topic-list`, `progress`, `settings`, `empty-home`, `empty-topic-list`, `connection-error` (variant B inline banner only)

**Bottom nav hidden:** everything else — all of `swipeable-intro`, `onboarding-quiz`, `building-your-plan`, all auth screens, all onboarding pre-purchase screens, `partner-linking`, all topic-flow screens, `prediction-card`, `payment-failure`, `connection-error` (variant A full-screen)

### Screen header rules

Every flow screen has a 56px screen header containing: back button (left-aligned, 44×44px tap target, chevron icon) and optional screen title or right action. Headers sit flush on the page surface — no shadow or border by default.

**On scroll:** Header gains a 1px solid `border-default` bottom border when content scrolls beneath it. No shadow.

### Back navigation

Back button navigates to the previous screen in the flow. Device-level back gesture (Android back, iOS swipe-from-left) follows the same path. No screen requires a "confirm exit" dialog in V1.

**Exceptions where back is hidden:** `swipeable-intro`, `sign-up`, `log-in`, `name-entry` (no back affordance — Apple back gesture only), `building-your-plan`, `alignment-reveal`, `post-reveal-reflection`, `home` (and all home base), `connection-error` (variant A).

### Modal navigation

Modals and bottom sheets are dismissed by: tap-outside (modals only), explicit close/Cancel button, or device-level back gesture. Modals never trigger navigation away from the underlying screen on dismiss.

### Mid-topic app resume

When a user closes the app mid-session and returns later, the app resumes based on where they left off:

- **Mid-question:** Resumes to the last visited question with progress intact. Previously selected (but not submitted) answer re-selected on mount. No toast — silent resume.
- **Mid-note step:** Resumes to the note step with any in-progress text preserved.
- **Mid-waiting-for-partner:** Returns to Waiting screen. If partner finished in the interim, auto-advance to Alignment Reveal.
- **Mid-onboarding (pre-paywall):** Resumes at the last completed onboarding step. Most common abandon point is post-quiz, pre-paywall.
- **Mid-name-entry:** Resumes with any typed name preserved in the input.
- **All other screens:** Resume to Home.

### Lapsed user re-entry

**Definition:** User hasn't opened the app in 14+ days.

**Treatment:** Direct-to-Home with a soft re-engagement card. Copy references the partner by name and most recent in-progress topic: *"It's been a while. Jordan's still waiting on a couple things."* If no in-progress topics: *"It's been a while. Ready to pick up where you left off?"* CTA: "Jump back in →" routes to most recently visited topic intro, or Topic List if no topic in progress. Dismissible via × icon; dismissed state persists for the session.

---

## Universal components

### Button

Buttons trigger actions. Every interactive element that isn't a link, a card, or a form input is a button.

#### Variants

| Variant | Use for | Visual treatment |
|---|---|---|
| **Primary** | The single most important action on a screen | Filled `action-primary`, `text-on-brand` label |
| **Secondary** | Lower-priority actions alongside a primary | Transparent, `border-strong` outline, `text-primary` label |
| **Tertiary** | Inline actions, small navigation moments | No background, no border, `text-link` label |
| **Ghost** | Skip / dismiss / "maybe later" affordances at the bottom of focused screens | No background, no border, `text-tertiary` label |
| **Destructive** | Irreversible or harmful actions | Filled `pink-400`, `status-error-text` label (dark on pink — white doesn't have enough contrast) |

Ghost is added in v2.0 because screen files have been inventing it inconsistently. The distinction from Tertiary is intent: Tertiary signals an inline link-like action (text-link purple); Ghost signals "you can pass on this" (text-tertiary gray, lower visual weight than even Tertiary).

#### Sizes

| Size | Height | H. padding | Label style |
|---|---|---|---|
| **Large** | 56px | `space-6` | `label-lg` |
| **Medium** | 44px | `space-5` | `label-md` |
| **Small** | 32px | `space-4` | `label-md` |

**Touch target rule:** 44px minimum for reliable tappability. Small (32px) only for tertiary or low-mistake-cost contexts.

**52px is not a button size.** It currently appears on Social Auth, Poke, and Send via Text/Email. Each should be either 56 (treat as primary action) or 44 (treat as secondary). Pick one per use.

#### Primary button states

| State | Treatment |
|---|---|
| Default | `action-primary` fill |
| Hover | `action-primary-hover` |
| Pressed | `action-primary-pressed` |
| Disabled | `opacity-disabled` (40%), `pointer-events: none` |
| Loading | Spinner replaces label, button stays at full opacity |

#### Don't

- Don't use more than one primary button per screen (rare exceptions: equal-weight alternative actions, e.g. Topic Intro's two CTAs).
- Don't use Grandstander for button labels.
- Don't remove the pill shape (`radius-full`). It's a brand-level decision.
- Don't use a Destructive button without a paired Cancel/Ghost action.
- **Don't use white text on `pink-400`.** Destructive label is `status-error-text` (dark), not white. (This rule was violated in v1.0 by the Account Deletion bottom sheet and has been the source of a real WCAG bug.)

### Text Input

Captures free-form single-line text. Email, password (where used), name, phone.

#### Anatomy

| Element | Required? | Spec |
|---|---|---|
| Label | Required | 13px DM Sans semibold (`text-primary`). NOT uppercase. 6px gap below to field. |
| Input field | Required | See below. |
| Helper text | Optional | 12px DM Sans regular (`text-secondary`). Gives context. |
| Error message | Conditional | Same size/placement as helper text, `status-error-text` color. Replaces helper text when active. |

#### Visual specification

| Property | Value |
|---|---|
| Background | `surface-card` (white) — always white, regardless of page context |
| Border — default | `1.5px solid border-default` |
| Border — focused | `1.5px solid border-focus` + `0 0 0 3px rgba(95,69,242,0.12)` focus ring |
| Border — error | `1.5px solid border-error` |
| Border radius | `radius-md` (8px) |
| Height | 46px |
| Padding | 11px vertical · 14px horizontal |
| Font | `body-md` |
| Placeholder color | `text-tertiary` |
| Disabled | opacity 0.42 · background `rgba(26,26,26,0.04)` · cursor: not-allowed |

#### Behavior

- Label always sits above the field. No floating label pattern.
- Error state triggers on blur, not while typing. Clear the error as the user corrects it.
- Input type must match content: `type="email"`, `type="password"`, `type="text"`, `type="tel"`.
- Auto-capitalize off for email and password. On for name fields.

### Note Textarea — NEW

Multi-line text input used on the Note Step. Visual cousin of Text Input but distinct enough to be its own component because of the multi-line behavior and character counter pairing.

#### Visual specification

| Property | Value |
|---|---|
| Background | `surface-nested` (cream) — distinguishes from regular Text Input |
| Border — default | `1.5px solid border-default` |
| Border — focused | `1.5px solid border-focus` + 3px ring (same as Text Input) |
| Border radius | `radius-lg` (12px) — stepped up from Text Input's `radius-md` to match the looser feel of multi-line input |
| Min height | 120px |
| Max height | 240px (then scrolls internally) |
| Padding | 14px |
| Font | `body-md` |
| Placeholder color | `text-tertiary` |

#### Character counter (paired with Note Textarea)

| Property | Value |
|---|---|
| Format | `{count} / 280` — right-aligned below textarea |
| Font | `body-xs` |
| Default color | `text-tertiary` |
| Approaching limit (260–280) | `purple-500` |
| Over soft limit (281+) | `status-error-text` |

Soft limit is 280 client-side (warning only). Hard limit is 500 server-side. Submit is always enabled — empty notes are valid.

### Segment Toggle — NEW

A pill-shaped two-option switch. Used for Phone/Email toggle on auth, By category / By stage on Topic List and Progress, and question type tabs on Question (if present in production).

#### Visual specification

| Property | Value |
|---|---|
| Container | `radius-full` · `1.5px solid border-default` outline · `surface-card` bg |
| Height | 40px (default) · 32px (compact, for use inside screen headers) |
| Active option | `action-primary` fill · `text-on-brand` label · `radius-full` · 3px inset from container edge |
| Inactive option | Transparent · `text-secondary` label |
| Font | `label-md` |
| Transition | `background 0.2s ease` on switch |

#### Rules

- Only two options. For more, use a different pattern (filter chips, dropdown).
- Active option must always be visually distinct enough to read at a glance — the inset pill is non-negotiable.
- When the toggle controls page content, switching it should smoothly re-arrange content rather than full re-render.

### Checkbox — NEW

Used on Manage Topics for the three-state topic inclusion model. Not used elsewhere in V1.

#### Visual specification

| Property | Value |
|---|---|
| Size | 22×22px |
| Border radius | `radius-sm` (4px) — stepped up to 6px for visual weight at this size |
| State: included | `action-primary` fill · white ✓ checkmark · 13px bold |
| State: "we hid" | `surface-card` bg · `2px dashed border-strong` |
| State: "you hid" | `surface-card` bg · `2px solid border-default` |
| Transition | `all 0.15s ease` on state change |
| Tap behavior | Cycles: Included → You hid. We hid → Included. You hid → Included. |

The three states are specific to Manage Topics. If a checkbox is needed elsewhere, use the two-state Included / Not-included version (drop the "we hid" dashed variant).

### OTP Input — NEW

Six-box numeric code entry. Used on OTP Verification.

#### Visual specification

| Property | Value |
|---|---|
| Count | 6 boxes |
| Size | 48×58px each |
| Border radius | `radius-md` (8px) |
| Background | `surface-card` (white) — always |
| Gap | 10px between boxes |
| Font | Grandstander 26px bold · `text-primary` — exception to the type scale because this is a single-character display, not body text |
| Empty border | `1.5px solid border-default` |
| Filled border | `1.5px solid border-strong` |
| Active border | `1.5px solid border-focus` + 3px focus ring |
| Error border | `1.5px solid border-error` + `status-error-surface` bg tint on all 6 boxes |
| Cursor | 2px blinking purple line in active box |

#### Behavior

- Each digit auto-advances focus to the next box. Backspace moves focus back.
- iOS SMS autofill pastes all 6 digits at once — handle as a single paste event.
- On wrong code: show error state on all boxes + error message. Don't clear digits. User corrects in place.

### Divider

Horizontal rule that separates distinct content sections. Used between form groups, between major page sections, and as an "or" separator before social auth buttons.

#### Variants

| Variant | Usage |
|---|---|
| Default | Between major sections |
| With label ("or") | Auth screens only — between primary form submit and social auth buttons |

#### Visual specification

| Property | Value |
|---|---|
| Line | 1px solid `border-default` |
| Vertical margin | `space-6` above and below |
| Width | Full content width |
| Label text | 12px DM Sans medium, `text-tertiary`, centered between two line segments |
| Label gap | `space-3` between text and line on each side |

### Progress Bar

Linear fill indicator. Three contexts: within-topic question progress, plan overview on Home/Topic List, and stacked multi-segment per-category bars on Progress.

#### Variants

| Variant | Usage | Label |
|---|---|---|
| Bare | Question step progress | None |
| Labeled | Plan overview | Count row above |
| Stacked | Progress screen per-category | Name left, count right |

#### Bare and Labeled — visual specification

| Property | Value |
|---|---|
| Track height | 6px |
| Track color | `rgba(26,26,26,0.10)` on cream · `rgba(26,26,26,0.08)` inside white cards |
| Fill color | `action-primary` |
| Border radius | `radius-full` on both track and fill |
| Fill animation | `width 0.4s ease` on mount and value change |
| Count label | `body-xs` (`text-secondary`) |

#### Stacked variant — visual specification

Used on Progress for per-category breakdowns. Multiple colored segments fill the track in order, with empty track representing "not started."

| Segment | Color | Represents | UI label (in legend or context) |
|---|---|---|---|
| 1. Resolved | `status-success-text` (`#157a46`) | Both answered + user marked resolved | "We're good" |
| 2. Pending | `status-pending-text` (`#1a5170`) | Both answered + reveal seen + user picked "needs more work" | "Needs work" |
| 3. In progress | `action-primary` | Your turn or Waiting | "In progress" |
| Remainder | Empty track | Not started | "Not started" |

Track height: 8px for stacked (slightly taller than bare 6px because there's more information to read).

#### Rules

- Don't use percentages as the primary label — "8 of 23 topics" is more meaningful than "35%". Exception: the alignment score (72%) on Progress is a score, not a count.
- At 0%, show the empty track with no fill.

### Badge / Status Pill

Small inline labels communicating status, category membership, count, or alignment state.

#### Variant family

| Variant | Style | UI label |
|---|---|---|
| Category — unselected | Outlined · `border-strong` · `text-secondary` | Category name |
| Category — selected | Filled `purple-500` · white text | Category name |
| Status: your-turn | Filled `action-primary` · white text | "Your turn" |
| Status: waiting | Neutral gray fill · `text-secondary` | "Waiting on [name]" |
| Status: pending | `status-pending-surface` · `status-pending-text` | "Needs work" |
| Status: resolved | `status-success-surface` · `status-success-text` | "✓ We're good" |
| Status: locked | Subtle gray · `text-tertiary` | "🔒 Locked" |
| Alignment: fully-aligned | `status-success-surface` · `status-success-text` | "🎉 Fully aligned" |
| Alignment: mostly-aligned | `rgba(255,215,85,0.38)` · `yellow-text-dark` | "😌 Mostly aligned" |
| Alignment: worth-conversation | `rgba(255,173,108,0.30)` · `orange-text-dark` | "🤔 Worth a conversation" |
| Count badge | Neutral gray pill | e.g. "5 topics" |

#### Visual specification

| Property | Value |
|---|---|
| Padding | 4px vertical · 10px horizontal |
| Border radius | `radius-full` (always pill-shaped) |
| Font | 12px DM Sans semibold · sentence case (NOT uppercase) |
| Height | ~24px |
| Outlined border | `1.5px solid border-strong` |

#### Rules

- Always `radius-full`.
- Status pills are sentence case — "Your turn", not "YOUR TURN".
- Alignment pills always include their emoji. Load-bearing for quick scanning on the reveal screen.
- Maximum one status pill per topic row. Priority: your-turn > waiting > pending > resolved > locked.

### Avatar

| Token | Diameter | Font size | Usage |
|---|---|---|---|
| `avatar-sm` | 24px | 9px | Tight inline contexts (rare) |
| `avatar-md` | 32px | 12px | Settings partner row, compact contexts |
| `avatar-lg` | 40px | 14px | Home greeting row — primary size |
| `avatar-xl` | 48px | 17px | Waiting screen, profile-prominent moments |

**Off-scale sizes currently in screens — to be retired:**
- 36px (Settings partner, Article byline) → `avatar-md` (32px)
- 40px called `avatar-md` (Home greeting) → `avatar-lg` (40px) — fix the token reference, the size is right

#### States

| State | Appearance | When |
|---|---|---|
| Initials (default) | `purple-500 @ 14%` background · `purple-600` text · DM Sans bold | Account exists, no profile photo (V1 only state) |
| Image | Circular crop of profile photo | V2 — not in V1 scope |
| Pending / unlinked | `2px dashed border-strong` · transparent bg · "?" in `text-tertiary` | Partner hasn't accepted invite yet |

### Toggle / Switch

Binary on/off control. Used in Settings for notification and pacing preferences. Always inside a List Row.

| Property | Value |
|---|---|
| Track dimensions | 44×26px |
| Track — on | `action-primary` |
| Track — off | `rgba(26,26,26,0.18)` |
| Thumb | 20px diameter · white · 3px inset from track edge |
| Thumb shadow | `0 1px 3px rgba(0,0,0,0.20)` |
| Transition | Track color + thumb position · 0.2s ease |
| Tap target | Full list row width × height |

### List Row

Standard row pattern for settings and structured navigation lists.

#### Variants

| Variant | Right element |
|---|---|
| Default (value + chevron) | Value text + "›" |
| Toggle row | Toggle component |
| With avatar | Avatar (md) leading + label + chevron |
| Destructive | None — label uses `status-error-text` |
| Section header | Standalone label above a card group |

#### Visual specification — row

| Property | Value |
|---|---|
| Background | `surface-card` |
| Min height | 52px |
| Padding | 13px vertical · 16px horizontal |
| Row separator | 1px solid `rgba(26,26,26,0.06)` — top border on each row except first |
| Label | `body-md` · `text-primary` |
| Value text | `body-xs` · `text-secondary` |
| Chevron | "›" · 14px · `text-tertiary` |
| Destructive label | `status-error-text` |
| Pressed state | Background `rgba(26,26,26,0.04)` |
| Card container radius | `radius-xl` |
| Card container shadow | `shadow-md` |

#### Visual specification — section header

| Property | Value |
|---|---|
| Font | 11.5px DM Sans semibold · ALL CAPS · letter-spacing +0.06em · `text-secondary` |
| Padding | 13px horizontal · 13px top · 5px bottom |
| Position | Outside the card container, immediately above it |

### Select / Date Picker

Trigger-based inputs that open a native OS picker sheet. We design the trigger; OS handles the picker.

| Property | Value |
|---|---|
| Background | `surface-card` |
| Border — default | `1.5px solid border-default` |
| Border — open/active | `1.5px solid border-focus` |
| Border radius | `radius-md` |
| Padding | 11px vertical · 14px horizontal |
| Height | 46px (matches Text Input) |
| Font | `body-md` |
| Chevron icon | 16px, `text-secondary`, right-aligned. Points down. |

### Slider — REWRITTEN

A 1–10 graduated scale for question variants that need a numeric or intensity response. End labels are per-question (e.g. "Hard no" / "Totally fine") rather than the fixed "Strongly disagree / Strongly agree" of v1.0.

#### Visual specification

| Property | Value |
|---|---|
| Scale | 1 to 10, discrete integer steps |
| Track height | 6px |
| Track color (unset) | `rgba(26,26,26,0.12)` throughout |
| Fill color (set) | `action-primary` — fills from left to current value |
| Track border radius | `radius-full` |
| Thumb diameter | 28px |
| Thumb color | `surface-card` (white) |
| Thumb border | `2px solid action-primary` |
| Thumb shadow | `shadow-sm` |
| Value display | Grandstander 32px bold · `action-primary` · centered above thumb |
| End labels | `minLabel` (left) / `maxLabel` (right) · `body-xs` · `text-tertiary` · 10px below track · always visible |
| Touch target | 44px height around track — full-width drag zone |
| Snap animation | thumb snaps to nearest integer on release · `left 0.15s ease` |

#### Default (no value selected) state

Thumb sits ghosted at midpoint (position 5) at 40% opacity. Fill is absent. Value display is hidden. Continue button is disabled until the user drags or taps to set a value.

The v1.0 spec used border swap to indicate unset — v2.0 uses opacity. Opacity reads more clearly that the thumb is "not yet committed."

#### Interaction

| Gesture | Behavior |
|---|---|
| Drag thumb | Follows finger continuously, snaps to nearest integer on release |
| Tap on track | Thumb jumps to tapped position (nearest integer), counts as a selection |
| First interaction | Thumb opacity transitions to 100%, value display appears, Continue enables |
| Haptic | Light impact on each integer snap |

#### Don't

- Don't use a continuous (non-snapping) slider. All values are integers 1–10.
- Don't show percentage or raw fraction labels. End labels only.
- Don't auto-advance on slider interaction. Same rule as multiple choice.

### Daisy Mark — NEW

The Daisy logo asset. Used at the "done" state on `building-your-plan`, on `name-entry` as a welcome anchor, and planned for additional supplemental moments.

#### Size scale

| Token | Diameter | Usage |
|---|---|---|
| `daisy-sm` | 24px | Inline use alongside body copy (e.g., paired with a brand mention) |
| `daisy-md` | 48px | Building Your Plan done state, Name Entry, mid-density welcome moments |
| `daisy-lg` | 80px | Empty state circles, splash-adjacent moments, large welcome anchors |

#### Visual specification

| Property | Value |
|---|---|
| Asset | `daisy.png` |
| Default position | Centered above the heading or content it precedes |
| Spacing below | `space-6` (24px) to next element, by default |

If a new use needs a size outside the scale (e.g., a 128px hero treatment), add it as `daisy-xl` rather than introducing a one-off value.

### Countdown Pill — NEW

Small inline timer pill. Used on OTP Verification for the resend cooldown.

| Property | Value |
|---|---|
| Style | `radius-full` · `surface-nested` bg · 4px 10px padding |
| Font | `body-xs` · `text-tertiary` |
| Content | "30s" counting down to 0, then disappears |
| Position | Inline next to the affordance it's gating (e.g. "Resend code") |

### Category Pill — NEW

Compact inline pill used on Personalized Results to display the 7 book category names.

| Property | Value |
|---|---|
| Background | `rgba(95,69,242,0.08)` |
| Text | `action-primary` |
| Border radius | `radius-full` |
| Padding | 5px 12px |
| Font | 12px DM Sans semibold |
| Layout | Flex wrap · 6px gap |
| Interaction | Not interactive — display only |

Names rendered verbatim in Title Case from the book. Never abbreviated, reworded, or lowercased.

---

## Navigation

### Bottom Nav

Persistent access to the four primary destinations.

| Property | Value |
|---|---|
| Height | 64px + bottom safe-area inset |
| Background | `surface-card` |
| Top border | `1px solid border-default` |
| Position | Fixed to bottom of viewport |
| z-index | `z-sticky` |
| Tab layout | Vertical stack: icon on top, label below |
| Icon size | 24×24px |
| Label style | `label-sm` 11px DM Sans medium — NOT uppercase here |
| Active color | `action-primary` (icon + label) |
| Inactive color | `text-secondary` (icon + label) |

#### Destinations (fixed order)

| Position | Destination | Slug |
|---|---|---|
| 1 | Home | `home` |
| 2 | Topics | `topic-list` |
| 3 | Progress | `progress` |
| 4 | Settings | `settings` |

#### Rules

- Tab order never changes. Muscle memory.
- No badges or notification dots in V1.
- Capped at four tabs. No "More" overflow ever.
- Tapping the active tab scrolls the destination back to top.

### Screen Header

Top chrome on every flow screen.

| Element | Required? | Spec |
|---|---|---|
| Back button | Conditional | Left-aligned · 44×44px · chevron · `text-primary` |
| Screen title | Optional | `heading-md` · `text-primary` · centered (with equal right offset to balance back) |
| Right action | Optional | Right-aligned · 44×44px · Tertiary button or icon |

| Property | Value |
|---|---|
| Height | 56px |
| Background | `surface-page` by default; `surface-card` on screens with a white background |
| Border (default) | None |
| Border (scrolled) | `1px solid border-default` on bottom |
| Horizontal padding | 4px |

### Article Nav Bar — NEW

Lightweight nav used on Topic Article. Distinct from Screen Header because it has read-time metadata on the right rather than a generic right action.

| Element | Spec |
|---|---|
| Back link | "‹ Back to topic" · 44px tap target · `action-primary` · `label-lg` |
| Read time | "X min read" · right-aligned · `body-xs` · `text-tertiary` |
| Border | `1px solid border-default` bottom on scroll |

---

## Feedback & overlays

### Toast / Snackbar

Brief system-level feedback that appears at the bottom of the screen and auto-dismisses.

| Variant | Background | Text |
|---|---|---|
| Info | `black-900` | White |
| Success | `status-success-text` (`#157a46`) | White |
| Error | Dark red `#5a1a1a` | White |
| Warning | Dark amber `#4d2e00` | White |

(v1.0 had a darker green `#1a4d35` for success. v2.0 unifies on `status-success-text` for the toast bg as well as text-on-green usage.)

| Property | Value |
|---|---|
| Border radius | `radius-xl` |
| Padding | 14px vertical · 16px horizontal |
| Max width | 343px |
| Shadow | `shadow-lg` |
| Position | Fixed · horizontally centered · 16px above bottom nav (or safe-area inset) |
| z-index | `z-toast` |
| Auto-dismiss | 3 seconds · swipe down to dismiss early |

#### Rules

- One toast at a time. New toast dismisses the existing one.
- Use for transient feedback only. Use a modal for decisions.
- Optional action is a single word ("Undo", "Retry", "View"). Never a full sentence.

### Modal / Dialog

Interrupts the current flow to present a decision.

| Property | Value |
|---|---|
| Backdrop | `surface-overlay` · z-index `z-overlay` |
| Modal card background | `surface-card` |
| Border radius | `radius-2xl` |
| Width | 343px |
| Padding | 28px top · 24px sides · 20px bottom |
| Shadow | `shadow-lg` |
| z-index | `z-modal` |
| Title | `display-sm` (20px Grandstander bold) · `text-primary` |
| Body | `body-md` · `text-secondary` |
| Actions | Stacked column · primary first · cancel/secondary below · 8px gap |

#### Rules

- Always provide a clear exit.
- Destructive modals use the Destructive button variant — never Primary purple for a destructive action.
- Maximum two actions. More → use a full screen.
- Maximum 2–3 sentences in body.

### Bottom Sheet

A panel that slides up from the bottom.

| Property | Value |
|---|---|
| Backdrop | `surface-overlay` |
| Background | `surface-card` |
| Border radius | `radius-2xl` top corners only |
| Drag handle | 40×4px · `border-default` fill · `radius-full` · centered · 12px from top edge, 20px above content |
| Padding | 12px top (handle) · 24px sides · 28px bottom (+ safe-area) |
| Shadow | `shadow-lg` |
| z-index | `z-modal` |
| Entry animation | Slide up · 280ms ease-out |
| Max height | 85% of viewport |

(v1.0 listed drag handle as 4×36px in one place and 40×4px in another. v2.0 standardizes on 40×4px — width × height, wider than tall.)

### Empty State

Full-page pattern for when there's nothing to show yet. Daisy's Guide empty states are warm and slightly sarcastic — they match the brand's voice and turn an absence into a moment of personality.

| Property | Value |
|---|---|
| Layout | Centered flex column · fills available screen height |
| Background | `surface-page` |
| Illustration | 80×80px circle container · `rgba(95,69,242,0.08)` fill · icon/emoji centered |
| Title | `display-md` · `text-primary` · 24px below illustration |
| Body | `body-md` · `text-secondary` · max-width 280px · 12px below title · 28px before CTA |
| CTA | Primary button (Large) · optional — not all empty states need an action |
| Horizontal padding | `space-8` |

#### Rules

- Empty state copy must match brand voice. "No partner linked" is wrong; "Still flying solo" is right.
- Always give a way out — CTA toward filling the empty state or back to somewhere useful.
- Don't show an empty state while content is loading — show Loading instead.

### Loading / Processing

Two patterns: the **processing checklist** (Building Your Plan — `building-your-plan`) and **skeleton screens** (any data load).

#### Pattern 1: Processing checklist

Used on `building-your-plan`. Makes the personalization algorithm feel intentional.

| Property | Value |
|---|---|
| Step states | Done (faded, ✓) · Active (full opacity, spinner) · Pending (heavily faded, ○) |
| Step card | `surface-card` · `radius-lg` · `shadow-sm` · 14px text |
| Step timing | ~700ms per step. Total: ~2–3 seconds. |
| Done icon | "✓" · `status-success-text` |
| Active icon | Purple spinner |
| Pending icon | "○" · `text-tertiary` |
| Layout | Centered · max-width 300px · 10px gap between steps |

#### Pattern 2: Skeleton

Used for async data loads.

| Property | Value |
|---|---|
| Skeleton lines | Rounded rectangles (`radius-sm`) · varying widths to mimic real content |
| Animation | Shimmer — gradient sweeps left to right · 1.6s ease-in-out · infinite |
| Color | `rgba(26,26,26,0.06)` base → `rgba(26,26,26,0.12)` at shimmer peak |

#### Rules

- Never show a blank screen.
- Skeleton layouts should approximate real content structure.
- Processing checklist is only for `building-your-plan`. Everything else uses skeletons.
- If data loads in under 200ms, skip the skeleton.

### Inline Banner — NEW

Non-blocking notification at the top of a screen. Used for connection error (variant B, mid-session) and payment failure error message.

#### Variants

| Variant | Background | Border | Text color |
|---|---|---|---|
| Neutral (offline, info) | `rgba(26,26,26,0.06)` | None | `text-secondary` |
| Error | `status-error-surface` | `1px solid border-error` | `status-error-text` |
| Success | `rgba(119,234,175,0.18)` | `1px solid status-success-surface` | `status-success-text` |

| Property | Value |
|---|---|
| Border radius | `radius-lg` |
| Padding | 12px 14px |
| Layout | Icon left (optional) · text right · close × on far right (optional) |
| Title font | `body-xs` bold |
| Body font | `body-xs` regular |
| Position | Top of scroll area · persistent (manually dismissible only) |

#### Rules

- Use for non-blocking states. If the user must respond, use a modal.
- Don't use error red for "not your fault" states (offline, server hiccup). Use neutral.
- Banner is persistent — auto-dismiss is a toast pattern, not a banner pattern.

---

## App-specific components

### Topic Card

The spotlight variant — used on `home` "Up next" and `prediction-card` list entries. For the compact list pattern, see Topic Row below.

#### States

| State (data model) | UI label | Meaning | Left border | Opacity | Status pill text |
|---|---|---|---|---|---|
| `available` | — | Neither has answered | None | 100% | None |
| `your-turn` | "Your turn" | Partner has answered; user hasn't | `action-primary` (3px) | 100% | "Your turn" |
| `waiting` | "Waiting" | User answered; partner hasn't | `border-strong` (3px) | 100% | "Waiting on [name]" |
| `pending` | "Needs work" | Both answered, user picked "needs more work" on reflection | `status-pending-surface` (3px) | 100% | "Needs work" |
| `resolved` | "We're good" | User marked resolved on `post-reveal-reflection` | `status-success-surface` (3px) | 100% | "✓ We're good" |
| `locked` | "Locked" | Paywall or time gate | None | `opacity-locked` (55%) | "🔒 Locked" |

Token names stay semantic (`status-pending-*`, `status-resolved-*`) so the data model and CSS stay coherent. The user-facing labels are display-only.

(v1.0 had 5 states with "Complete." v2.0 splits Complete into Pending + Resolved to match the new post-reveal lifecycle.)

#### Visual specification

| Property | Value |
|---|---|
| Background | `surface-card` |
| Border radius | `radius-xl` |
| Shadow | `shadow-md` |
| Padding | `space-4` |
| Left border | 3px solid · state-dependent (see table) |
| Icon | Topic emoji · 28px · left-aligned · 40px container |
| Title | `label-lg` bold · `text-primary` |
| Description | `body-xs` · `text-secondary` · 1–2 lines · truncate with ellipsis |
| Tap target | Full card. Locked is non-interactive. |

### Topic Row — NEW (compact list variant)

Used on `topic-list` for the dense list view. Multiple rows live inside a single white card container.

#### Visual specification

| Property | Value |
|---|---|
| Container | `surface-card` · `radius-xl` · `shadow-md` · rows separated by 1px solid `rgba(26,26,26,0.06)` |
| Row min height | 52px |
| Row padding | 12px vertical · 16px horizontal |
| State dot | 10px circle · left of label · color per state |
| Topic name | `body-sm` medium · `text-primary` · ellipsis on overflow · **bold** for "Your turn" state |
| Status pill | Right-aligned · 11px DM Sans semibold · color per state |
| Pressed state | `rgba(26,26,26,0.03)` row background |
| Locked | No tap animation · no navigation · cursor default |

States and colors match Topic Card. Sort priority within group: your-turn > available > waiting > pending ("Needs work") > resolved ("We're good") > locked.

### Topic Toggle Row — NEW

Used on `manage-topics` for the 3-state inclusion checkbox + topic name + reason text pattern.

| Element | Spec |
|---|---|
| Layout | Checkbox left · text block right |
| Checkbox | See Checkbox component (3-state variant) |
| Topic name | `body-sm` · `text-primary` (included) or `text-tertiary` (hidden) |
| Reason text | Below name · `body-xs` · `text-tertiary` · only shown for hidden states |
| "Tap to add back" | Inline link in reason text · `text-link` color |
| Row padding | 10px vertical |
| Row separator | 1px solid `rgba(26,26,26,0.06)` |

### Question Card

The primary interaction surface of the app.

#### Container

| Property | Value |
|---|---|
| Background | `surface-card` |
| Border radius | `radius-xl` |
| Shadow | `shadow-md` |
| Padding | `space-6` all sides |
| Width | Full width with `space-4` horizontal screen margin |

#### Question text

| Property | Value |
|---|---|
| Font | `display-sm` |
| Color | `text-primary` |

(In v1.0 this was inconsistent across screens. v2.0 standardizes on `display-sm` (20px Grandstander) for question text.)

#### subText

| Property | Value |
|---|---|
| Font | `body-sm` |
| Color | `text-secondary` |
| Position | 6px below question text · 16px above answer area |

#### Answer options

| Property | Default | Selected |
|---|---|---|
| Background | `surface-nested` | `action-primary` |
| Text color | `text-primary` | `text-on-brand` |
| Border radius | `radius-lg` | (same) |
| Padding | `space-4` vertical · `space-5` horizontal | (same) |
| Min height | 56px | (same) |
| Gap between options | `space-2` | (same) |
| Font | `label-lg` | (same) |

Single-select OR multi-select — same visual treatment, behavior is the only distinction. Press: `scale(0.98)`. Transition: 150ms ease.

#### Behavior rules

- **Tapping an answer never auto-advances.** User must tap Continue.
- **Tapping Skip skips without saving.** Question can be returned to.
- **Selection persists if user navigates away and returns.**
- Maximum 6 answer options.

#### Don't

- Don't use Grandstander for answer option text.
- Don't auto-advance.
- Don't add icons to answer options.
- Don't put question text in ALL CAPS.

### Reveal Box — single-select

Used on `alignment-reveal` for single-select question reveals. Always used as a pair — two boxes side by side.

#### Visual specification — each box

| Property | Value |
|---|---|
| Background | `surface-card` |
| Border | `1.5px solid border-default` |
| Border radius | `radius-lg` |
| Padding | 14px |
| Min height | 100px |
| Width | `flex: 1` |
| Gap between boxes | 10px |

#### Anatomy

| Element | Spec |
|---|---|
| Owner label | "YOU SAID" / "[NAME] SAID" · 11px DM Sans bold · ALL CAPS · `+0.05em` · `text-secondary` · 8px below |
| Answer text | `body-sm` · `text-primary` · line-height 1.5 · verbatim |

#### Rules

- Always paired. Left = "You said". Right = partner. Never inverted.
- Answer text is the user's verbatim selection — never paraphrased.
- Always followed by a "For You Two" card on `alignment-reveal`.

### Reveal Box — multi-select — NEW

Used on `alignment-reveal` when the question type is multi-select. Same two-box container as single-select, different content layout.

| Element | Spec |
|---|---|
| Container | Same as single-select Reveal Box |
| Owner labels | "YOU SELECTED" / "[NAME] SELECTED" |
| Content | Flex-wrap row of pill tags · 6px gap |
| Shared pill (both selected) | `rgba(119,234,175,0.28)` bg · `status-success-text` · `radius-full` · 4px 10px padding · 12px DM Sans semibold |
| Unique pill (this person only) | `rgba(26,26,26,0.07)` bg · `text-primary` · same shape/font |
| Shared count badge | "X in common" · centered below both boxes · 12px DM Sans medium · `status-success-text` · 10px margin top · only shown if overlap > 0 |

### Reveal Box — slider — NEW

Used on `alignment-reveal` when the question type is slider. Does NOT use the two-box layout — it's a single full-width card.

| Property | Value |
|---|---|
| Container | `surface-card` · `radius-xl` · `shadow-md` · 20px padding · full width |
| Values row | Left: user's value (Grandstander 28px bold · `action-primary`) + "You" label (11px DM Sans medium · `text-secondary`) · Right: partner's value (Grandstander 28px bold · `text-primary`) + "[name]" label |
| Same-value state | Single centered value (Grandstander 28px bold · `status-success-text`) · "You both said {n}" label below in `status-success-text` 13px medium |
| Track | 6px · `radius-full` · `rgba(26,26,26,0.10)` |
| Range fill | `rgba(95,69,242,0.12)` between the two markers · omitted when same value |
| Your marker | 14px circle · `action-primary` fill · z-index 2 |
| Partner marker | 14px circle · white fill · `2px solid border-strong` · z-index 1 |
| Same-value marker | Single 16px circle · `status-success-text` fill |
| End labels | minLabel left · maxLabel right · `body-xs` · `text-tertiary` · 6px below track |
| Delta label | Centered · 12px · different: "{n} apart" `text-tertiary` · same: "Same ✓" `status-success-text` medium · 12px below end labels |

### For You Two Card — RENAMED (was AI Summary Card)

The AI-generated couples summary that follows the Reveal Boxes on `alignment-reveal` and appears on `completed-topic`.

| Property | Value |
|---|---|
| Border | `1.5px dashed border-strong` |
| Border radius | `radius-lg` |
| Background | `rgba(26,26,26,0.02)` |
| Padding | 16px |
| Shadow | None |
| Label | "✨ FOR YOU TWO" · 11px DM Sans bold · ALL CAPS · `+0.05em` · `text-secondary` · 8px below |
| Body text | `body-sm` · `text-primary` · line-height 1.6 |
| Spacing above | `space-3` |

#### Rules

- The dashed border is part of the broader "supplemental / authored content" treatment, shared with Credibility Card and Resources Card. It is no longer exclusively AI-generated.
- The "✨" is part of the spec. Don't replace.
- AI input is all 4 question texts + both partners' answers + both note texts.
- Copy must be warm, specific, actionable. Never generic ("You have different views"). Never mentions AI.

### Prediction Card Header

A special treatment that sits above the question card on `prediction-card`. Signals "sealed envelope."

#### Three states

| State | Border | Background | Sub-label |
|---|---|---|---|
| Answering | `2px dashed rgba(26,26,26,0.20)` | `rgba(26,26,26,0.03)` | "Sealed until after baby arrives" · `text-tertiary` |
| Locked | `2px solid rgba(26,26,26,0.25)` | `rgba(26,26,26,0.03)` | "Sealed until after baby arrives" · `text-tertiary` |
| Reveal-ready | `2px solid action-primary` | `rgba(95,69,242,0.05)` | "The moment has arrived 🎉" · `text-secondary` |

| Property | Value |
|---|---|
| Border radius | `radius-lg` |
| Padding | 12px 16px |
| Layout | Centered text |
| Primary label | "🔮 Prediction card" · 11px DM Sans bold · `+0.05em` · ALL CAPS via CSS · `text-secondary` |
| Sub-label | 12px DM Sans regular · 3px below primary |
| Spacing below | 16px |

**Note on caps:** v1.0 specified mixed-case label rendered uppercase via CSS. Screens currently use literal ALL CAPS ("PREDICTION CARD"). Standardize: mixed-case source text + `text-transform: uppercase` in CSS.

### Partner Status Block

Inline display of partner's avatar, name, and activity status.

| Property | Value |
|---|---|
| Layout | Flex row · avatar left · text middle · optional action right |
| Background | `surface-card` |
| Border radius | `radius-lg` |
| Shadow | `shadow-sm` |
| Padding | 14px 16px |
| Avatar | `avatar-md` |
| Name | `body-sm` bold · `text-primary` |
| Status | `body-xs` · `text-secondary` |

### Stats Display — CONSOLIDATED

Replaces both Stats Row (3-col) and Stats Card (2-col) from v1.0. One component with a `columns` prop and a `surface` prop.

| Property | Value |
|---|---|
| Layout | Equal-width columns · flex row · full content width |
| Column divider | `1px solid border-default` · right border on each column except last |
| Number style | Grandstander · `text-primary` · `-0.02em` |
| Label style | `label-sm` ALL CAPS · `text-secondary` · 4px below number |
| Alignment | Text centered in column |
| Vertical padding | `space-2` top and bottom per cell |

#### `columns` variants

| Columns | Number size |
|---|---|
| 2 | Grandstander 28px |
| 3 | Grandstander 32px (page-level) or 28px (inside a white card) |

#### `surface` variants

| Surface | Container |
|---|---|
| Bare (on cream page) | No background, no shadow — divider lines between columns only |
| Card | `surface-card` · `radius-xl` · `shadow-md` · 16px padding |
| Sub-card (nested inside screen) | `surface-card` · `radius-lg` · no shadow |

### Hero Image Card

The illustration container on `topic-intro`. 160px-tall white card.

| Property | Value |
|---|---|
| Height | 160px — fixed |
| Width | Full content width |
| Background | `surface-card` |
| Border radius | `radius-xl` |
| Shadow | None |
| Spacing below | `space-6` |
| V1 placeholder | Centered topic emoji at 48px, `text-tertiary` |

#### Rules

- Height is fixed at 160px. Don't let illustrations overflow.
- Never put text inside the hero image card.
- No shadow.

### Feature Promise Card

Icon + title + body cards used on onboarding intro (`onboarding-intro`).

| Property | Value |
|---|---|
| Background | `surface-card` |
| Border radius | `radius-xl` |
| Shadow | `shadow-sm` |
| Padding | 16px |
| Layout | Flex row · icon left (22px) · text right |
| Title | `label-lg` bold · `text-primary` · 4px below |
| Body | `body-xs` · `text-secondary` · line-height 1.5 |
| Gap between cards | `space-3` |

### Price / Purchase Card — UPDATED

The primary conversion element on `paywall`.

| Property | Value |
|---|---|
| Background | `surface-card` |
| Border radius | `radius-xl` |
| Shadow | `shadow-md` |
| Padding | 24px 20px |
| Eyebrow | "One-time purchase" · 12px DM Sans regular · `text-secondary` |
| Price | Grandstander 48px bold · `text-primary` · `-0.02em` |
| Sub-label | "Lifetime access · One-time charge · Does not renew" · 13px · `text-secondary` |
| Feature checkmark | "✓" · `status-success-text` · 14px bold |
| Feature text | `body-sm` · `text-primary` |

**Price:** $49. (v1.0 specified $40. Update.)

**Sub-label copy:** "Lifetime access, One-time charge, Does not renew" (the `·` separator stays — that's a typographic mark, not an em dash). Avoid em dashes in the actual copy.

#### Rules

- One price, one card. No tiers.
- Feature list max 5 items.

### Credibility Card — NEW

The "Dr. Daisy, MD" trust signal on `paywall`. Uses the dashed border treatment per the broader "supplemental/authored content" pattern.

| Property | Value |
|---|---|
| Border | `1.5px dashed border-strong` |
| Background | `rgba(26,26,26,0.02)` |
| Border radius | `radius-lg` |
| Padding | 16px |
| Body | `body-sm` · `text-primary` |
| Emphasis | "Dr. Daisy, MD" rendered bold (`text-primary`) |

### Founding Member Card — NEW

Purple-tinted callout below Credibility on `paywall`. Communicates time-limited pricing.

| Property | Value |
|---|---|
| Background | `rgba(95,69,242,0.05)` |
| Border | `1px solid rgba(95,69,242,0.15)` |
| Border radius | `radius-lg` |
| Padding | 12px 14px |
| Title row | "🔒 Founding member pricing" · 12px DM Sans bold · `action-primary` · 6px below |
| Body | 12px DM Sans regular · `text-secondary` |

### Invite Link Card

Shareable partner invite URL on `partner-linking`.

| Property | Value |
|---|---|
| Background | `surface-card` |
| Border | `1px solid border-default` |
| Border radius | `radius-lg` |
| Shadow | `shadow-sm` |
| Padding | 16px |
| Card label | "Your invite link" · 13px DM Sans bold · `text-primary` · 8px below |
| URL display | Monospace font · 13px · `action-primary` · `rgba(95,69,242,0.06)` bg · `radius-sm` · 8px 10px padding · `word-break: break-all` |

#### Rules

- URL is display-only. Tap to select/copy, doesn't navigate.
- Never truncate with ellipsis. Use `word-break: break-all`.

### Badge Notification Card

Achievement unlock announcement on `home`.

| Property | Value |
|---|---|
| Background | `surface-card` |
| Border | `1px solid rgba(255,215,85,0.5)` — yellow at 50% |
| Border radius | `radius-lg` |
| Shadow | `shadow-sm` |
| Padding | 14px 16px |
| Layout | Flex row · 🏅 medal emoji left (24px) · text right |
| Body text | `body-sm` · `text-primary` · badge name in bold |
| Dismissibility | Tapping dismisses |

### Progress Row — UPDATED

Composed row showing one category's completion. Stacked vertically on `progress` to show all 7 categories.

(v1.0 specified a single fill bar. v2.0 uses the multi-segment stacked variant by default — see Progress Bar Stacked variant above.)

| Element | Spec |
|---|---|
| Category name | `body-xs` medium · `text-primary` · left-aligned |
| Count label | `body-xs` · `text-secondary` · right-aligned |
| Bar | Stacked Progress Bar (8px) — see Progress Bar component |
| Gap between rows | `space-5` |
| Tap target | Minimum 44px — pad if needed |
| Tap behavior | Navigates to `topic-list` filtered to that category |

#### The 7 categories (fixed)

1. The Basics
2. Pregnancy & Birth
3. The Village
4. Eat, Poop, Sleep
5. Health & Development
6. The Existential
7. Us

Names rendered in Title Case verbatim. Order matches book.

### Reflection Status Pill — NEW

Interactive pill on `completed-topic` that shows current reflection state ("We're good" / "Needs work") and opens the selector when tapped.

| Property | Value |
|---|---|
| Pill | Standard Badge / Status Pill — resolved or pending variant |
| Inline suffix | " · Tap to change" · `body-xs` · `text-tertiary` |
| Tap behavior | Opens `post-reveal-reflection` 2-option selector |

### Option Card — NEW

Selectable card used on `post-reveal-reflection`. Replaces older "Talk about it / Revisit later" pattern.

| Property | Value |
|---|---|
| Background | `surface-card` |
| Border (default) | `1.5px solid border-default` |
| Border (selected) | `1.5px solid action-primary` + `0 0 0 3px rgba(95,69,242,0.12)` focus ring |
| Border radius | `radius-xl` |
| Shadow | `shadow-md` |
| Padding | 16px vertical · 18px horizontal |
| Layout | Emoji icon left (22px) · text block right · 14px gap |
| Title | `label-lg` bold · `text-primary` |
| Body | `body-xs` · `text-secondary` |
| Press state | `transform: scale(0.99)` |
| Gap between cards | 10px |

Single-select. Tapping another deselects previous.

### Info Card ("How it works") — NEW

Numbered-step explainer card used on `personalized-results` ("How it works") and as a general pattern.

| Property | Value |
|---|---|
| Background | `surface-card` |
| Border radius | `radius-xl` |
| Shadow | `shadow-md` |
| Padding | 16px |
| Title | `body-sm` bold · `text-primary` |
| Step number | Grandstander 14px bold · `action-primary` · left of step text — exception to type scale, accepted as deliberate display treatment |
| Step body | `body-xs` regular · `text-secondary` |
| Gap between items | `space-2` |

### Onboarding Nudge Card — NEW

Purple-filled brand card used on `empty-home` to push first-time users toward their first action.

| Property | Value |
|---|---|
| Background | `surface-brand` |
| Border radius | `radius-xl` |
| Padding | 18px |
| Eyebrow | "Get started" · `label-sm` ALL CAPS · white 60% opacity |
| Heading | `display-sm` · white |
| Body | `body-xs` · white 75% opacity · max 2 lines |
| CTA | White-filled pill button · `action-primary` label · 42px height · full-width |
| Dismissal | Automatically disappears once user taps into any topic intro |

(42px CTA inside is a contained exception — outside this card, button heights follow the standard 56/44/32 scale.)

### Chaos Meter — NEW

Easter-egg 1–10 score on `progress`. Running joke about how divergent the couple's answers have been.

| Property | Value |
|---|---|
| Container | `surface-card` · `radius-xl` · `shadow-md` · 16px padding |
| Title | "🌡️ Chaos meter" · `body-sm` bold |
| Score | Grandstander inline in sentence · `display-sm` · `action-primary` |
| Body | "Based on how different your answers have been... you're at [X] / 10. Perfectly normal. Probably." — exact copy |
| Visibility | Hidden until user has 3+ revealed topics |
| Calculation | Higher = more divergent answers. Never explain the formula to users. |

#### Rules

- Never explain the calculation in UI. Mystery is the point.
- Don't promote this metric. It sits at the bottom of `progress`, below the real data.

### "What Happens Next" Card — NEW

Tinted explainer card used on `re-answer-flow` to set expectations before triggering a re-answer round.

| Property | Value |
|---|---|
| Background | `rgba(26,26,26,0.04)` — subtle tint, not white card |
| Border | `1px solid border-default` |
| Border radius | `radius-xl` |
| Padding | 18px |
| Step numbers | Grandstander 14px bold · `action-primary` · left of each step |
| Step text | `body-xs` · `text-secondary` · line-height 1.5 |

### Article Byline — NEW

The "Dr. Daisy, MD · Medically reviewed" attribution on `topic-article`.

| Property | Value |
|---|---|
| Layout | Flex row · avatar left · text right |
| Avatar | `avatar-md` (32px) — was 36px in screens, normalize to scale |
| Name | "Dr. Daisy, MD" · `body-xs` bold · `text-primary` |
| Sublabel | "Medically reviewed" · 12px · `text-secondary` |
| Borders | 1px solid `border-default` top and bottom — sets the byline apart from article body |

### Sticky CTA Region — NEW pattern

Used on `topic-article`, `manage-topics`, and other long-scroll screens where the primary action must remain reachable.

| Property | Value |
|---|---|
| Position | `position: sticky` or `position: absolute` at viewport bottom |
| Background | Gradient fade from transparent (top) to `surface-page` (30% from top) — content scrolls under gracefully |
| Padding | 12px top · 20px sides · 24px bottom (+ safe-area inset) |
| Button | Primary (Large) · `shadow-lg` to lift above content |
| z-index | `z-sticky` |

### Emoji Feedback Block — NEW

3-emoji satisfaction rating on `topic-article` ("Was this guide helpful?").

| Property | Value |
|---|---|
| Emojis | 😞 😐 😊 — fixed set, in order |
| Size | 28px |
| Gap | 20px between |
| Interaction | `scale(1.2)` on hover/tap · tap logs feedback and shows brief "Thanks!" toast |
| Label | "Was this guide helpful?" · `label-md` · `text-secondary` · 12px below section border |
| Separator | `1.5px dashed border-default` above block |

### Resources Card — NEW

Additional links section at the end of `topic-article`. Uses the dashed border treatment per the broader "supplemental/authored content" pattern.

| Property | Value |
|---|---|
| Border | `1.5px dashed border-strong` |
| Background | `rgba(26,26,26,0.02)` |
| Border radius | `radius-lg` |
| Padding | 16px |
| Label | "Additional resources" · 11px DM Sans bold · ALL CAPS · `+0.05em` · `text-tertiary` |
| Links | `body-xs` · `action-primary` · each link on its own line |

---

## Cross-cutting patterns

### Dashed border treatment — what it signals

In v1.0 the dashed border meant "AI-generated content." In v4 it's used on:

- For You Two Card (AI-generated)
- Credibility Card (authored by Dr. Daisy)
- Resources Card (external links)
- Prediction Card Header (sealed/special)

The unifying meaning is **"supplemental or authored content distinct from the main flow"** — not strictly AI. v2.0 adopts this broader meaning. The dashed border tells the user: "this content was placed here intentionally and isn't part of the standard interaction."

If a fifth use comes up that doesn't fit this definition, it's a sign the treatment is being overused, not a sign to broaden again.

### Brand voice in empty states and error states

Two voice rules:

1. **Empty states are warm and slightly sarcastic.** "No partner linked" is wrong; "Still flying solo. Bold choice." is right. The brand earns trust by acknowledging the absence with personality.
2. **Error states are honest about whose fault it is.** Connection drops aren't the user's fault — use neutral language ("You're offline") and a neutral banner color, not error red. Payment failures get error styling because the user needs to act. Server errors get apologetic copy ("Something went wrong on our end").

The voice never apologizes for the app's existence. It can apologize for specific failures.

### Topic lifecycle — "Needs work" vs "We're good"

Every topic moves through this state machine. Internal state names (pending, resolved) are the data-model values. The labels in parentheses are what users actually see.

```
available → your-turn / waiting → (both submit) → reveal seen → post-reveal-reflection
                                                                       ↓
                                                            ┌──────────┴──────────┐
                                                         resolved              pending
                                                       ("We're good")       ("Needs work")
                                                                                ↓
                                                                       optional reminder
```

- **`resolved`** (label: "We're good") means the user picked "We're good, mark resolved" on the post-reveal reflection screen. We're done with this topic for now.
- **`pending`** (label: "Needs work") means the user picked "Needs more work" on the same screen. Optionally sets a reminder.
- Both states appear in the Topic Row status pill, the Topic Card spotlight on Home, the Reflection Status Pill on Completed Topic, and the stacked bar segments on Progress.
- These states are NOT shown on the Alignment Reveal screen itself — the reveal is just the reveal. Reflection happens on the screen after.

**Why two layers (data model + label):** "Pending" as a label sounds bureaucratic and doesn't match the brand voice. "Needs work" is honest and warm. But the data model needs stable state names that don't change when copy gets reworded. So the tokens, schema, and code use `pending`/`resolved`; only the displayed text uses the labels.

### Re-answer round mechanics

Either partner can initiate. Topic state during round:

- Initiator's old reveal remains canonical until both have re-answered
- Partner gets a push: "[name] wants to re-answer [topic]. Want to re-answer together?"
- 14-day expiry. Nudges at day 7 and day 13.
- If partner doesn't respond, round expires and topic returns to prior Completed state. Initiator's pending re-answers are discarded.

Previous answers are retained server-side but not surfaced in UI for V1.

---

## Screen index

The 30 v4 screens (29 main + 1 sub-step). All references in this document use slugs; screen numbers are presentation only and may change.

| Slug | File | Section | Bottom nav |
|---|---|---|---|
| `swipeable-intro` | 01-swipeable-intro.html | Intro | Hidden |
| `onboarding-quiz` | 02-onboarding-quiz.html | Intro | Hidden |
| `building-your-plan` | 03-building-your-plan.html | Intro | Hidden |
| `sign-up` | 04-sign-up.html | Auth | Hidden |
| `otp-verification` | 05-otp-verification.html | Auth | Hidden |
| `name-entry` | 06-name-entry.html | Auth | Hidden |
| `log-in` | 07-log-in.html | Auth | Hidden |
| `personalized-results` | 08-personalized-results.html | Onboarding | Hidden |
| `paywall` | 09-paywall.html | Onboarding | Hidden |
| `partner-linking` | 10-partner-linking.html | Onboarding | Hidden |
| `home` | 11-home.html | Home base | Shown |
| `progress` | 12-progress.html | Home base | Shown |
| `settings` | 13-settings.html | Home base | Shown |
| `topic-list` | 14-topic-list.html | Topic flow | Shown |
| `manage-topics` | 15-manage-topics.html | Topic flow | Conditional (hidden in onboarding context) |
| `topic-intro` | 16-topic-intro.html | Topic flow | Hidden |
| `topic-article` | 17-topic-article.html | Topic flow | Hidden |
| `question` | 18-question.html | Topic flow | Hidden |
| `note-step` | 18b-note.html | Topic flow | Hidden |
| `waiting-for-partner` | 19-waiting-for-partner.html | Topic flow | Hidden |
| `alignment-reveal` | 20-alignment-reveal.html | Topic flow | Hidden |
| `post-reveal-reflection` | 21-post-reveal-reflection.html | Topic flow | Hidden |
| `re-answer-flow` | 22-re-answer-flow.html | Topic flow | Hidden |
| `completed-topic` | 23-completed-topic.html | Topic flow | Hidden |
| `prediction-card` | 24-prediction-card.html | Special | Hidden |
| `empty-home` | 25-empty-home.html | Empty states | Shown |
| `empty-topic-list` | 26-empty-topic-list.html | Empty states | Shown |
| `payment-failure` | 27-payment-failure.html | Error states | Hidden |
| `connection-error` | 28-connection-error.html | Error states | Conditional (variant A hidden, variant B shown) |
| `onboarding-intro` | 29-onboarding-intro.html | A/B test variant | Hidden |

Each screen file is its own spec. The design system documents foundations and components; screens compose them.

---

## Migration notes

### What's no longer in the system

- **Screen 12 Topic Intro spec** from v1.0 — replaced by the `topic-intro` screen file at 16-topic-intro.html, which is the canonical spec for this screen.
- **`status-error` and `status-success` bare tokens** — retired. Use `status-error-text` / `status-error-surface` / `border-error` and `status-success-text` / `status-success-surface`.
- **Hardcoded greens `#1c7d3e` and `#1a4d35`** — retired. Use `status-success-text` (`#157a46`).
- **"AI summary" card name** — renamed to "For you two."
- **Topic state "Complete"** — split into pending (UI label: "Needs work") and resolved (UI label: "We're good").
- **Slider 1–5 scale** — replaced with 1–10 scale and per-question end labels.
- **Stats Row and Stats Card** — merged into single Stats Display component.
- **Drag handle 4×36px** — standardized to 40×4px. (v1.0 had both.)
- **List Row value text 13.5px** — normalized to 13px (`body-xs`).
- **List Row chevron 16px** — normalized to 14px.

### What's new

- Ghost button as 4th variant.
- Note Textarea, Segment Toggle, Checkbox, OTP Input, Daisy Mark, Countdown Pill, Category Pill (universal components)
- Article Nav Bar (navigation)
- Inline Banner (feedback)
- Topic Row, Topic Toggle Row, Reveal Box (multi-select), Reveal Box (slider), Credibility Card, Founding Member Card, Reflection Status Pill, Option Card, Info Card, Onboarding Nudge Card, Chaos Meter, "What Happens Next" Card, Article Byline, Sticky CTA Region, Emoji Feedback Block, Resources Card (app-specific components)
- "Needs work" and "We're good" as the new UI labels for the post-reveal lifecycle states (data model unchanged: still `pending` and `resolved`)
- Blue family for "Needs work" surface and text (`blue-text-dark` primitive added)
- Stacked Progress Bar variant
- Per-question slider end labels (replaces fixed "Strongly disagree / agree")
- Daisy Mark size scale (sm / md / lg)

### What changed but stayed

- Type scale gained `display-sm`, `body-sm`, `body-xs` to reduce drift.
- Avatar `avatar-md` (32px) is reaffirmed — multiple screens incorrectly applied `avatar-md` to a 40px element. Fix the token reference, not the size.
- Letter-spacing convention is now `em` throughout.

---

## Drift prevention

The drift between v1.0 and v4 happened because the design system, screen files, decisions log, and CHANGELOG are four separate documents that all need to be updated in the right order, and the order isn't enforced anywhere. Practical safeguards:

### 1. Screens reference tokens by name, not by value

Each screen's spec table should cite tokens (`padding: space-4`), not raw values (`padding: 16px`). When a token changes, the screen automatically reflects it. When a screen specifies a raw value that doesn't match the token, that's a drift signal worth catching in review.

### 2. CHANGELOG section in this file

See bottom of this document. Every decision recorded inline. No external decisions log to fall out of sync.

### 3. Slug-based references

Screen and component references in prose use slugs (`topic-intro`, `for-you-two-card`), not numbers. Renumbering files doesn't cascade through this document.

### 4. Pre-commit grep (optional but cheap)

A 50-line script in the repo's `pre-push` hook can catch the easy ones:

- `status-error` not followed by `-text` or `-surface` → block
- Raw `#ff9191`, `#c0392b`, `#157a46`, `#1c7d3e`, `#1a4d35` in screen files → flag
- Font size or radius that doesn't match the token table → flag
- Internal link to a 404 file → block
- "Screen N" hard-coded reference in any spec doc (use slug) → flag

### 5. Quarterly walk-through

One pass per quarter where each screen is checked against this document. Catches drift while it's 1–2 screens worth, not 24.

### 6. No versioning

This document does not have a version number. It is at HEAD. Changes are dated in the CHANGELOG. If the brand changes substantially enough to warrant a major version, fork the document; otherwise edit in place.

---

## CHANGELOG

Date-stamped record of design system decisions. Add new entries at the top.

### 2026-05-27 — Initial v2.0 release

Foundational rewrite of the design system to align with v4 screens. All 12 structural decisions resolved:

- **Slider scale:** 1–10 with per-question end labels (was 1–5 in v1.0)
- **For You Two card:** renamed from "AI Summary Card"; ✨ emoji + label carry the AI signaling, dashed border meaning broadened
- **Topic Card and Topic Row:** coexist as separate components (Card = Home spotlight, Row = dense list)
- **Stats Display:** consolidated former Stats Row + Stats Card into one component with `columns` and `surface` props
- **Ghost button:** added as 4th non-destructive variant; covers skip / dismiss / soft-exit actions previously specced inconsistently across screens
- **Dashed border treatment:** meaning broadened from "AI-generated content only" to "supplemental or authored content distinct from main flow"; covers For You Two, Credibility, Resources, and Prediction Card Header
- **Topic lifecycle states:** 6 states (available / your-turn / waiting / pending / resolved / locked); UI labels "Needs work" and "We're good" replace bureaucratic "Pending" / "Resolved" in display while data-model state names remain unchanged
- **"Needs work" color:** blue family — `blue-text-dark: #1a5170` on `status-pending-surface: rgba(159,236,250,0.40)`; chosen over amber to keep on-palette and avoid collision with the Mostly Aligned yellow
- **Canonical green:** `#157a46` (`status-success-text`); retired `#1c7d3e` and `#1a4d35`
- **Letter-spacing convention:** `em` throughout
- **Price:** $49 (was $40 in v1.0)
- **Daisy Mark:** size scale of `daisy-sm` (24px), `daisy-md` (48px), `daisy-lg` (80px); extensible with `daisy-xl` if a hero-size use case emerges

Structural changes:

- Migrated from screen-number to slug-based references throughout
- Added type scale tokens: `display-sm`, `body-sm`, `body-xs` to capture sizes that screens were already using off-spec
- Added new primitive: `blue-text-dark`
- Retired `status-error` / `status-success` bare tokens (the migration v1.0 noted but didn't enforce across screens)
- Documented 20+ net-new components introduced in v4 screens (Note Textarea, Segment Toggle, Checkbox, OTP Input, Inline Banner, Topic Row, Topic Toggle Row, Multi-select Reveal Box, Slider Reveal Box, Credibility Card, Founding Member Card, Reflection Status Pill, Option Card, Info Card, Onboarding Nudge Card, Chaos Meter, What Happens Next Card, Article Byline, Sticky CTA Region, Emoji Feedback Block, Resources Card, Daisy Mark, Countdown Pill, Category Pill, Article Nav Bar)
- Added Drift Prevention section with concrete safeguards (CHANGELOG, slug references, pre-commit grep, quarterly walk-through)
- Removed v1.0 inline screen spec for Topic Intro — screen specs now live in their respective screen files
- Standardized bottom sheet drag handle to 40×4px (v1.0 had it both ways)
- Removed version number; document is now living-at-HEAD

### v1.0 — original

- First codified design system
- See git history for prior decisions
