#!/usr/bin/env python3
"""Split designed screens.html into per-screen HTML files + shared CSS."""
import re
import base64
from pathlib import Path

ROOT = Path(__file__).parent
SOURCE = ROOT / "designed screens.html"

# Sidebar entries: (data_idx, display_num, label)
SIDEBAR = [
    (0, 1, "Swipeable Intro", "Intro"),
    (1, 2, "Sign Up", "Auth"),
    (2, 3, "OTP Verification", None),
    (3, 4, "Log In", None),
    (4, 5, "Partner Linking", "Onboarding"),
    (5, 6, "Onboarding Intro", None),
    (6, 7, "Onboarding Quiz", None),
    (7, 8, "Building Your Plan", None),
    (8, 9, "Personalized Results", None),
    (9, 10, "Manage Topics", None),
    (10, 11, "Paywall", "Paywall"),
    (11, 12, "Home", "Home Base"),
    (22, 23, "Progress", None),
    (23, 24, "Settings", None),
    (12, 13, "Topic List", "Topic Flow"),
    (13, 14, "Topic Intro", None),
    (14, 15, "Topic Article", None),
    (15, 16, "Question", None),
    (16, 17, "Waiting for Partner", None),
    (17, 18, "Alignment Reveal", None),
    (18, 19, "Post-Reveal Reflection", None),
    (19, 20, "Re-answer Flow", None),
    (20, 21, "Completed Topic", None),
    (21, 22, "Prediction Card", "Special"),
    (24, 25, "Empty Home", "Empty States"),
    (25, 26, "Empty Topic List", None),
    (26, 27, "Payment Failure", "Error States"),
    (27, 28, "Connection Error", None),
]


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def load_screens():
    text = SOURCE.read_text(encoding="utf-8")
    screens = []
    for line in text.split("\n"):
        m = re.match(r"\s*\{ title: '([^']+)', b64: '([^']+)' \},?", line)
        if m:
            screens.append({"title": m.group(1), "b64": m.group(2)})
    return text, screens


def extract_shell_css(text: str) -> str:
    m = re.search(r"<style>(.*?)</style>", text, re.DOTALL)
    return m.group(1).strip() if m else ""


def extract_shell_sidebar_html(text: str) -> str:
    m = re.search(r"(<div class=\"sidebar\">.*?</div>)\s*<div class=\"main\">", text, re.DOTALL)
    return m.group(1) if m else ""


def prefix_css(css: str, page_class: str) -> str:
    """Scope screen CSS under body.page-XX .screen-root (and body for :root vars)."""
    scope = f"body.{page_class} .screen-root"
    body_scope = f"body.{page_class}"

    # Extract @keyframes blocks (keep global; rename if duplicate later)
    keyframes_store = []

    def stash_keyframes(match):
        keyframes_store.append(match.group(0))
        return f"\n/*__KF_{len(keyframes_store) - 1}__*/\n"

    css = re.sub(
        r"@keyframes\s+[\w-]+\s*\{(?:[^{}]|\{[^{}]*\})*\}",
        stash_keyframes,
        css,
        flags=re.DOTALL,
    )

    def prefix_block(block: str, media_wrapper: str = "") -> str:
        block = block.strip()
        if not block:
            return ""
        if block.startswith("@media"):
            # Recurse into media query body
            inner_match = re.match(r"(@media[^{]+)\{([\s\S]*)\}\s*$", block, re.DOTALL)
            if not inner_match:
                return block
            header, inner = inner_match.groups()
            inner_prefixed = prefix_block(inner, media_wrapper=header.strip())
            return f"{header}{{\n{inner_prefixed}\n}}"
        if block.startswith("/*__KF_"):
            return block

        # Split selector list from declarations
        if "{" not in block:
            return block
        sel_part, _, decl_part = block.partition("{")
        selectors = [s.strip() for s in sel_part.split(",") if s.strip()]
        prefixed = []
        for sel in selectors:
            if sel == ":root":
                prefixed.append(body_scope)
            elif sel == "body":
                prefixed.append(scope)
            elif sel == "html":
                prefixed.append(f"{body_scope} html")
            elif sel == "*":
                prefixed.append(f"{scope}, {scope} *")
            elif sel.startswith("body "):
                prefixed.append(f"{scope} {sel[5:]}")
            elif sel.startswith("html "):
                prefixed.append(f"{body_scope} {sel}")
            else:
                prefixed.append(f"{scope} {sel}")
        return ",\n".join(prefixed) + " {" + decl_part

    # Parse top-level blocks by brace counting
    blocks = []
    depth = 0
    start = 0
    i = 0
    while i < len(css):
        c = css[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                blocks.append(css[start : i + 1].strip())
                start = i + 1
        i += 1
    if start < len(css):
        tail = css[start:].strip()
        if tail:
            blocks.append(tail)

    out_parts = []
    for block in blocks:
        if not block:
            continue
        out_parts.append(prefix_block(block))

    result = "\n\n".join(out_parts)
    for idx, kf in enumerate(keyframes_store):
        result = result.replace(f"/*__KF_{idx}__*/", kf)
    return result


def build_sidebar_html(active_idx: int, idx_to_file: dict) -> str:
    lines = [
        '<div class="sidebar">',
        '  <div class="sidebar-brand">',
        '    <div class="sidebar-brand-title">daisy\'s guide</div>',
        '    <div class="sidebar-brand-sub">Designed Screens v1 · 28 screens</div>',
        '  </div>',
    ]
    last_section = None
    for data_idx, num, label, section in SIDEBAR:
        if section and section != last_section:
            lines.append(f'  <div class="sidebar-section-label">{section}</div>')
            last_section = section
        href = idx_to_file[data_idx]
        active = " active" if data_idx == active_idx else ""
        lines.append(
            f'  <a class="sidebar-item{active}" href="{href}">'
            f'<span class="screen-num">{num:02d}</span>{label}</a>'
        )
    lines.append("</div>")
    return "\n".join(lines)


def replace_nav_handlers(html: str, idx_to_file: dict) -> str:
    def nav_pill_repl(m):
        classes = m.group(1)
        before = m.group(2) or ""
        idx = int(m.group(3))
        after = m.group(4) or ""
        text = m.group(5)
        return (
            f'<a class="{classes}"{before}{after} href="{idx_to_file[idx]}">'
            f"{text}</a>"
        )

    html = re.sub(
        r'<div class="(nav-pill[^"]*)"([^>]*?)onclick="window\.parent\.showScreen\((\d+)\)"([^>]*)>([^<]+)</div>',
        nav_pill_repl,
        html,
    )
    return html


def main():
    text, screens = load_screens()
    shell_css = extract_shell_css(text)

    # idx -> filename
    idx_to_file = {}
    idx_to_page_class = {}
    for i, s in enumerate(screens):
        num = i + 1
        # use display num from sidebar if present
        for data_idx, display_num, label, _ in SIDEBAR:
            if data_idx == i:
                num = display_num
                break
        fname = f"{num:02d}-{slugify(s['title'])}.html"
        idx_to_file[i] = fname
        idx_to_page_class[i] = f"page-{i:02d}"

    all_screen_css = []
    for i, s in enumerate(screens):
        decoded = base64.b64decode(s["b64"]).decode("utf-8")
        style_m = re.search(r"<style>(.*?)</style>", decoded, re.DOTALL)
        body_m = re.search(r"<body[^>]*>([\s\S]*)</body>", decoded, re.DOTALL)
        script_parts = re.findall(r"<script[^>]*>([\s\S]*?)</script>", decoded, re.DOTALL)

        screen_css = style_m.group(1).strip() if style_m else ""
        scoped = prefix_css(screen_css, idx_to_page_class[i])
        all_screen_css.append(
            f"/* ── Screen {idx_to_file[i]} ── */\n{scoped}"
        )

        body_html = body_m.group(1).strip() if body_m else ""
        body_html = replace_nav_handlers(body_html, idx_to_file)

        prev_idx = i - 1 if i > 0 else None
        next_idx = i + 1 if i < len(screens) - 1 else None
        prev_href = idx_to_file[prev_idx] if prev_idx is not None else None
        next_href = idx_to_file[next_idx] if next_idx is not None else None

        sidebar = build_sidebar_html(i, idx_to_file)

        prev_btn = (
            f'<a class="topbar-btn" href="{prev_href}" aria-label="Previous">‹</a>'
            if prev_href
            else '<span class="topbar-btn disabled" aria-disabled="true">‹</span>'
        )
        next_btn = (
            f'<a class="topbar-btn" href="{next_href}" aria-label="Next">›</a>'
            if next_href
            else '<span class="topbar-btn disabled" aria-disabled="true">›</span>'
        )

        page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{s['title']} — Daisy's Guide Designed Screens</title>
<link href="https://fonts.googleapis.com/css2?family=Grandstander:wght@700&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body class="{idx_to_page_class[i]}">
{sidebar}
<div class="main">
  <div class="topbar">
    <span class="topbar-title">{s['title']}</span>
    <div style="display:flex;align-items:center;">
      <span class="key-hint">← →</span>
      <div class="topbar-nav">
        {prev_btn}
        <span class="topbar-counter">{i + 1} / {len(screens)}</span>
        {next_btn}
      </div>
    </div>
  </div>
  <div class="frame-wrap">
    <div class="screen-root">
{body_html}
    </div>
  </div>
</div>
"""
        if script_parts:
            page_html += "<script>\n" + "\n".join(script_parts) + "\n</script>\n"
        page_html += '<script src="nav.js"></script>\n</body>\n</html>\n'

        (ROOT / idx_to_file[i]).write_text(page_html, encoding="utf-8")

    # Shared styles.css
    extra_shell = """
/* Shell layout adjustments for inline screen content */
.frame-wrap { overflow-y: auto; }
.sidebar-item { text-decoration: none; }
.topbar-btn.disabled { opacity: 0.3; pointer-events: none; }
a.topbar-btn { text-decoration: none; }
"""
    styles = (
        "/* ── App shell ── */\n"
        + shell_css
        + extra_shell
        + "\n/* ── Screen content (scoped per page) ── */\n"
        + "\n\n".join(all_screen_css)
    )
    (ROOT / "styles.css").write_text(styles, encoding="utf-8")

    # nav.js - keyboard navigation between pages
    nav_js = """(function () {
  const pages = """
    nav_js += str([idx_to_file[i] for i in range(len(screens))])
    nav_js += """;
  const path = window.location.pathname.split('/').pop() || 'index.html';
  let idx = pages.indexOf(path);
  if (idx < 0) idx = 0;
  document.addEventListener('keydown', (e) => {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    const tag = (e.target && e.target.tagName) || '';
    if (tag === 'INPUT' || tag === 'TEXTAREA') return;
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
      if (idx < pages.length - 1) { e.preventDefault(); window.location.href = pages[idx + 1]; }
    }
    if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
      if (idx > 0) { e.preventDefault(); window.location.href = pages[idx - 1]; }
    }
  });
})();
"""
    (ROOT / "nav.js").write_text(nav_js, encoding="utf-8")

    # index redirect to first screen
    first = idx_to_file[0]
    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url={first}">
<title>Daisy's Guide — Designed Screens v1</title>
</head>
<body>
<p>Redirecting to <a href="{first}">{first}</a>…</p>
</body>
</html>
"""
    (ROOT / "index.html").write_text(index_html, encoding="utf-8")

    print(f"Generated {len(screens)} screen HTML files + styles.css + nav.js + index.html")
    for i, f in idx_to_file.items():
        print(f"  [{i:02d}] {f}")


if __name__ == "__main__":
    main()
