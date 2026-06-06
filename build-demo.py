#!/usr/bin/env python3
"""
build-demo.py  —  Generate the mobile demo (demo/mobile/) from the illustration-
enriched demo/ sandbox pages. Re-runnable; touches nothing in demo/*.html or v4/.

For each demo/NN-*.html it writes demo/mobile/screens/NN-*.html: the page near-
verbatim (own body class, inline styles, scripts intact) plus demo-fit.css, which
hides the documentation shell and makes the phone fill the viewport. Internal
links keep their filenames, so the app's own buttons drive in-iframe navigation.
"""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(ROOT, "demo")                 # source: illustration-enriched sandbox
SCR  = os.path.join(ROOT, "demo", "mobile", "screens")
os.makedirs(SCR, exist_ok=True)

pages = sorted(p for p in glob.glob(os.path.join(SRC, "[0-9]*.html")))
written = []
for path in pages:
    name = os.path.basename(path)
    html = open(path, encoding="utf-8").read()

    # styles.css (the diverged demo one) -> reachable from demo/mobile/screens/
    html = html.replace('href="styles.css"', 'href="../../styles.css"')
    # load demo-fit.css after it so the shell overrides win
    html = html.replace('href="../../styles.css">',
                        'href="../../styles.css">\n<link rel="stylesheet" href="../demo-fit.css">', 1)
    # repoint placeholder images (repo-root/images) from the deeper folder
    html = html.replace('"../images/', '"../../../images/')
    # repoint real illustrations (demo/illus) referenced as bare 'illus/...'
    for q in ("'illus/", '"illus/', '(illus/'):
        html = html.replace(q, q[0] + '../../illus/')
    # design-system doc link -> still reachable (harmless if untapped)
    html = html.replace('href="design system.md"', 'href="../../../v4/design system.md"')
    # demo-mode flag on <body>, preserving its existing page-NN scope class
    if re.search(r'<body class="[^"]*">', html):
        html = re.sub(r'<body class="([^"]*)">', r'<body class="\1 demo-mode">', html, 1)
    else:
        html = re.sub(r'<body>', '<body class="demo-mode">', html, 1)
    # drop the doc-shell keyboard nav (the mobile shell provides its own)
    html = html.replace('<script src="nav.js"></script>', '')
    # auto-show the real A-variant illustration on load. Screens with the
    # variant mechanism (only screen 01 today) boot on the placeholder because
    # nothing calls showVariant(); the demo hides the doc-shell variant pills
    # that would trigger it. Inject a load-time call so the real illustration
    # shows and Next walks the variant row. Guarded so it no-ops on other screens.
    if "function showVariant" in html:
        boot = ("\n  if (typeof showVariant === 'function') "
                "showVariant('1A');\n</script>")
        html = html.replace("\n</script>", boot, 1)

    open(os.path.join(SCR, name), "w", encoding="utf-8").write(html)
    written.append(name)

print(f"Wrote {len(written)} screens to demo/mobile/screens/")
