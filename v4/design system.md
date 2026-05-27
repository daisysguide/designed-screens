# Daisy's Guide — Design System v1.0

# Getting Started

## Daisy\'s Guide Design System

The source of truth for all visual and interaction decisions in the Daisy's Guide app. Foundation tokens, component specs, and screen specs — everything Jake needs to build and everything we need to stay consistent as the product grows.

### What's in v1.0

- **Foundation** — color primitives and semantic tokens, typography (Grandstander / DM Sans), spacing (4px base), border radius, shadows, opacity & z-index, and navigation patterns.
- **Universal Components** — Button, Text Input, Divider, Progress Bar, Badge / Status Pill, Avatar, Toggle / Switch, List Row, Select / Date Picker *(🚧 TK)*, Slider *(🚧 TK)*.
- **Navigation** — Bottom Nav, Screen Header.
- **Feedback & Overlays** — Toast / Snackbar, Modal / Dialog, Bottom Sheet, Empty State, Loading / Processing.
- **App-specific Components** — Topic Card, Question Card, Reveal Box, AI Summary Card, Prediction Card Header, Partner Status Block, Stats Row, Stats Card, Hero Image Card, Feature Promise Card, Price / Purchase Card, Invite Link Card, Badge Notification Card, Progress Row *(🚧 TK)*.
- **Screens** — Screen 12: Topic Intro. Additional screen specs to follow.

### How to read this document

- Tokens use a **two-layer system**: primitive tokens are raw values (`purple-500: #5f45f2`); semantic tokens are meaning-based aliases (`action-primary: purple-500`). Components always reference semantic tokens.
- Complete component specs include anatomy, token usage tables, state specs, behavior rules, and "don't" callouts. Specs marked 🚧 are reserved placeholders — structure and anchors are live, full detail to be added before build.
- Visual demos render using the actual token values — what you see is what gets built.

---

# Foundation

## Colors

A two-layer system. Primitives are the palette — raw hex values. Semantic tokens are
meaning-based aliases that components reference. This separation allows primitive values to change
without touching component specs.

### Primitive tokens — brand

### Primitive tokens — accents (soft)

### Primitive tokens — accents (bold)

### Semantic tokens — surfaces

| Token | Value | Usage |
| --- | --- | --- |
| `surface-page` | `cream-50` | Default page background |
| `surface-card` | `white` | Cards and content containers sitting above the page |
| `surface-nested` | `cream-50` | Elements nested inside cards (answer option backgrounds, sub-sections) |
| `surface-inverse` | `black-900` | Dark sections, inverse moments |
| `surface-brand` | `purple-500` | Purple-filled sections |

### Semantic tokens — text

| Token | Value | Usage |
| --- | --- | --- |
| `text-primary` | `black-900` | Body copy, headings, all default text |
| `text-secondary` | `black-900 @ 60% opacity` | Supporting text, captions, labels |
| `text-tertiary` | `black-900 @ 40% opacity` | Placeholder text, de-emphasized metadata |
| `text-on-brand` | `cream-50` | Text on purple-filled surfaces |
| `text-link` | `purple-500` | Interactive inline links |

### Semantic tokens — actions & status

| Token | Value | Usage |
| --- | --- | --- |
| `action-primary` | `purple-500` | Primary button fill, active states, progress fill |
| `action-primary-hover` | `purple-600` | Hover state |
| `action-primary-pressed` | `purple-700` | Pressed state |
| `status-error` | `pink-400 (#ff9191)` | Error state border color — inputs, banners |
| `status-error-text` | `#c0392b` | Form validation error messages, inline error text, destructive List Row labels — WCAG AA compliant (5.7:1 on white) |
| `status-error-surface` | `rgba(255,145,145,0.12)` | Error state background tint — inputs, error banners |
| `status-warning` | `orange-400` | Warning states |
| `status-highlight` | `yellow-400` | Yellow reserved for highlight only |
| `status-success-surface` | `green-400 (#77eaaf)` | Completion fill — progress bars, left borders on complete topic cards, checkmarks on Paywall |
| `status-success-text` | `#157a46` | Text and icons rendered on or near a green surface — "✓ Complete" pill labels, category complete count labels |
| `border-focus` | `purple-500 (#5f45f2)` | Input focused border |

> **Migration note — `status-error` and `status-success` (old single tokens):** Both are retired as of this update. Any reference to the bare `status-error` token should be replaced with `status-error-text` (for text/icon uses) or `status-error-surface` (for background uses). Any reference to the bare `status-success` token should be replaced with `status-success-surface` (fills, borders) or `status-success-text` (text/icon on green). The off-palette value `#c0392b` that appeared in auth screens 02–04 is now the canonical value of `status-error-text`. Replace all raw `#c0392b` hardcodes with `status-error-text`. Replace all text/icon uses of the bare `status-error` token (#ff9191) with `status-error-text` (#c0392b) — the pink value fails WCAG AA at ~1.75:1 on white.

## Typography

Two typefaces. Grandstander for display and brand moments. DM Sans for everything else.
One font for personality, one for legibility — and never cross the streams.

### Type scale

### Rules

- Grandstander is used exclusively for display sizes, screen titles, and brand moments. Never for
  body copy, labels, or button text.
- ALL CAPS is reserved exclusively for `label-sm`. Never use for headings, body, or
  display sizes.
- Grandstander letter-spacing: `-0.02em`. DM Sans: `0` (default).
  `label-sm` uppercase: `+0.05em`.

## Spacing

A 4px base unit. All spacing in the app — padding, margin, gap — uses a token from this
scale. If something needs 14px, the answer is either 12 or 16 — pick the one that fits the rhythm.

## Border radius

The brand leans soft. Default to `radius-xl` (16px) for cards, with nested
elements stepping down to `radius-lg` (12px). Pills (`radius-full`) for
primary CTAs.

| Token | Value | Common usage |
| --- | --- | --- |
| `radius-none` | 0 | Full-width dividers, very rare |
| `radius-sm` | 4px | Small badges |
| `radius-md` | 8px | Inputs, secondary elements |
| `radius-lg` | 12px | Nested elements inside cards (answer options, sub-cards) |
| `radius-xl` | 16px | **Default for cards and primary buttons** |
| `radius-2xl` | 24px | Hero cards, modal sheets (top corners) |
| `radius-full` | 9999px | Pills, circular buttons, avatars |

## Shadows

Mobile shadows are subtle by design. Heavy shadows feel dated and clunky on small
screens. Shadows use `black-900` at low opacity (not pure black) to stay warm and
consistent with the brand.

| Token | Value | Usage |
| --- | --- | --- |
| `shadow-sm` | `0 1px 2px rgba(26,26,26,0.05)` | Inputs, subtle separation |
| `shadow-md` | `0 2px 8px rgba(26,26,26,0.06), 0 1px 2px rgba(26,26,26,0.04)` | Default card elevation |
| `shadow-lg` | `0 8px 24px rgba(26,26,26,0.10), 0 2px 4px rgba(26,26,26,0.06)` | Modals, bottom sheets, floating elements |

## Opacity & z-index

Opacity for state feedback. Z-index for layering. Both use named tokens — no arbitrary
values.

### Opacity tokens

| Token | Value | Usage |
| --- | --- | --- |
| `opacity-disabled` | 40% | Disabled state for all interactive components |
| `opacity-overlay` | 50% | Modal backdrop, image overlays |
| `opacity-ghost` | 60% | Secondary icons, de-emphasized decorative elements |

### Z-index tokens

| Token | Value | Usage |
| --- | --- | --- |
| `z-base` | 0 | Normal document flow |
| `z-raised` | 10 | Cards that need to float above page content |
| `z-sticky` | 200 | Bottom nav, sticky headers |
| `z-overlay` | 400 | Modal backdrops |
| `z-modal` | 500 | Modals, bottom sheets, drawers |
| `z-toast` | 600 | Toasts and snackbars (above everything) |

## Navigation patterns

How navigation works at the app level. Individual screen specs reference these rules.

### Bottom nav visibility

The app has a persistent bottom nav with four destinations: **Home**,
**Topics**, **Progress**, **Settings**. Shown on the four
"home base" screens; hidden during focused flows so users can concentrate.

### Screen header rules

Every flow screen has a 56px screen header containing: back button (left-aligned, 44×44px tap target,
chevron icon) and optional screen title or right action. Headers sit flush on the page surface — no
shadow or border by default. Individual screen specs may override when content scrolls underneath.

### Back navigation

The back button always navigates to the previous screen in the flow. Device-level back gesture
(Android back, iOS swipe-from-left) follows the same path. No screen requires a "confirm exit"
dialog in V1.

### Modal navigation

Modals and bottom sheets are dismissed by: tap-outside (modals only), explicit close/Cancel button,
or device-level back gesture. Modals never trigger navigation away from the underlying screen on
dismiss.

### Mid-topic app resume

When a user closes the app mid-session and returns later, the app resumes based on where they left off:

- **Mid-question (Screen 16):** Resumes to the last visited question with progress intact. Previously selected (but not submitted) answer re-selected on mount. No toast — silent resume.
- **Mid-waiting-for-partner (Screen 17):** Returns directly to the Waiting screen. If the partner finished in the interim, the screen detects this on mount and auto-advances to Alignment Reveal (Screen 18).
- **Mid-onboarding (pre-paywall):** Resumes at the last completed onboarding step. Most common abandon point is post-quiz, pre-paywall — returns to Personalized Results (Screen 09) or Paywall directly.
- **Mid name-entry (Screen 05b):** Resumes to Screen 05b with input empty. Account creation already succeeded server-side, but name is not yet captured.
- **All other screens:** Resume to Home (Screen 12).

### Lapsed user re-entry

**Definition:** User hasn't opened the app in 14 or more days.

**Treatment:** Direct-to-Home with a soft re-engagement card on the Home screen. No dedicated welcome-back screen in V1.

**Re-engagement card spec:**

- Appears at the top of the Home scroll area, above "Up next"
- Copy references the partner by name and most recent in-progress topic: *"It's been a while — Jordan's still waiting on a couple things."*
- If no in-progress topics: *"It's been a while. Ready to pick up where you left off?"*
- CTA: "Jump back in →" → most recently visited topic intro, or Topic List if no topic in progress
- Dismissible via × icon; dismissed state persists for the session
- Trigger threshold: 14 days since last app open
- Does not show if user has 0 topics started — Empty Home nudge card takes precedence

---

# Universal Components

## Button

Buttons trigger actions. The primary way users move through the app, submit decisions,
and take next steps. Every interactive element that isn't a link, a card, or a form input should be
a button.

### Variants × sizes

Four variants. Three sizes. All buttons use `radius-full` (pill shape) — non-negotiable
for the system.

### Variant rules

| Variant | Use for | Visual treatment |
| --- | --- | --- |
| **Primary** | The single most important action on a screen | Filled `action-primary`, `text-on-brand` label |
| **Secondary** | Lower-priority actions alongside a primary | Transparent, `border-strong` outline, `text-primary` label |
| **Tertiary** | Inline actions, small navigation moments | No background, no border, `text-link` label |
| **Destructive** | Irreversible or harmful actions | Filled `status-error-text`, `text-primary` label (dark on pink — white doesn't have enough contrast) |

### Size specifications

| Size | Height | H. padding | Label style | Use for |
| --- | --- | --- | --- | --- |
| **Large** | 56px | `space-6` | `label-lg` | Primary screen CTAs |
| **Medium** | 44px | `space-5` | `label-md` | Default in-card actions, most inline |
| **Small** | 32px | `space-4` | `label-md` | Compact contexts, inside list items |

**Touch target rule:** 44px minimum for reliable tappability. Small (32px) only for
tertiary or low-mistake-cost contexts.

### States — Primary

### Full-width stacked CTA pattern

The most common button layout in the app — a primary button stacked above a secondary or tertiary
action, both full-width, at the bottom of a screen.

### Don't

- Don't use more than one primary button per screen (rare exceptions: equal-weight alternative
  actions).
- Don't use Grandstander for button labels.
- Don't remove the pill shape (`radius-full`). It's a brand-level decision.
- Don't use a destructive button without a paired Cancel action.

## Text Input

Captures free-form text. Appears in auth forms (name, email, password), onboarding quiz
open-text variant, and settings. Every interactive text field uses this component.

### Anatomy

| Element | Required? | Spec |
| --- | --- | --- |
| Label | Required | 13px DM Sans semibold, `text-primary`, NOT uppercase. 6px gap below label, above field. |
| Input field | Required | See visual spec below. |
| Helper text | Optional | 12px DM Sans regular, `text-secondary`. Gives context ("We'll never share your email"). |
| Error message | Conditional | Same size/placement as helper text, `status-error-text` (#ff9191) color. Replaces helper text when active. |

### Visual specification — field

| Property | Value |
| --- | --- |
| Background | `surface-card` (white) — always white, regardless of page context. Cream input on cream page disappears. |
| Border — default | `1.5px solid border-default` |
| Border — focused | `1.5px solid border-focus` (purple-500) + `0 0 0 3px rgba(95,69,242,0.12)` focus ring |
| Border — error | `1.5px solid border-error` (pink-400) |
| Border radius | `radius-md` (8px) |
| Padding | 11px vertical · 14px horizontal |
| Font | 15px DM Sans regular (`body-md`) |
| Placeholder color | `text-tertiary` |
| Disabled | opacity 0.42 · background `rgba(26,26,26,0.04)` · cursor: not-allowed |

### States

### Behavior rules

- Label always sits above the field — no floating label pattern. On mobile with the keyboard up, a
  disappearing label is disorienting.
- Error state triggers on blur (user leaves the field), not while typing. Exception: clear the
  error as they correct it.
- Input type attribute must match content: `type="email"`,
  `type="password"`, `type="text"`. This triggers the correct mobile
  keyboard.
- Auto-capitalize off for email and password. On for name fields.
- Password fields: show/hide eye icon right-aligned inside field, 44×44px tap target.

### Don't

- Don't use floating labels.
- Don't show errors while the user is actively typing — wait for blur.
- Don't use `surface-nested` (cream) for the input background. White on cream is the
  pattern.

## Divider

Horizontal rule that separates distinct content sections. Used between form groups in
auth screens, between major page sections on Home and Progress, and as an "or" separator before
social auth buttons.

### Variants

| Variant | Usage |
| --- | --- |
| Default | Between major sections — Home, Progress, auth forms, Topic List categories |
| With label ("or") | Auth screens only — between primary form submit and social auth buttons (Screens 02, 03) |

### Visual specification

| Property | Value |
| --- | --- |
| Line | 1px solid `border-default` — `rgba(26,26,26,0.15)` |
| Vertical margin | `space-6` (24px) above and below — matches the section spacing rhythm |
| Width | Full content width (edge-to-edge within parent's horizontal padding) |
| Label text | 12px DM Sans medium, `text-tertiary`, centered between two line segments |
| Label gap | `space-3` (12px) between text and line on each side |

### Visual

### Rules

- Only divide semantically distinct sections — the spacing scale handles most separation. Dividers
  are for section-level breaks only.
- The "or" labeled variant is exclusively for the auth screen social auth separator. Don't
  repurpose it elsewhere.
- Dividers don't appear inside cards. Use spacing tokens for intra-card separation.

## Progress Bar

Linear fill indicator showing completion. Three contexts in V1: onboarding quiz step
indicator, within-topic question progress, and overall plan progress on Home, Topic List, and
Progress screens.

### Variants

| Variant | Usage | Label? |
| --- | --- | --- |
| Bare | Within-topic question progress (Screen 13) — minimal, no label distraction mid-flow | None |
| Labeled | Plan overview on Home, Topic List, Progress — context matters here | Count row above |
| Category row | Progress screen (Screen 18) — category name + count + bar as a unit | Name left, count right |

### Visual specification

| Property | Value |
| --- | --- |
| Track height | 6px |
| Track color | `rgba(26,26,26,0.10)` on cream · `rgba(26,26,26,0.08)` inside white cards |
| Fill color | `action-primary` (purple-500) |
| Border radius | `radius-full` — both track and fill |
| Fill animation | width 0.4s ease on mount and value change |
| Count label | 12px DM Sans regular, `text-secondary` |
| Category label | 13px DM Sans medium, `text-primary` |

### Visual

### Rules

- Don't use percentages as the primary label — "8 of 23 topics" is more meaningful than "35%".
  Exception: the alignment score on Progress screen uses 72% because it's a score, not a count.
- At 0%, show the empty track with no fill. The track alone communicates "this is a progress
  indicator that hasn't started."

## Badge / Status Pill

Small inline labels communicating status, category membership, count, or alignment
state. Single component covering category filters, topic status, alignment reveal states, and count
badges across many screens.

### Variant family

| Variant | Usage | Style |
| --- | --- | --- |
| Category — unselected | Category filter pills, Personalized Results (08) | Outlined · border-strong · text-secondary |
| Category — selected | Active category filter | Filled purple-500 · white text |
| Status: Your turn | Topic awaiting user's answers — highest priority | Filled purple-500 · white |
| Status: Waiting | User answered; waiting for partner | Neutral gray fill · text-secondary |
| Status: Complete | Both answered, reveal done | Green soft fill · dark green text |
| Status: Locked | Paywall or partner action required first | Subtle gray · text-tertiary |
| Alignment: Fully aligned | Reveal screen — best outcome | Green soft fill |
| Alignment: Mostly aligned | Reveal screen — good outcome | Yellow soft fill |
| Alignment: Worth a conversation | Reveal screen — needs discussion | Orange soft fill |
| Count badge | Topic count on category headers ("5 topics") | Neutral gray pill |

### Visual specification

| Property | Value |
| --- | --- |
| Padding | 4px vertical · 10px horizontal |
| Border radius | `radius-full` (9999px) — always pill-shaped |
| Font | 12px DM Sans semibold (weight-600) · sentence case. NOT uppercase. |
| Height | ~24px |
| Outlined border | `1.5px solid border-strong` |

### Visual — all variants

### Soft fill color values

| Variant | Background | Text color |
| --- | --- | --- |
| Complete / Fully aligned | `rgba(119,234,175,0.28–0.30)` | `status-success-text` (#157a46) |
| Mostly aligned | `rgba(255,215,85,0.38)` | `#8a6800` — hardcoded dark yellow |
| Worth a conversation | `rgba(255,173,108,0.30)` | `#9a5500` — hardcoded dark orange |
| Waiting | `rgba(26,26,26,0.07)` | `text-secondary` |
| Locked | `rgba(26,26,26,0.06)` | `text-tertiary` |

### Rules

- Always `radius-full`. Never a rectangular badge for this component.
- Status pills are sentence case — "Your turn", not "YOUR TURN".
- Alignment pills always include their emoji. It's load-bearing for quick scanning on the reveal
  screen.
- Maximum one status pill per topic row. Priority order: Your turn > Waiting > Complete >
  Locked.
- **Category name encoding (data layer fix):** Category names containing `&` — specifically "Pregnancy & Birth" and "Health & Development" on Screens 08 (Personalized Results) and 13 (Topic List) — must be stored and rendered as literal `&`, not the HTML entity `&amp;`. The `&amp;` string was observed rendering in the designed screens source; fix in the data layer before build so it never reaches the UI. Do not HTML-encode display strings in the data layer.

## Avatar

Circular user representation. Appears on the Home greeting row, Settings partner row,
and the Waiting screen. Conveys who's who in the couple without a name taking up space.

### Sizes

| Token | Diameter | Font size | Usage |
| --- | --- | --- | --- |
| `avatar-sm` | 24px | 9px | Tight inline contexts (rare) |
| `avatar-md` | 32px | 12px | Settings partner row · compact contexts |
| `avatar-lg` | 40px | 14px | Home greeting row — primary size |
| `avatar-xl` | 48px | 17px | Waiting screen · profile-prominent moments |

### States

| State | Appearance | When |
| --- | --- | --- |
| Initials (default) | purple-500 @ 14% opacity background · purple-600 text · DM Sans bold | Account exists, no profile photo (V1 only has this state) |
| Image | Circular crop of profile photo | V2 — not in V1 scope |
| Pending / unlinked | 2px dashed `border-strong` · transparent background · "?" in `text-tertiary` | Partner hasn't accepted invite yet |

### Visual

### Rules

- Initials from display name: "Sarah" → "S" · "Sarah Jones" → "SJ". One character is fine.
- Both partners use the same purple tint in V1. No per-user color. The name and context
  distinguish them.
- The pending "?" is the only time a non-initial character appears.
- Avatar is not interactive in V1 — don't wrap in a pressable element unless it links somewhere.

## Toggle / Switch

Binary on/off control. Appears exclusively in Settings (Screen 19) for notification and
pacing preferences. Always used inside a List Row — never standalone.

### Visual specification

| Property | Value |
| --- | --- |
| Track dimensions | 44px × 26px |
| Track — on | `action-primary` (purple-500) |
| Track — off | `rgba(26,26,26,0.18)` — neutral gray |
| Thumb | 20px diameter · white · 3px inset from track edge |
| Thumb shadow | `0 1px 3px rgba(0,0,0,0.20)` |
| Transition | Track color + thumb position · 0.2s ease |
| Tap target | Full list row width × height — not just the toggle element |

### Visual

### Rules

- Toggle is always right-aligned in its row. Label left, toggle right — matches iOS/Android system
  settings.
- State change is immediate on tap — no confirmation dialog for V1 settings toggles.
- Toggle is never standalone — it always lives inside a List Row with a label.

## List Row

Standard row pattern for settings and structured navigation lists. Covers the entire
Settings screen (Screen 19) and topic list rows (Screen 11). Groups of rows live inside white card
containers with section headers above them.

### Variants

| Variant | Right element | Usage |
| --- | --- | --- |
| Default (value + chevron) | Value text + "›" | Settings rows with a destination (email, due date, nudge frequency) |
| Toggle row | Toggle component | Settings boolean preferences |
| With avatar | Avatar (md) left-leading, label, chevron right | Partner row in Settings |
| Destructive | None | Log out — label uses `status-error-text` |
| Section header | None — standalone label above a card group | Group label ("Notifications", "Pacing", etc.) |

### Visual specification — row

| Property | Value |
| --- | --- |
| Background | `surface-card` (white) |
| Min height | 52px |
| Padding | 13px vertical · 16px horizontal |
| Row separator | 1px solid `rgba(26,26,26,0.06)` — top border on each row except first |
| Label | 15px DM Sans regular · `text-primary` |
| Value text | 13.5px DM Sans regular · `text-secondary` |
| Chevron | "›" · 14px · `text-tertiary` |
| Destructive label | `status-error-text` (#ff9191) |
| Pressed state | Background: `rgba(26,26,26,0.04)` |
| Card container radius | `radius-xl` (16px) |
| Card container shadow | `shadow-md` |

### Visual specification — section header

| Property | Value |
| --- | --- |
| Font | 11.5px DM Sans semibold · ALL CAPS · letter-spacing +0.06em · `text-secondary` |
| Padding | 13px horizontal · 13px top · 5px bottom |
| Position | Outside the card container, immediately above it — not a row inside the card |

### Visual

### Rules

- Group related rows in a single card. Don't mix categories in one card.
- Section headers live above the card, outside it — they label the group, not a row inside it.
- Chevron ("›") appears only when tapping navigates or opens something. Toggle rows and
  destructive rows have no chevron.
- Each row's tap target is full width × height, minimum 44px tall.

### Don't

- Don't use list rows for question answer choices — that's the Question Card component.
- Don't show a chevron unless tapping is navigable.
- Don't use a red destructive label — use `status-error-text` (pink-400) to stay on-brand.

## Select / Date Picker

Trigger-based inputs that open a native OS picker sheet. Used in onboarding (life stage dropdown, due date) and settings (nudge frequency, guided timeline). We design the trigger element — the OS handles the picker sheet itself.

### Variants

| Variant | Trigger displays | OS picker type | Screens |
| --- | --- | --- | --- |
| Select | Selected option label, or placeholder | Scroll wheel — discrete list of options | 07 (life stage, guided timeline), 24 (nudge frequency) |
| Date Picker | Formatted date string (e.g. "March 15, 2025"), or placeholder | Scroll wheel — month / day / year columns | 07 (due date), 24 (due date revisit) |

### Anatomy — trigger element

| Element | Required? | Spec |
| --- | --- | --- |
| Label | Required | 13px DM Sans semibold, `text-primary`. 6px gap below, same as Text Input. |
| Trigger field | Required | Full-width tappable surface. Matches Text Input dimensions. See visual spec below. |
| Value / placeholder | Required | Left-aligned inside field. Placeholder uses `text-tertiary`; selected value uses `text-primary`. |
| Chevron icon | Required | 16px, `text-secondary`, right-aligned. Points down — signals picker, not free-text. |
| Helper text | Optional | 12px DM Sans regular, `text-secondary`. Same placement as Text Input. |

### Visual specification — trigger field

| Property | Value |
| --- | --- |
| Background | `surface-card` (white) |
| Border — default | `1.5px solid border-default` |
| Border — open / active | `1.5px solid border-focus` (purple-500) |
| Border radius | `radius-md` (8px) |
| Padding | 11px vertical · 14px horizontal |
| Height | 46px — matches Text Input |
| Font | 15px DM Sans regular (`body-md`) |
| Disabled | opacity 0.42 · background `rgba(26,26,26,0.04)` · cursor: not-allowed |

### States

| State | Trigger appearance | Notes |
| --- | --- | --- |
| Default (empty) | Default border, placeholder text, chevron | No value selected yet |
| Open | `border-focus` purple border on trigger | OS sheet is visible. Trigger stays visible behind the sheet. |
| Filled | Default border, value text in `text-primary`, chevron | User has confirmed a selection |
| Disabled | Reduced opacity, no interaction | Use only when field is conditionally unavailable (e.g. due date field hidden if not pregnant) |

### Behavior rules

- The trigger is the only designed surface. The OS picker sheet (scroll wheel, confirm/cancel buttons) is entirely native — do not attempt to restyle it.
- Tapping the trigger immediately opens the OS picker — there is no focused-but-not-open state.
- The selected value does not commit until the user taps the native "Done" / "Confirm" button. If the user dismisses without confirming, the trigger reverts to its previous state.
- Due date field: conditionally rendered. Only shown after a "pregnant" life stage selection in onboarding. Hidden otherwise — don't disable it, remove it from the DOM.
- Label always sits above — same rule as Text Input. No inline labels.

### Don't

- Don't build a custom dropdown or popover. The native OS picker is faster, more accessible, and expected by mobile users.
- Don't use a Text Input for fields that have a constrained option set. If the answer is a pick from a list, it's a Select.
- Don't omit the chevron. Without it, the field looks like a disabled Text Input.

## Slider

A 1–5 graduated scale for question variants that need a numeric or intensity response. An alternative answer format to multiple-choice — same question card template, different answer region. Scale ends are labeled "Strongly disagree" and "Strongly agree".

### Context

The Slider replaces the answer options area inside the Question Card. The question card container, header region (counter + progress bar), and action region (Continue + Skip) remain identical to the multiple-choice variant.

### Visual specification

| Property | Value |
| --- | --- |
| Scale | 1 to 5, discrete integer steps |
| Track height | 6px — matches Progress Bar track |
| Track color | `rgba(26,26,26,0.10)` |
| Fill color | `action-primary` (purple-500) — fills from left to current value |
| Track border radius | `radius-full` |
| Thumb diameter | 28px |
| Thumb color | `surface-card` (white) |
| Thumb border | `2px solid action-primary` (purple-500) |
| Thumb shadow | `shadow-sm` |
| Step markers | 5 small tick marks (2px × 8px, `rgba(26,26,26,0.15)`) centered on the track at each integer position |
| Value label | Current integer shown above thumb, 15px DM Sans semibold, `text-primary` |
| End labels | "Strongly disagree" (left) / "Strongly agree" (right) · 12px DM Sans regular, `text-secondary`, 10px below track |
| Touch target | 44px height around track — full-width drag zone, not just thumb |
| Snap animation | thumb snaps to nearest integer on release · `left 0.15s ease` |

### Default state

On first render, no value is selected — thumb sits at the midpoint (position 3) but is visually distinct from a confirmed selection: thumb border uses `border-default` rather than `action-primary`, and the fill is absent. The Continue button remains disabled until the user drags or taps to set a value.

### Interaction

| Gesture | Behaviour |
| --- | --- |
| Drag thumb | Follows finger continuously, snaps to nearest integer on release |
| Tap on track | Thumb jumps to tapped position (nearest integer), immediately counts as a selection |
| First interaction | Thumb border switches to `action-primary`, fill appears, Continue button enables |

### Behavior rules

- The same "no auto-advance" rule applies here as in the multiple-choice Question Card. Setting a value never auto-advances — user must tap Continue.
- The full track width is a valid touch target — users should be able to tap anywhere on the track row to set a value, not just drag the thumb.
- Selection persists if the user navigates away and returns, same as other question types.
- The value label above the thumb only appears once a value is confirmed (first interaction). Don't show "3" hovering above an unset default position.

### Don't

- Don't use a continuous (non-snapping) slider. All values are integers 1–5.
- Don't show percentage or raw fraction labels on the track. End labels only.
- Don't auto-advance on slider interaction — same rule as multiple choice.
- Don't use the slider for questions with more than 5 meaningful positions — use multiple choice instead.

---

# Navigation

## Bottom nav

Persistent access to the four primary destinations. Visibility rules in the navigation
patterns section above.

### Visual

### Destinations (fixed order)

| Position | Destination | Screen # | Active tab |
| --- | --- | --- | --- |
| 1 | Home | 10 | When on Screen 10 |
| 2 | Topics | 11 | When on Screen 11 |
| 3 | Progress | 18 | When on Screen 18 |
| 4 | Settings | 19 | When on Screen 19 |

### Visual specification

| Property | Value |
| --- | --- |
| Height | 64px (+ bottom safe-area inset) |
| Background | `surface-card` (white) |
| Top border | `1px solid border-default` |
| Position | Fixed to bottom of viewport |
| z-index | `z-sticky` (200) |
| Tab layout | Vertical stack: icon on top, label below |
| Icon size | 24×24px |
| Label style | `label-sm` 11px DM Sans medium — NOT uppercase here |
| Active color | `action-primary` (purple-500) for both icon and label |
| Inactive color | `text-secondary` for both icon and label |

### Rules

- Tab order never changes — position is fixed. Users develop muscle memory.
- No badges or notification dots in V1.
- The nav is capped at four tabs. No overflow "More" option — ever.
- Tapping the active tab scrolls the destination back to top (standard iOS pattern).

### Don't

- Don't add a fifth tab.
- Don't reorder tabs based on usage frequency.
- Don't use a heavy active state (background fill, underline). Color shift is the signal.
- Don't show the bottom nav on this screen.

## Screen Header

The top chrome present on every flow screen (below the device status bar). Contains a
back button, an optional title, and an optional right action. Defined informally in navigation
patterns — this is the formal component spec.

### Anatomy

| Element | Required? | Spec |
| --- | --- | --- |
| Back button | Conditional | Left-aligned · 44×44px tap target · chevron icon ("‹") · `text-primary` · not present on screens with no logical "back" (Splash, Home base screens) |
| Screen title | Optional | 17px DM Sans bold · `text-primary` · centered · visually centered against the back button by adding equal right offset. Omitted when body content carries the title (Screen 12, Screen 15). |
| Right action | Optional | Right-aligned · 44×44px tap target · Tertiary button or icon · used for "Skip", "Save", or contextual actions |

### Visual specification

| Property | Value |
| --- | --- |
| Height | 56px |
| Background | `surface-page` (cream) by default — matches the screen's page background. Screens on a white surface use `surface-card`. |
| Border/shadow (default) | None — sits flush on the page surface |
| Border (scrolled) | `1px solid border-default` on bottom — applied when content has scrolled beneath the header |
| Horizontal padding | 4px · back button and right action each have their own 44×44px target, providing optical alignment |

### Variants (by content)

### Screen-by-screen reference

| Screen | # | Back? | Title? | Right action? |
| --- | --- | --- | --- | --- |
| Sign Up | 02 | No (entry point) | None | None |
| Log In | 03 | No (entry point) | None | None |
| Partner Linking | 04 | Yes → Sign Up | None | None |
| Onboarding Intro–Quiz | 05–06 | Yes | None | "Skip" (tertiary) |
| Topic Intro | 12 | Yes → Topic List | None (topic title carries it) | None |
| Question | 13 | Yes → Topic Intro | None | None |
| Waiting for Partner | 14 | Yes → Home | None | None |
| Alignment Reveal | 15 | No (flow terminus) | None | None |
| Post-Reveal | 16 | No | None | None |
| Prediction Card | 17 | Yes | None | None |

### Don't

- Don't add a shadow to the header by default — the scrolled border is the only separation needed.
- Don't center the back button visually — it must be left-aligned.
- Don't use the screen header on home-base screens (Home, Topics, Progress, Settings) — those use
  the bottom nav and page-level titles.

---

# Feedback & Overlays

## Toast / Snackbar

Brief system-level feedback that appears at the bottom of the screen and auto-dismisses.
Not for complex decisions — for simple confirmations, nudge feedback, and errors that resolve
themselves.

### Variants

| Variant | Usage | Example |
| --- | --- | --- |
| Info (default) | Neutral system messages | "Nudge sent to Jordan 👉" |
| Success | Confirming a completed action | "Topic marked as resolved ✓" |
| Error | Something failed; user may need to retry | "Couldn't save your answer. Try again." |
| Warning | Something needs attention; not a failure | "Your partner hasn't joined yet." |

### Visual specification

| Property | Value |
| --- | --- |
| Background | Dark fills — keeps toasts distinct from the cream/white page surface so they pop at a glance. See color table below. |
| Border radius | `radius-xl` (16px) |
| Padding | 14px vertical · 16px horizontal |
| Max width | 343px (375px screen − 16px each side) |
| Shadow | `shadow-lg` |
| Position | Fixed · horizontally centered · 16px above bottom nav (or 16px above safe-area inset when nav is hidden) |
| z-index | `z-toast` (600) — above everything |
| Auto-dismiss | 3 seconds · swipe down to dismiss early |
| Optional action | Right-aligned text link — white, bold, 13px. Use sparingly ("Undo", "Retry"). One action maximum. |

### Color values

| Variant | Background | Text |
| --- | --- | --- |
| Info | `#1a1a1a` (black-900) | White |
| Success | `#1a4d35` (dark green — hardcoded) | White |
| Error | `#5a1a1a` (dark red — hardcoded) | White |
| Warning | `#4d2e00` (dark amber — hardcoded) | White |

Dark backgrounds for all toast variants — not the soft accent tints. On a
cream/white page, a soft green toast would read as a card, not an alert. Dark is the contrast
signal.

### Visual

### Rules

- One toast at a time. If a new one triggers while one is showing, the first dismisses immediately
  and the new one appears.
- Only use toasts for transient feedback — not for actions that require a decision. Use a modal
  for that.
- The optional action should be a single word or short phrase ("Undo", "Retry", "View"). Never a
  full sentence.
- Toasts are not accessible as standalone alerts — critical errors that require user action belong
  in a modal, not a toast.

## Modal / Dialog

Interrupts the current flow to present a decision or important information. Used when
the action is significant enough that the user must explicitly respond before proceeding.

### When to use a modal vs. other patterns

| Use modal for | Don't use modal for |
| --- | --- |
| Confirmation of a destructive action ("Are you sure you want to delete your account?") | Simple feedback — use a toast |
| Actions requiring input before proceeding | Long-form content or multi-step flows — use a full screen |
| Blocking decisions with no safe "ignore" path | Non-urgent information — use a callout or inline message |

### Visual specification

| Property | Value |
| --- | --- |
| Backdrop | `rgba(26,26,26,0.50)` — new token `surface-overlay` · covers full viewport · z-index `z-overlay` (400) |
| Modal card background | `surface-card` (white) |
| Border radius | `radius-2xl` (24px) |
| Width | 343px (screen − 16px each side) |
| Padding | 28px top · 24px sides · 20px bottom |
| Shadow | `shadow-lg` |
| z-index | `z-modal` (500) |
| Title | 20px DM Sans bold, `text-primary`, 10px below |
| Body | `body-md` (15px), `text-secondary`, 24px below |
| Actions | Stacked column · primary action first (top) · cancel/secondary below · 8px gap |
| Dismiss | Tap backdrop · explicit Cancel button · device back gesture |
| Entry animation | Scale from 0.95 → 1.0 + fade in · 200ms ease-out |

### Visual

### Rules

- Always provide a clear exit path — either a Cancel button or dismissible backdrop. Never trap
  the user.
- The primary action in a destructive modal uses the Destructive button variant. Never a Primary
  (purple) button for a destructive action.
- Modal titles should be questions or direct statements — not vague ("Are you sure?" is fine;
  "Warning" is not).
- Maximum two actions. If more are needed, reconsider the flow — you may need a full screen
  instead.

### Don't

- Don't use modals for routine actions. Reserve them for genuinely significant decisions.
- Don't stack modals. One at a time, always.
- Don't put long-form text inside a modal. Keep body copy to 2–3 sentences maximum.

## Bottom Sheet

A panel that slides up from the bottom of the screen. Less disruptive than a modal —
used for contextual actions, supplemental inputs, and optional flows that don't require a full
screen.

### When to use a bottom sheet vs. modal

| Bottom sheet | Modal |
| --- | --- |
| Optional supplemental actions (promo code entry on paywall) | Required decisions before proceeding |
| Contextual options for a selected item | Destructive action confirmation |
| Progressive disclosure of secondary content | Blocking, can't-be-ignored decisions |

### Visual specification

| Property | Value |
| --- | --- |
| Backdrop | `surface-overlay` — same as modal (`rgba(26,26,26,0.50)`) |
| Background | `surface-card` (white) |
| Border radius | `radius-2xl` (24px) top corners only — bottom corners flush with screen edge |
| Drag handle | 40×4px · `border-default` fill · `radius-full` · centered · 12px from top edge, 20px above content |
| Padding | 12px top (handle area) · 24px sides · 28px bottom (+ safe-area inset) |
| Shadow | `shadow-lg` |
| z-index | `z-modal` (500) |
| Entry animation | Slide up from bottom · 280ms ease-out |
| Dismiss | Drag down · tap backdrop · explicit Cancel/Close button |
| Max height | 85% of viewport height. Content scrolls internally beyond that. |

### Visual

### Rules

- Always include a drag handle — it communicates dismissibility and matches platform conventions.
- Tap-backdrop dismisses the sheet unless the sheet contains a form with unsaved state — in that
  case, confirm dismiss with a brief inline warning.
- Don't use a bottom sheet for destructive confirmations. Use a modal.
- If the sheet would need to be taller than 85% of the viewport, consider a full screen instead.

## Empty State

Full-page pattern for when there's nothing to show yet. Daisy's Guide's empty states are
warm and encouraging — they match the brand's voice and turn an absence of content into a
moment of personality.

### Where it appears

| Screen | Trigger | Tone |
| --- | --- | --- |
| Partner Linking (04) | User skips without linking a partner | Friendly, encouraging — "I'll loop them in later" |
| Topic List (11) | No topics available (edge case) | Encouraging — "Your plan is loading…" |
| Home (10) | Partner hasn't joined yet (first session) | Warm nudge — "It's more fun with two." |

### Visual specification

| Property | Value |
| --- | --- |
| Layout | Centered flex column · fills available screen height · vertically centered in remaining space below the header |
| Background | `surface-page` (cream) — matches the screen it sits on |
| Illustration | 80×80px circle container · `rgba(95,69,242,0.08)` fill · icon or emoji centered inside. Topic-specific illustrations in . |
| Title | `display-md` (Grandstander 24px bold) · `text-primary` · 24px below illustration |
| Body | `body-md` (15px) · `text-secondary` · max-width 280px · 12px below title · 28px below before CTA |
| CTA | Primary button · Large · optional — not all empty states need an action |
| Horizontal padding | `space-8` (32px) each side |

### Visual

### Rules

- Empty state copy must match the brand voice — warm, friendly, encouraging, never clinical. "No partner
  linked" is the wrong tone; "I'll loop them in later" is right.
- Always give the user a way out — a CTA that moves them toward filling the empty state, or back
  to somewhere useful.
- Don't show an empty state when content is still loading — show the Loading state instead.

## Loading / Processing State

Two distinct patterns: the **processing checklist** (Screen 07 — makes
personalization feel earned) and **skeleton screens** (for any screen waiting on data).
Different contexts, different treatments.

### Pattern 1: Processing checklist

Used on Screen 07 (Building Your Plan). Makes the personalization algorithm feel real and
intentional. Shows a sequence of steps completing in order.

| Property | Value |
| --- | --- |
| Step states | Done (faded, check icon) · Active (full opacity, spinner) · Pending (heavily faded, empty circle) |
| Step card | `surface-card` (white) · `radius-lg` (12px) · `shadow-sm` · 14px text |
| Step timing | Each step "completes" after ~700ms before the next becomes active. Total sequence: ~2–3 seconds. |
| Done icon | "✓" · `status-success-surface` color |
| Active icon | Spinner — same as Button loading state (white replaced by purple-500) |
| Pending icon | "○" · `text-tertiary` |
| Layout | Centered on page · max-width 300px · steps stacked with 10px gap |

### Pattern 2: Skeleton screen

Used any time a screen is waiting on an async data load (e.g. topic list loading, progress screen
fetching data). Replaces content with shimmer-animated placeholders that match the approximate
layout of what will appear.

| Property | Value |
| --- | --- |
| Skeleton lines | Rounded rectangles (`radius-sm`) · varying widths to mimic real content (100%, 75%, 60%, etc.) |
| Animation | Shimmer — gradient sweeps left to right · 1.6s ease-in-out · infinite |
| Color | `rgba(26,26,26,0.06)` base → `rgba(26,26,26,0.12)` at shimmer peak |
| Height | Matches approximate content: 14px for body text · 20px for headings · 6px for progress bars · use actual component shapes for cards |

### Rules

- Never show a blank screen — always show either a skeleton or the processing checklist while
  waiting. Blank feels broken.
- Skeleton layouts should approximate the real content structure. Don't show 3 skeleton lines if 8
  items will load.
- The processing checklist is only for the Building Your Plan screen (Screen 07). All other
  loading states use skeletons.
- If data loads in under 200ms, skip the skeleton — showing it briefly creates a flash that feels
  worse than nothing.

---

# App-specific Components

## Topic Card

The primary navigation element for browsing and selecting topics. Appears on the Home
screen ("Up next" callout) and the Topic List (Screen 11). Has four distinct states that communicate
where each topic stands in the couple's flow.

### States

| State | Meaning | Left border | Opacity | Status pill |
| --- | --- | --- | --- | --- |
| **Available** | Neither partner has answered yet. Ready to start. | None | 100% | None |
| **Your turn** | Partner has answered; user hasn't yet. Highest priority. | `action-primary` (3px) | 100% | "Your turn" pill |
| **Waiting** | User answered; partner hasn't yet. | `border-strong` (3px) | 100% | "Waiting on [name]" pill |
| **Complete** | Both answered, reveal done. | `status-success-surface` (3px) | 100% | "✓ Complete" pill |
| **Locked** | Paywall or partner action required before this is accessible. | None | 55% | "🔒 Locked" pill |

### Visual specification

| Property | Value |
| --- | --- |
| Background | `surface-card` (white) |
| Border radius | `radius-xl` (16px) |
| Shadow | `shadow-md` |
| Padding | `space-4` (16px) |
| Left border | 3px solid · state-dependent color (see table above) · applied via `border-left` property, not a separate element |
| Icon | Topic emoji · 28px · left-aligned · 40px container width for consistent alignment |
| Title | 15px DM Sans bold · `text-primary` |
| Description | 13px DM Sans regular · `text-secondary` · 1-2 lines · truncate with ellipsis at 2 lines |
| Status pill | Sits below description · uses Badge/Pill component |
| Tap target | Full card · pressing navigates to Topic Intro (Screen 12), except Locked state which is non-interactive |

### Visual — all states

### Rules

- Left border is 3px — thick enough to be visible at a glance, not so thick it dominates. Don't
  increase it.
- The icon is always an emoji in V1. Topic illustrations (Hero Image Card) are for the Topic Intro
  screen, not the list card.
- Locked cards are non-interactive — no tap animation, no navigation. Cursor default.
- Description truncates at 2 lines with ellipsis. Don't let it wrap to 3+ lines in the list view.

## Question card

The primary interaction surface of the app. Users encounter it on every question in
every topic. Users see it dozens of times per session — brand personality must come through here.

### States

### Anatomy

A question moment consists of three structural regions on screen:

1. **Header region** (above card) — question counter + progress bar
2. **Question card** (white surface) — question text + answer options
3. **Action region** (below card) — Continue button + skip option

### Question card container

| Property | Value |
| --- | --- |
| Background | `surface-card` (white) |
| Border radius | `radius-xl` (16px) |
| Shadow | `shadow-md` |
| Padding | `space-6` (24px) all sides |
| Width | Full width with `space-4` horizontal margin from screen edges |

### Answer options

| Property | Default | Selected |
| --- | --- | --- |
| Background | `surface-nested` (cream-50) | `action-primary` (purple-500) |
| Text color | `text-primary` | `text-on-brand` |
| Border radius | `radius-lg` (12px) | |
| Padding | `space-4` vertical · `space-5` horizontal | |
| Min height | 56px | |
| Gap between options | `space-2` (8px) | |

Single-select. 150ms ease for color change. `scale(0.98)` on press for tactile feedback.

### Behavior rules

- **Tapping an answer never auto-advances.** User must explicitly tap Continue.
  Daisy's Guide is about considered decisions, not speed.
- **Tapping Skip skips without saving an answer.** Question can be returned to later.
- **Selection persists if user navigates away and returns.**

### Don't

- Don't use Grandstander for answer option text.
- Don't auto-advance after answer selection.
- Don't add icons to answer options.
- Don't show more than 6 answer options.
- Don't put question text in ALL CAPS.

## Reveal Box

The signature component of the app. Shows both partners' answers side by side
immediately after the alignment reveal animation plays. The visual comparison is the core mechanic —
the layout must make the contrast (or agreement) land instantly.

### Anatomy

The Reveal Box is always used as a pair — two boxes, side by side, inside a flex row with a 10px gap.
They are never shown individually.

| Element | Spec |
| --- | --- |
| Owner label | "You said" / "[Partner name] said" · 11px DM Sans bold · ALL CAPS · letter-spacing +0.5px · `text-secondary` · 8px below |
| Answer text | `body-sm` equivalent: 14px DM Sans regular · `text-primary` · line-height 1.5 |

### Visual specification — each box

| Property | Value |
| --- | --- |
| Background | `surface-card` (white) |
| Border | `1.5px solid border-default` |
| Border radius | `radius-lg` (12px) |
| Padding | 14px |
| Min height | 100px — ensures boxes are comparable height even with short answers |
| Width | `flex: 1` — equal width, side by side |
| Gap between boxes | 10px |

### Entry animation

Before answers are revealed, a brief anticipation animation plays (handled at the screen level, not
this component). The boxes start hidden and fade + scale in (200ms ease-out) after the animation
completes. Both boxes animate in simultaneously.

### Visual

### Rules

- Always paired — left box is always "You said", right box is always the partner. Never invert
  this order.
- Answer text is the user's actual verbatim answer selection — not paraphrased or summarized. What
  they tapped is what appears.
- Min height keeps the boxes comparable in size even when answer lengths differ. Don't remove it.
- The AI Summary Card always follows the Reveal Box — never show the Reveal Box without it on
  Screen 15.

## AI Summary Card

The AI-generated couples summary that follows the Reveal Box on Screen 15. Visually
distinct from regular white cards — the dashed border signals "this is generated, not authored."
Always paired with the Reveal Box above it.

### Visual specification

| Property | Value |
| --- | --- |
| Border | `1.5px dashed border-strong` — dashed treatment is load-bearing; it signals AI-generated content |
| Border radius | `radius-lg` (12px) |
| Background | `rgba(26,26,26,0.02)` — barely-there tint to distinguish from pure white cards |
| Padding | 16px |
| Shadow | None |
| Label | "✨ AI summary" · 11px DM Sans bold · ALL CAPS · letter-spacing +0.5px · `text-secondary` · 8px below |
| Body text | 14px DM Sans regular · `text-primary` · line-height 1.6 |
| Spacing above | `space-3` (12px) — sits close to the Reveal Box it describes |

### Visual

### Rules

- The dashed border is non-negotiable — it's the visual signal that this content is AI-generated,
  not user-entered or app-authored.
- The "✨" emoji in the label is part of the spec. Don't replace it with a different icon.
- AI summary copy should be warm, specific, and actionable. Never generic ("You two have different
  views"). This is a content constraint, not a component constraint — but worth noting here.
- Always follows the Reveal Box. Never appears without context above it.

## Prediction Card Header

A special treatment that sits above the question card on Screen 17, signaling that this
question is a prediction — not a regular topic question. Creates a "sealed envelope" feeling that
makes the mechanic feel meaningful.

### Visual specification

| Property | Value |
| --- | --- |
| Border | `2px dashed rgba(26,26,26,0.20)` — dashed, slightly heavier than AI Summary Card |
| Border radius | `radius-lg` (12px) |
| Background | `rgba(26,26,26,0.03)` |
| Padding | 12px 16px |
| Layout | Centered text |
| Primary label | "🔮 Prediction card" · 11px DM Sans bold · ALL CAPS · letter-spacing +0.5px · `text-secondary` |
| Sub-label | "You'll revisit this after baby arrives" · 12px DM Sans regular · `text-tertiary` · 3px below primary label |
| Spacing below | 16px — before the question card begins |

### Visual

### States

The Prediction Card Header has three distinct visual states corresponding to the lifecycle of a prediction question.

#### Answering state (default)
The user has not yet submitted their answer.

| Property | Value |
| --- | --- |
| Border | `2px dashed rgba(26,26,26,0.20)` |
| Background | `rgba(26,26,26,0.03)` |
| Sub-label | "Sealed until after baby arrives" · `text-tertiary` |
| Question card | Rendered below with answer options |
| CTA | "Lock in my prediction →" · disabled until option selected |

#### Locked state (post-submission, awaiting milestone)
The user has submitted. The answer is sealed. The milestone date is in the future.

| Property | Value |
| --- | --- |
| Border | `2px solid rgba(26,26,26,0.25)` — solid, slightly stronger than dashed answering state |
| Background | `rgba(26,26,26,0.03)` |
| Sub-label | "Sealed until after baby arrives" · `text-tertiary` |
| Question card | Replaced by a sealed card: 🔒 icon, "Your prediction is sealed." heading (Grandstander 18px), body copy confirming the reveal date, inline pill showing the reveal date |
| CTA | "Back to topics" · enabled |
| Visual intent | The shift from dashed to solid border communicates permanence — the envelope is sealed |

#### Reveal-ready state (milestone reached)
The milestone date has passed. Both partners' answers are available to open.

| Property | Value |
| --- | --- |
| Border | `2px solid purple-500 (#5f45f2)` — purple, active signal |
| Background | `rgba(95,69,242,0.05)` — subtle purple tint |
| Sub-label | "The moment has arrived 🎉" · `text-secondary` |
| Question card | Sealed card with 🔮 icon, "Time to find out." heading, body confirming the milestone was hit |
| CTA | "See your predictions →" · enabled · full weight · triggers reveal animation |
| Visual intent | Purple border and tint makes the card feel activated — it's the only state where the header has a color treatment |

### Rules

- This header is exclusively for prediction questions — don't use it on regular topic questions.
- The three states are mutually exclusive. Never show the dashed-border answering state after submission.
- The reveal-ready state is triggered by the data layer detecting the milestone date has passed — never by user action alone.
- Push notification is sent to both partners when reveal-ready state activates.

## Partner Status Block

Compact inline display of a partner's avatar, name, and activity status. Appears on the
Home screen (partner status section) and the Waiting for Partner screen (Screen 14). Gives the user
a sense of their partner's presence without requiring real-time push.

### States

| State | Status text | When |
| --- | --- | --- |
| Active recently | "[Name] · last active 2h ago" | Partner has used the app within the last 24 hours |
| Waiting (answering) | "[Name] is answering now..." | Partner is actively in the same topic flow |
| Pending invite | "Invite pending · hasn't joined yet" | Partner hasn't created an account yet |

### Visual specification

| Property | Value |
| --- | --- |
| Layout | Flex row · avatar left · text block middle · optional action right |
| Background | `surface-card` (white) |
| Border radius | `radius-lg` (12px) |
| Shadow | `shadow-sm` |
| Padding | 14px 16px |
| Avatar | `avatar-md` (32px) · initials or pending state |
| Name style | 14px DM Sans bold · `text-primary` |
| Status style | 12px DM Sans regular · `text-secondary` |

### Visual

## Stats Row

A three-column metric display using large Grandstander numbers. Used on the Personalized
Results screen (08), the Progress screen (18), and referenced in Screen 12. The data display
workhorse for "big numbers at a glance."

### Visual specification

| Property | Value |
| --- | --- |
| Layout | Three equal-width columns · flex row · full content width |
| Column divider | `1px solid border-default` · right border on each column except last |
| Number style | Grandstander 32px bold · `text-primary` · letter-spacing `-0.02em` · line-height 1.1 |
| Label style | 11px DM Sans medium · ALL CAPS · letter-spacing `+0.5px` · `text-secondary` · 4px below number |
| Alignment | Text centered within each column |
| Vertical padding | `space-2` (8px) top and bottom per cell |

### Visual

### Rules

- Always three columns. Don't use this component for two-column data — use the Stats Card (2-col)
  instead.
- Numbers can include units inline: "~8wk", "72%", "~3". Keep them short — if the number + unit
  exceeds 5 characters it starts to crowd.
- Labels are ALL CAPS (`label-sm` treatment). This is one of the few places outside of
  section headers where ALL CAPS is used.

## Stats Card

A two-column stat display used inside the Topic Intro screen (Screen 12) to show
question count and estimated time. Formally specced here; referenced in the Screen 12 spec as a
sub-component.

This component is a sub-card — it sits inside a screen's content area rather than
directly on the cream page. It uses `radius-lg` (12px) rather than the default
`radius-xl` (16px) to signal the nested relationship.

### Visual specification

| Property | Value |
| --- | --- |
| Background | `surface-card` (white) |
| Border radius | `radius-lg` (12px) — stepped down from card default since it's nested inside a screen |
| Shadow | None — white background against cream page provides sufficient separation |
| Padding | `space-4` (16px) all sides |
| Layout | Two equal columns · divided by `1px solid border-default` vertical line |
| Number style | Grandstander 28px bold · `text-primary` · line-height 1.1 |
| Label style | 11px DM Sans medium · ALL CAPS · letter-spacing `+0.5px` · `text-secondary` · 4px below number |
| Spacing below | `space-6` (24px) |

### Visual

### Rules

- Always exactly two columns. For three-column data use Stats Row.
- This component is contextual to the Topic Intro screen — don't repurpose it elsewhere without
  reconsidering whether Stats Row is a better fit.

## Hero Image Card

The illustration container on the Topic Intro screen (Screen 12). A 160px-tall white
card that houses each topic's SVG or PNG illustration. Formally specced here; referenced in the
Screen 12 spec.

### Visual specification

| Property | Value |
| --- | --- |
| Height | 160px — fixed |
| Width | Full content width (screen width minus `space-4` horizontal margin each side) |
| Background | `surface-card` (white) |
| Border radius | `radius-xl` (16px) |
| Shadow | None — white-on-cream contrast provides the separation |
| Spacing below | `space-6` (24px) |
| Illustration sizing | Illustration asset centered within the 160px height · internal padding `space-4` (16px) all sides · SVG or PNG |
| V1 placeholder | When topic illustration is not yet available: centered topic emoji at 48px, `text-tertiary` color |

### Visual

### Rules

- Height is fixed at 160px. Don't let illustrations overflow — clip with
  `overflow: hidden`.
- Never put text inside the hero image card.
- The card has no shadow — the white-on-cream contrast is the visual anchor. Don't add one.

## Feature Promise Card

Icon + title + body cards used on the Onboarding Intro screen (Screen 05) to build trust
before the quiz. Three cards appear in sequence: time estimate, personalization, and privacy. The
goal is to answer the user's implicit "why are you asking me this?" before they ask it.

### Visual specification

| Property | Value |
| --- | --- |
| Background | `surface-card` (white) |
| Border radius | `radius-xl` (16px) |
| Shadow | `shadow-sm` |
| Padding | 16px |
| Layout | Flex row · icon left (22px, flex-shrink: 0) · text block right |
| Title | 15px DM Sans bold · `text-primary` · 4px below |
| Body | 13px DM Sans regular · `text-secondary` · line-height 1.5 |
| Gap between cards | `space-3` (12px) |

### Visual

### Rules

- Icon is always an emoji in V1 — no custom icon assets needed for this component.
- Keep body copy to 1–2 sentences. These are reassurances, not explanations.
- Three cards on Screen 05 is the canonical usage. Don't add more without reconsidering whether
  the screen is getting too heavy.

## Price / Purchase Card

The primary conversion element on the Paywall screen (Screen 09). Displays the price
prominently, reinforces the value proposition, and leads directly into the purchase CTA. Designed to
feel earned — the user has just seen their personalized plan.

### Visual specification

| Property | Value |
| --- | --- |
| Background | `surface-card` (white) |
| Border radius | `radius-xl` (16px) |
| Shadow | `shadow-md` |
| Padding | 24px 20px |
| Eyebrow | "One-time purchase" · 12px DM Sans regular · `text-secondary` |
| Price | Grandstander 48px bold · `text-primary` · letter-spacing `-0.02em` |
| Sub-label | "Lifetime access · All guides · Both partners" · 13px · `text-secondary` |
| Feature checklist | 16px margin top · left-aligned · checkmark (✓) in `status-success-surface` color · 14px body text |
| Alignment | Price section: centered · Feature checklist: left-aligned |

### Visual

### Rules

- One price, one card. No tiers in V1.
- The price uses Grandstander — consistent with stats and display text, but here it's doing
  conversion work. The brand personality in the number makes it feel less transactional.
- Feature list max 4–5 items. More starts to feel like a negotiation.

## Invite Link Card

Displays the shareable partner invite URL on Screen 04. The link is the mechanism — the
card makes it feel like something worth sharing rather than a technical string.

### Visual specification

| Property | Value |
| --- | --- |
| Background | `surface-card` (white) |
| Border | `1px solid border-default` |
| Border radius | `radius-lg` (12px) |
| Shadow | `shadow-sm` |
| Padding | 16px |
| Card label | "Your invite link" · 13px DM Sans bold · `text-primary` · 8px below |
| URL display | Monospace font (`SF Mono` / system mono) · 13px · `purple-500` · `rgba(95,69,242,0.06)` background · `radius-sm` (6px) · 8px 10px padding · word-break: break-all |

### Visual

### Rules

- The URL is display-only — tapping it selects/copies, it doesn't navigate. The Share/Send buttons
  below the card handle distribution.
- Never truncate the URL with an ellipsis. Use `word-break: break-all` so the full link
  is always visible.

## Badge Notification Card

An achievement unlock announcement shown on the Home screen (Screen 10). Appears when a
couple earns a milestone badge — one of the app's personality moments. The sarcastic badge names are
a core part of the brand voice.

### Visual specification

| Property | Value |
| --- | --- |
| Background | `surface-card` (white) |
| Border | `1px solid rgba(255,215,85,0.5)` — yellow-400 at 50% · warm, celebratory, not attention-grabbing |
| Border radius | `radius-lg` (12px) |
| Shadow | `shadow-sm` |
| Padding | 14px 16px |
| Layout | Flex row · medal emoji left (24px) · text right |
| Body text | 14px DM Sans regular · `text-primary` · badge name in bold |
| Dismissibility | Tapping dismisses — it disappears from Home on next session load |

### Visual

### Sample badge names

| Badge name | Trigger |
| --- | --- |
| "Officially panicking together" | First topic completed |
| "Surprisingly on the same page" | 3 consecutive fully-aligned reveals |
| "Still together after the finances talk" | Finances category complete |
| "Professionally disagreeing" | 5 "worth a conversation" reveals |
| "Did not see that coming" | First misaligned reveal |

### Rules

- The yellow border is intentional — it's celebratory without being aggressive. Don't replace it
  with a filled yellow background.
- Badge names are always in quotes in the UI — they're named things, not generic descriptions.
- One badge notification visible at a time on Home. If multiple badges unlock simultaneously,
  queue them — show one per session.

## Progress Row

A composed row showing one book category's completion state: category name, answered count, and a progress bar — all as a single tappable unit. Stacks vertically on the Progress screen (23) to show all 7 categories at once.

### Anatomy

| Element | Required? | Spec |
| --- | --- | --- |
| Category name | Required | 13px DM Sans medium, `text-primary`, left-aligned |
| Answer count | Required | 12px DM Sans regular, `text-secondary`, right-aligned. Format: "X of Y answered" |
| Progress bar | Required | Full-width, 6px track. Uses Progress Bar visual spec — `action-primary` fill, `radius-full` |

### Visual specification

| Property | Value |
| --- | --- |
| Row padding | 0 — no card wrapping. Rows sit directly on the page surface with spacing between them. |
| Gap between label row and bar | 6px |
| Gap between Progress Rows | `space-5` (20px) |
| Complete state — bar fill | `status-success-surface` (green-400, #77eaaf) instead of `action-primary` |
| Complete state — count label | "All answered" replaces "X of Y answered" |
| Not started state — bar | Empty track only. Count label reads "0 of Y answered". |
| Tap target height | Minimum 44px — pad vertically if the natural height is less |

### The 7 categories

These are fixed — they map directly to the 7 Daisy's Guide book categories. Order on the Progress screen follows book order.

| # | Category name |
| --- | --- |
| 1 | Birth plan |
| 2 | Sleep |
| 3 | Feeding |
| 4 | Finances |
| 5 | Relationships |
| 6 | Health |
| 7 | Childcare |

### Tap behavior

Tapping a Progress Row navigates to the Topic List (Screen 11) filtered to that category — so the user can jump directly into unanswered topics. This is the primary navigation affordance on the Progress screen.

### Relationship to Progress Bar

The Progress Row is a composed component that *uses* the Progress Bar's category row variant as its bar element. The distinction: Progress Bar specifies the bar itself (track, fill, animation). Progress Row specifies the full composed unit — label row + bar + spacing + tap behavior + state variations.

### Don't

- Don't wrap rows in cards. They sit directly on the page — the spacing between them creates the visual rhythm.
- Don't show percentages. "4 of 5 answered" is more concrete than "80%".
- Don't change the category order or names. They're tied to the book structure.
- Don't disable tap behavior for completed categories — users may want to revisit answered topics.

---

# Screens

## Screen 12 — Topic Intro

One screen shown before questions begin for each topic. Sets emotional context, primes
the user with what to expect, and transitions them from "browsing topics" into "answering this
topic."

|  |  |
| --- | --- |
| **Entered from** | Topic List (11) — user taps a topic |
| **Exits to** | Question (13) — "Start answering" — OR — Topic List (11) — "Back to topics" |
| **Bottom nav** | Hidden (inside a topic flow) |

### Visual

### Layout behavior

Flex column layout. Content sits above a flexible spacer that pushes the CTA region toward the bottom
for thumb reach. On most devices, this screen fits without scrolling. The CTA region is
**not** sticky — it floats toward the bottom naturally via the spacer.

### Topic illustration

| Property | Value |
| --- | --- |
| Container | White card sitting on the cream page |
| Height | 160px |
| Background | `surface-card` (white) |
| Border radius | `radius-xl` (16px) |
| Shadow | None — white-on-cream contrast does the lifting |
| Spacing below | `space-6` (24px) |

### Stats card

| Property | Value |
| --- | --- |
| Background | `surface-card` (white) |
| Border radius | `radius-lg` (12px) — stepped down since it's sub-card inside a larger composition |
| Shadow | None |
| Padding | `space-4` (16px) all sides |
| Layout | Two-column equal width, divided by a thin `border-default` vertical line |
| Number style | Grandstander 28px bold, `text-primary`, line-height 1.1× |
| Label style | `label-sm` uppercase, `text-secondary`, 4px below number |

### Don't

- Don't show the bottom nav on this screen.
- Don't skip the topic illustration — the white card against cream is a key visual anchor.
- Don't use more than 3 sentences for the topic blurb.
