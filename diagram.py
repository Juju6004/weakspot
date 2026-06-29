# -*- coding: utf-8 -*-
"""Generate a discriminator arrow-chart SVG from a spec dict — no hand-placed
coordinates, auto-sized, text auto-wrapped so nothing clips.

Single vertical column (title -> cues -> THE TELL -> answer -> RULED OUT) so it
renders reliably and reads top-to-bottom on a phone. This is the "diagram-back"
format: the card's explanation is a chart, not a paragraph.

    spec = {
      "title": "Post-op incision drainage -> what is it?",
      "cues":  ["POD 6, after C-section",
                "*serosanguineous* drainage (not pus)",
                "probe -> *NO resistance*"],
      "tell":  "probe slides in freely + serosanguineous (not pus)",
      "answer": "FASCIAL DEHISCENCE",
      "answer_sub": "the fascia is open - surgical emergency",   # optional
      "ruled_out": [("wound infection", "needs pus + fever + erythema"),
                    ("subfascial abscess", "probe meets RESISTANCE + purulent")],
    }

*bold* markup is honored in any text field.
"""
import html


def _esc(s):
    return html.escape(s, quote=False)


def _markup(text):
    out, bold = [], False
    for seg in text.split("*"):
        if seg:
            out.append(f'<tspan font-weight="700">{_esc(seg)}</tspan>' if bold else _esc(seg))
        bold = not bold
    return "".join(out)


def _wrap(text, max_chars):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if not cur or len(cur) + len(w) + 1 <= max_chars:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def discriminator_svg(spec):
    W, X = 800, 30
    CW = W - 2 * X            # content width 740
    cx = X + CW / 2
    p = []

    def text(x, y, s, size, fill, weight=None, anchor=None, markup=False):
        w = f' font-weight="{weight}"' if weight else ""
        a = f' text-anchor="{anchor}"' if anchor else ""
        body = _markup(s) if markup else _esc(s)
        p.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}"{w}{a}>{body}</text>')

    def rect(x, y, w, h, fill, stroke, sw=1, rx=10):
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
                 f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def arrow(x, y1, y2):
        p.append(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="#444" '
                 f'stroke-width="2" marker-end="url(#ah)"/>')

    # title (wraps)
    y = 44
    for ln in _wrap(spec["title"], 44):
        text(X, y, ln, 23, "#1a1a1a", weight="700", markup=True)
        y += 31
    y += 6

    # cue chips
    for c in spec["cues"]:
        clines = _wrap(c, 58)
        ch = max(44, 16 + len(clines) * 24)
        rect(X, y, CW, ch, "#e7f0fb", "#a9c7ec")
        ty = y + 28
        for ln in clines:
            text(X + 16, ty, ln, 17, "#0d3b66", markup=True)
            ty += 24
        y += ch + 12
    arrow(cx, y - 2, y + 28)
    y += 36

    # the tell
    tlines = _wrap(spec["tell"], 58)
    th = 32 + len(tlines) * 24
    rect(X, y, CW, th, "#fffbe6", "#e8b500", sw=2)
    text(X + 18, y + 26, "THE TELL", 14, "#8a6d00", weight="700")
    ty = y + 50
    for ln in tlines:
        text(X + 18, ty, ln, 16.5, "#5b4a00", markup=True)
        ty += 24
    y += th
    arrow(cx, y, y + 32)
    y += 38

    # answer
    sub = spec.get("answer_sub")
    ah = 78 if sub else 58
    rect(X + 60, y, CW - 120, ah, "#e6f5ea", "#1b8a4b", sw=3, rx=12)
    text(cx, y + (34 if sub else 37), spec["answer"], 22, "#1b5e20",
         weight="800", anchor="middle", markup=True)
    if sub:
        text(cx, y + 58, sub, 15.5, "#256b3a", anchor="middle", markup=True)
    y += ah + 28

    # ruled out
    text(X, y, "RULED OUT", 16, "#888888", weight="700")
    y += 18
    for name, reason in spec["ruled_out"]:
        rlines = _wrap(reason, 66)
        bh = 30 + len(rlines) * 22
        rect(X, y, CW, bh, "#f5f5f5", "#dddddd")
        text(X + 16, y + 24, "✗ " + name, 15.5, "#a93226", weight="700")
        yy = y + 46
        for ln in rlines:
            text(X + 16, yy, ln, 14.5, "#555555", markup=True)
            yy += 22
        y += bh + 10

    H = int(y + 18)
    head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" font-family="-apple-system,Helvetica,Arial,sans-serif">'
            '<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#444"/></marker></defs>'
            f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
    return head + "".join(p) + "</svg>"
