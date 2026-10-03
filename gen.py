"""Profile README art for github.com/yuxev.

Editorial layout with a hand-drawn pixel display font and original pixel art.
Every image is generated twice (light/dark) so it follows the viewer's GitHub theme.
Run `python gen3.py` → assets/*.svg
"""
import math
import os
import random
from xml.sax.saxutils import escape

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
W = 830  # README content width on a GitHub profile

THEMES = {
    "light": dict(ink="#1f2328", muted="#656d76", faint="#8c959f", rule="#d0d7de", accent="#d2461f",
                  pill="#f6f8fa"),
    "dark": dict(ink="#e6edf3", muted="#9198a1", faint="#6e7681", rule="#30363d", accent="#ff7a4d",
                 pill="#161b22"),
}
SERIF = "Georgia, 'Iowan Old Style', 'Times New Roman', serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]

# ───────────────────────── pixel display font ─────────────────────────
# 11 rows: 0-8 cap height, 3-8 x-height, 9-10 descenders. Proportional widths.
_U = {
    "A": ".###.|#...#|#...#|#...#|#####|#...#|#...#|#...#|#...#",
    "B": "####.|#...#|#...#|#...#|####.|#...#|#...#|#...#|####.",
    "C": ".###.|#...#|#....|#....|#....|#....|#....|#...#|.###.",
    "D": "####.|#...#|#...#|#...#|#...#|#...#|#...#|#...#|####.",
    "E": "#####|#....|#....|#....|####.|#....|#....|#....|#####",
    "F": "#####|#....|#....|#....|####.|#....|#....|#....|#....",
    "G": ".###.|#...#|#....|#....|#.###|#...#|#...#|#...#|.###.",
    "H": "#...#|#...#|#...#|#...#|#####|#...#|#...#|#...#|#...#",
    "I": "###|.#.|.#.|.#.|.#.|.#.|.#.|.#.|###",
    "J": "..###|...#.|...#.|...#.|...#.|...#.|...#.|#..#.|.##..",
    "K": "#...#|#...#|#..#.|#.#..|##...|#.#..|#..#.|#...#|#...#",
    "L": "#....|#....|#....|#....|#....|#....|#....|#....|#####",
    "M": "#...#|##.##|#.#.#|#.#.#|#...#|#...#|#...#|#...#|#...#",
    "N": "#...#|#...#|##..#|##..#|#.#.#|#..##|#..##|#...#|#...#",
    "O": ".###.|#...#|#...#|#...#|#...#|#...#|#...#|#...#|.###.",
    "P": "####.|#...#|#...#|#...#|####.|#....|#....|#....|#....",
    "R": "####.|#...#|#...#|#...#|####.|#.#..|#..#.|#...#|#...#",
    "S": ".###.|#...#|#....|#....|.###.|....#|....#|#...#|.###.",
    "T": "#####|..#..|..#..|..#..|..#..|..#..|..#..|..#..|..#..",
    "U": "#...#|#...#|#...#|#...#|#...#|#...#|#...#|#...#|.###.",
    "V": "#...#|#...#|#...#|#...#|#...#|#...#|.#.#.|.#.#.|..#..",
    "W": "#...#|#...#|#...#|#...#|#.#.#|#.#.#|#.#.#|##.##|#...#",
    "Y": "#...#|#...#|#...#|.#.#.|..#..|..#..|..#..|..#..|..#..",
    "0": ".###.|#...#|#..##|#.#.#|#.#.#|##..#|#...#|#...#|.###.",
    "1": "..#..|.##..|..#..|..#..|..#..|..#..|..#..|..#..|.###.",
    "2": ".###.|#...#|....#|....#|...#.|..#..|.#...|#....|#####",
    "3": ".###.|#...#|....#|....#|..##.|....#|....#|#...#|.###.",
    "4": "...#.|..##.|.#.#.|#..#.|#..#.|#####|...#.|...#.|...#.",
    "5": "#####|#....|#....|####.|....#|....#|....#|#...#|.###.",
    "6": ".###.|#....|#....|####.|#...#|#...#|#...#|#...#|.###.",
    "7": "#####|....#|....#|...#.|..#..|..#..|.#...|.#...|.#...",
    "8": ".###.|#...#|#...#|#...#|.###.|#...#|#...#|#...#|.###.",
    "9": ".###.|#...#|#...#|#...#|.####|....#|....#|#...#|.###.",
    "Q": ".###.|#...#|#...#|#...#|#...#|#...#|#.#.#|#..#.|.##.#",
    "X": "#...#|#...#|.#.#.|.#.#.|..#..|.#.#.|.#.#.|#...#|#...#",
    "Z": "#####|....#|...#.|...#.|..#..|.#...|.#...|#....|#####",
    "/": "....#|....#|...#.|...#.|..#..|.#...|.#...|#....|#....",
    ":": ".|.|.|#|.|.|.|.|#",
    "(": "..#|.#.|#..|#..|#..|#..|#..|.#.|..#",
    ")": "#..|.#.|..#|..#|..#|..#|..#|.#.|#..",
    "!": "#|#|#|#|#|#|#|.|#",
    ".": ".|.|.|.|.|.|.|.|#",
    "'": "#|#|.|.|.|.|.|.|.",
}
_L = {  # rows 3..8 (x-height), plus optional ascender rows 0..2 and descender rows 9..10
    "a": (None, ".###.|....#|.####|#...#|#...#|.####", None),
    "b": ("#....|#....|#....", "####.|#...#|#...#|#...#|#...#|####.", None),
    "c": (None, ".###|#...|#...|#...|#...|.###", None),
    "d": ("....#|....#|....#", ".####|#...#|#...#|#...#|#...#|.####", None),
    "e": (None, ".###.|#...#|#####|#....|#....|.###.", None),
    "f": ("..##|.#..|.#..", "####|.#..|.#..|.#..|.#..|.#..", None),
    "g": (None, ".####|#...#|#...#|#...#|#...#|.####", "....#|.###."),
    "h": ("#....|#....|#....", "####.|#...#|#...#|#...#|#...#|#...#", None),
    "i": (".|#|.", "#|#|#|#|#|#", None),
    "j": ("...|..#|...", "..#|..#|..#|..#|..#|..#", "..#|##."),
    "k": ("#...|#...|#...", "#..#|#.#.|##..|#.#.|#..#|#..#", None),
    "l": ("#.|#.|#.", "#.|#.|#.|#.|#.|.#", None),
    "m": (None, "######.|#..#..#|#..#..#|#..#..#|#..#..#|#..#..#", None),
    "n": (None, "####.|#...#|#...#|#...#|#...#|#...#", None),
    "o": (None, ".###.|#...#|#...#|#...#|#...#|.###.", None),
    "p": (None, "####.|#...#|#...#|#...#|#...#|####.", "#....|#...."),
    "r": (None, "#.##|##..|#...|#...|#...|#...", None),
    "s": (None, ".####|#....|.###.|....#|....#|####.", None),
    "t": ("....|.#..|.#..", "####|.#..|.#..|.#..|.#..|..##", None),
    "u": (None, "#...#|#...#|#...#|#...#|#...#|.####", None),
    "v": (None, "#...#|#...#|#...#|.#.#.|.#.#.|..#..", None),
    "w": (None, "#...#|#...#|#.#.#|#.#.#|#.#.#|.#.#.", None),
    "x": (None, "#...#|.#.#.|..#..|..#..|.#.#.|#...#", None),
    "y": (None, "#...#|#...#|#...#|#...#|#...#|.####", "....#|.###."),
    "_": (None, "....|....|....|....|....|....", "....|####"),
    "-": (None, "...|...|###|...|...|...", None),
    ",": (None, ".|.|.|.|.|#", "#|."),
    "q": (None, ".####|#...#|#...#|#...#|#...#|.####", "....#|....#"),
    "z": (None, "#####|...#.|..#..|.#...|#....|#####", None),
}
FONT = {}
for k, v in _U.items():
    rows = v.split("|")
    FONT[k] = rows + ["." * len(rows[0])] * 2
for k, (asc, x, desc) in _L.items():
    xr = x.split("|")
    w = len(xr[0])
    FONT[k] = (asc.split("|") if asc else ["." * w] * 3) + xr + (desc.split("|") if desc else ["." * w] * 2)
FONT[" "] = ["..."] * 11
BOLD = {}
for k, g in FONT.items():
    BOLD[k] = ["".join("#" if (row + ".")[i] == "#" or (i and row[i - 1] == "#") else "."
                       for i in range(len(row) + 1)) for row in g]


def R(x, y, w, h, fill, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"{extra}/>'


def ptext(s, x, y, s_, color, accent_from=None, accent=None, bold=True):
    """Pixel-font string at (x, y) with pixel size s_. Returns (svg, width)."""
    out, cx = [], x
    for i, ch in enumerate(s):
        g = (BOLD if bold else FONT)[ch]
        col = accent if accent_from is not None and i >= accent_from else color
        for r, line in enumerate(g):
            c = 0
            while c < len(line):
                if line[c] != "#":
                    c += 1
                    continue
                a = c
                while c < len(line) and line[c] == "#":
                    c += 1
                out.append(R(cx + a * s_, y + r * s_, (c - a) * s_, s_, col))
        cx += (len(g[0]) + 1) * s_
    return f'<g shape-rendering="crispEdges">{"".join(out)}</g>', cx - x - s_


def t(x, y, s, size, fill, family=SERIF, extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{fill}"{extra}>'
            f"{s}</text>")


def doc(h, body, style="", title=""):
    st = f"<style>{style}</style>" if style else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}">'
            f"<title>{escape(title)}</title>{st}{body}</svg>")


def pix(rows_fn, x, y, s, extra=""):
    """Wrap pixel-grid drawing (in grid units) into a crisp, scaled group."""
    return (f'<g transform="translate({x} {y}) scale({s})" shape-rendering="crispEdges"{extra}>'
            f"{rows_fn}</g>")


def save(name, theme, content):
    with open(os.path.join(OUT, f"{name}-{theme}.svg"), "w", encoding="utf-8") as f:
        f.write(content)


def dither_rows(x0, y0, w, h, a, b):
    """Vertical a→b gradient as Bayer-dithered pixel runs (grid units)."""
    out = [R(x0, y0, w, h, a)]
    for yy in range(h):
        lvl = int(16 * yy / max(1, h - 1) + 0.5)
        if not lvl:
            continue
        row = BAYER[(y0 + yy) % 4]
        if lvl >= 16:
            out.append(R(x0, y0 + yy, w, 1, b))
            continue
        for xx in range(w):
            if row[(x0 + xx) % 4] < lvl:
                out.append(R(x0 + xx, y0 + yy, 1, 1, b))
    return "".join(out)


# ───────────────────────── hero illustration: Tanger from the window ─────────────────────────
SCENES = {
    "dark": dict(sky=("#0e1428", "#26305a"), haze="#3a3a66", coast="#232a4c", sea=("#1d2a4a", "#111a30"),
                 glint="#e9d9a6", cliff="#0d111d", rim="#1b2236", tower="#cfc6b0", tower_s="#9d9582",
                 lamp="#ffd36b", frame="#3b2c26", frame_l="#4f3b32", sill="#5a4336", sill_f="#3e2e25",
                 cat="#0b0e17", pot="#b5532f", leaf="#3f6b48", leaf_l="#5d8d5e", mug="#d2461f",
                 steam="#9aa3b5", book=("#3d5a80", "#8e3b33", "#c99a3c"), night=True),
    "light": dict(sky=("#9cc9e6", "#bfdeee"), haze="#e4eef0", coast="#9fb6c6", sea=("#4f8fbd", "#3f7eab"),
                  glint="#ffffff", cliff="#8a6a4e", rim="#6f9a52", tower="#f2ece0", tower_s="#c9bfae",
                  lamp="#e8d9a0", frame="#8a5a3c", frame_l="#a8724e", sill="#b98a64", sill_f="#94694a",
                  cat="#2e2823", pot="#c0603a", leaf="#4f7d4f", leaf_l="#79a86a", mug="#d2461f",
                  steam="#ffffff", book=("#3d5a80", "#b8433a", "#e3b341"), night=False),
}


def scene(theme):
    p = SCENES[theme]
    rnd = random.Random(5)
    G = []  # grid 96 x 76
    gx0, gy0, gx1, gy1 = 6, 4, 90, 66  # glass
    gw = gx1 - gx0
    horizon = 47
    # sky
    G.append(dither_rows(gx0, gy0, gw, horizon - gy0, p["sky"][0], p["sky"][1]))
    if p["night"]:
        for _ in range(38):
            x, y = rnd.randrange(gx0, gx1), rnd.randrange(gy0, horizon - 6)
            G.append(R(x, y, 1, 1, rnd.choice(["#c9d1d9", "#8b949e", "#e9d9a6"]),
                       f' class="tw" style="animation-delay:{rnd.uniform(0, 5):.1f}s"'))
        mx, my = 40, 13  # crescent moon
        for yy in range(-4, 5):
            for xx in range(-4, 5):
                if xx * xx + yy * yy <= 18 and (xx - 2) ** 2 + (yy + 1) ** 2 > 10:
                    G.append(R(mx + xx, my + yy, 1, 1, "#efe3c2"))
    else:
        sx, sy = 40, 13
        for yy in range(-4, 5):
            span = int(math.sqrt(max(0, 18 - yy * yy)))
            G.append(R(sx - span, sy + yy, span * 2 + 1, 1, "#fff6d8"))
        for cx, cy, cw in [(34, 12, 14), (58, 20, 10), (12, 26, 9)]:
            cloud = (R(cx + 2, cy, cw - 4, 1, "#ffffff") + R(cx, cy + 1, cw, 2, "#ffffff")
                     + R(cx + 1, cy + 3, cw - 2, 1, "#e6f0f5"))
            G.append(f'<g class="drift">{cloud}</g>')
    # far coast of Spain across the strait
    for x in range(gx0, 60):
        h = int(2 + 1.6 * math.sin(x / 5.0) + 1.2 * math.sin(x / 2.3 + 1))
        G.append(R(x, horizon - h, 1, h, p["coast"]))
    G.append(R(gx0, horizon - 1, gw, 1, p["haze"], ' opacity=".5"'))
    # sea
    G.append(dither_rows(gx0, horizon, gw, gy1 - horizon, p["sea"][0], p["sea"][1]))
    for _ in range(12):
        x, y = rnd.randrange(gx0, 64), rnd.randrange(horizon + 2, gy1 - 1)
        G.append(R(x, y, rnd.choice([2, 3]), 1, p["glint"],
                   f' class="sh" opacity=".3" style="animation-delay:{rnd.uniform(0, 3):.1f}s"'))
    if p["night"]:  # moonlight path on the water
        for i, y in enumerate(range(horizon + 1, gy1, 2)):
            w = 2 + i // 2
            G.append(R(40 - w // 2 + rnd.choice([-2, 0, 2]), y, w, 1, p["glint"],
                       f' class="sh" opacity=".45" style="animation-delay:{i * 0.25:.2f}s"'))
    # Cap Spartel cliff
    for x in range(64, gx1):
        top = int(max(38, 66 - (x - 64) * 2.2)) if x < 77 else 38 + (1 if x % 7 == 0 else 0)
        G.append(R(x, top, 1, gy1 - top, p["cliff"]))
        G.append(R(x, top, 1, 1, p["rim"]))
    # lighthouse (square tower on a low keeper's house)
    L = 6  # lighthouse x offset
    G.append(R(70 + L, 34, 13, 4, p["tower_s"]))
    G.append(R(70 + L, 34, 13, 1, p["tower"]))
    G.append(R(74 + L, 22, 5, 13, p["tower"]))
    G.append(R(78 + L, 22, 1, 13, p["tower_s"]))
    G.append(R(73 + L, 21, 7, 1, p["tower_s"]))
    G.append(R(75 + L, 18, 3, 3, p["lamp"], ' class="lamp"' if p["night"] else ""))
    G.append(R(74 + L, 17, 5, 1, p["frame"]))
    G.append(R(76 + L, 16, 1, 1, p["frame"]))
    for wy in (25, 29):
        G.append(R(76 + L, wy, 1, 2, p["frame"]))
    if p["night"]:  # rotating beam: left and right halves alternate
        beam_l = "".join(R(x, 19 - (82 - x) // 9, 1, 1 + 2 * ((82 - x) // 9), "#ffe9a8")
                         for x in range(gx0, 81))
        beam_r = "".join(R(x, 19 - (x - 84) // 4, 1, 1 + 2 * ((x - 84) // 4), "#ffe9a8")
                         for x in range(84, gx1))
        G.append(f'<g class="bl">{beam_l}</g><g class="br">{beam_r}</g>')
    # glass sheen
    for x0, y0 in [(gx0 + 3, gy0 + 3), (49 + 3, gy0 + 3)]:
        for i in range(6):
            G.append(R(x0 + i, y0 + 8 - i, 1, 1, "#ffffff", ' opacity=".10"'))
    # window frame + mullions
    G.append(R(2, 0, 92, 4, p["frame"]) + R(2, 0, 4, 66, p["frame"]) + R(90, 0, 4, 66, p["frame"]))
    G.append(R(2, 0, 92, 1, p["frame_l"]) + R(2, 0, 1, 66, p["frame_l"]))
    G.append(R(47, 4, 3, 62, p["frame"]) + R(47, 4, 1, 62, p["frame_l"]))
    G.append(R(6, 32, 84, 3, p["frame"]) + R(6, 32, 84, 1, p["frame_l"]))
    # sill
    G.append(R(0, 66, 96, 2, p["sill"]) + R(0, 68, 96, 4, p["sill_f"]))
    G.append(R(2, 72, 92, 2, "#000000", ' opacity=".18"'))
    # plant
    G.append(R(10, 59, 10, 2, p["pot"]) + R(11, 61, 8, 5, p["pot"]) + R(11, 61, 8, 1, "#000000", ' opacity=".2"'))
    for lx, top, c in [(12, 47, "leaf"), (14, 43, "leaf_l"), (16, 46, "leaf"), (13, 51, "leaf_l"),
                       (17, 50, "leaf_l")]:
        G.append(R(lx, top, 1, 59 - top, p[c]) + R(lx + 1, top + 2, 1, 57 - top, p[c]))
    # books
    b1, b2, b3 = p["book"]
    G.append(R(24, 62, 14, 4, b1) + R(25, 58, 12, 4, b2) + R(26, 56, 10, 2, b3))
    G.append(R(24, 63, 14, 1, "#ffffff", ' opacity=".25"') + R(25, 59, 12, 1, "#ffffff", ' opacity=".25"'))
    # cat watching the strait (back view)
    cat = p["cat"]
    cx = -6
    G.append(R(58 + cx, 56, 9, 10, cat) + R(59 + cx, 54, 7, 2, cat) + R(60 + cx, 48, 6, 6, cat)
             + R(60 + cx, 46, 1, 2, cat) + R(65 + cx, 46, 1, 2, cat) + R(57 + cx, 60, 1, 6, cat))
    G.append(f'<g class="tail">{R(67 + cx, 63, 4, 2, cat)}{R(70 + cx, 60, 2, 3, cat)}</g>')
    G.append(f'<g class="tail2">{R(67 + cx, 63, 5, 2, cat)}{R(72 + cx, 64, 2, 2, cat)}</g>')
    # mug + steam
    G.append(R(79, 59, 7, 7, p["mug"]) + R(86, 60, 2, 1, p["mug"]) + R(87, 61, 1, 3, p["mug"])
             + R(86, 63, 1, 1, p["mug"]) + R(79, 59, 7, 1, "#ffffff", ' opacity=".3"'))
    for i, sx in enumerate((80, 82, 84)):
        G.append(f'<g class="st" style="animation-delay:{i * 0.7:.1f}s">'
                 f'{R(sx, 55, 1, 2, p["steam"])}{R(sx + 1, 53, 1, 2, p["steam"])}</g>')
    return "".join(G)


SCENE_CSS = (
    ".tw{animation:tw 5s ease-in-out infinite}@keyframes tw{50%{opacity:.25}}"
    ".sh{animation:sh 3s steps(2) infinite}@keyframes sh{50%{opacity:.15}}"
    ".lamp{animation:lamp 6s steps(1) infinite}@keyframes lamp{50%{fill:#fff3c4}}"
    ".bl{opacity:0;animation:bl 6s linear infinite}.br{opacity:0;animation:br 6s linear infinite}"
    "@keyframes bl{0%,45%{opacity:0}55%{opacity:.28}75%{opacity:.14}100%{opacity:0}}"
    "@keyframes br{0%{opacity:.22}20%{opacity:.1}35%,90%{opacity:0}100%{opacity:.22}}"
    ".drift{animation:drift 40s linear infinite alternate}@keyframes drift{to{transform:translateX(8px)}}"
    ".st{opacity:0;animation:st 2.4s steps(4) infinite}"
    "@keyframes st{0%{opacity:0;transform:translateY(2px)}30%{opacity:.6}100%{opacity:0;transform:translateY(-4px)}}"
    ".tail{animation:tl 4s steps(1) infinite}.tail2{animation:tl2 4s steps(1) infinite}"
    "@keyframes tl{0%{opacity:1}80%,100%{opacity:0}}@keyframes tl2{0%{opacity:0}80%,100%{opacity:1}}"
)


# ───────────────────────── hero ─────────────────────────
def hero(th, c):
    H = 380
    b = []
    b.append(R(0, 14, 8, 8, c["accent"]))
    b.append(t(18, 22, "SOFTWARE DEVELOPER  ·  TANGER, MOROCCO", 11.5, c["muted"], MONO,
               ' letter-spacing="1.6"'))
    s1, _ = ptext("Adil", 0, 46, 6, c["ink"])
    s2, _ = ptext("Asselman", 0, 112, 6, c["ink"])
    b += [s1, s2]
    acc = c["accent"]
    lines = [f'I write <tspan font-style="italic" fill="{acc}">systems-level</tspan> C and C++,',
             "ship full-stack TypeScript products,",
             f'and build <tspan font-style="italic" fill="{acc}">mobile games</tspan>.']
    for i, ln in enumerate(lines):
        b.append(t(0, 206 + i * 28, ln, 21, c["ink"]))
    facts = [("BASED IN", "Tanger, Morocco"), ("CURRENTLY", "Freelancing &amp; building games"),
             ("OPEN TO", "Full-time &amp; freelance")]
    y = 290
    for k, v in facts:
        b.append(R(0, y - 18, 410, 1, c["rule"]))
        b.append(t(0, y + 1, k, 10.5, c["faint"], MONO, ' letter-spacing="1.4"'))
        b.append(t(112, y + 1, v, 15.5, c["ink"]))
        y += 30
    b.append(R(0, y - 18, 410, 1, c["rule"]))
    b.append(pix(scene(th), 446, 46, 4))
    style = SCENE_CSS
    save("hero", th, doc(H, "".join(b), style,
                         "Adil Asselman — software developer in Tanger. Pixel art: Cap Spartel lighthouse "
                         "seen from a window."))


# ───────────────────────── section headers ─────────────────────────
def section(th, c, num, label, title, accent_from=None):
    H = 112
    b = [t(0, 30, num, 12, c["accent"], MONO, ' font-weight="700" letter-spacing="1"')]
    b.append(t(26, 30, f"/  {label}", 12, c["muted"], MONO, ' letter-spacing="1.6"'))
    lx = 26 + (len(label) + 3) * 8.6 + 14
    b.append(R(lx, 25, W - lx, 1, c["rule"]))
    s, _ = ptext(title, 0, 46, 5, c["ink"], accent_from, c["accent"])
    b.append(s)
    save(f"sec-{label.lower()}", th, doc(H, "".join(b), "", f"{num} {label}: {title}"))


# ───────────────────────── project thumbnails (24 x 18 grid) ─────────────────────────
def thumb(kind, th):
    dark = th == "dark"
    o = []
    if kind == "flock":
        for i, col in enumerate(["#2e2350", "#4a2f63", "#76406d", "#a9546a", "#d9705f", "#f29a62"]):
            o.append(R(0, i * 3, 24, 3, col))
        o.append(R(15, 12, 5, 1, "#ffd48a") + R(14, 13, 7, 2, "#ffd48a"))
        o.append(R(0, 15, 24, 3, "#241b38"))
        birds = [(3, 3), (8, 5), (13, 2), (6, 9), (12, 8), (17, 5)]
        k = "#1a1426"
        for i, (x, y) in enumerate(birds):
            up = R(x, y, 2, 1, k) + R(x + 2, y + 1, 1, 1, k) + R(x + 3, y, 2, 1, k)
            dn = R(x, y + 1, 1, 1, k) + R(x + 1, y, 3, 1, k) + R(x + 4, y + 1, 1, 1, k)
            d = f' style="animation-delay:{i * 0.13:.2f}s"'
            o.append(f'<g class="fa"{d}>{up}</g><g class="fb"{d}>{dn}</g>')
    elif kind == "dash":
        o.append(R(0, 0, 24, 18, "#0f1622") + R(0, 0, 24, 3, "#1c2636"))
        o.append(R(1, 1, 1, 1, "#ff5f57") + R(3, 1, 1, 1, "#febc2e") + R(5, 1, 1, 1, "#28c840"))
        code = [(2, 5, 6, "#7fd1b9"), (9, 5, 5, "#e8eef2"), (4, 7, 8, "#f2b84b"), (4, 9, 5, "#e8eef2"),
                (10, 9, 4, "#7fd1b9"), (2, 11, 4, "#e8eef2"), (4, 13, 7, "#8aa0b8")]
        for x, y, w, col in code:
            o.append(R(x, y, w, 1, col))
        o.append(R(16, 8, 6, 6, "#28c840") + R(17, 11, 1, 1, "#0f1622") + R(18, 12, 1, 1, "#0f1622")
                 + R(19, 11, 1, 1, "#0f1622") + R(20, 10, 1, 1, "#0f1622"))
        o.append(R(14, 15, 1, 1, "#e8eef2", ' class="blink"'))
    elif kind == "pong":
        o.append(R(0, 0, 24, 18, "#101418"))
        for y in range(1, 18, 3):
            o.append(R(12, y, 1, 2, "#3a4250"))
        o.append(R(2, 5, 1, 5, "#e8eef2", ' class="pl"') + R(21, 8, 1, 5, "#e8eef2", ' class="pr"'))
        o.append(R(0, 0, 2, 2, "#ff7a4d", ' class="ball"'))
        o.append(R(9, 1, 1, 2, "#8a93a3") + R(14, 1, 1, 2, "#8a93a3"))
    elif kind == "mem":
        o.append(R(0, 0, 24, 18, "#f4efe6" if not dark else "#1a1f2b"))
        cols = ["#e2502a", "#2f6fed", "#3d8a5a", "#e3b341"]
        rnd = random.Random(2)
        for row in range(4):
            x = 1
            while x < 23:
                w = rnd.choice([2, 3, 4, 5])
                w = min(w, 23 - x)
                free = rnd.random() < 0.3
                col = ("#d6d0c4" if not dark else "#2c3344") if free else rnd.choice(cols)
                o.append(R(x, 1 + row * 4, w - 1 if w > 1 else 1, 3, col))
                x += w
        o.append(R(9, 13, 3, 3, "#ffffff", ' class="blink" opacity=".7"'))
    elif kind == "table":
        o.append(R(0, 0, 24, 18, "#2a2140"))
        for yy in range(-6, 7):
            span = int(math.sqrt(max(0, 40 - yy * yy)))
            o.append(R(12 - span, 9 + yy, span * 2, 1, "#8a5b3c"))
        for i in range(5):
            a = -math.pi / 2 + i * 2 * math.pi / 5
            px, py = 12 + 4 * math.cos(a), 9 + 4 * math.sin(a)
            o.append(R(round(px) - 1, round(py) - 1, 2, 2, "#e9e3f5",
                       f' class="eat" style="animation-delay:{i * 0.8:.1f}s"'))
            fa = a + math.pi / 5
            o.append(R(round(12 + 4.5 * math.cos(fa)), round(9 + 4.5 * math.sin(fa)), 1, 1, "#c9c2d6"))
    elif kind == "ray":
        o.append(R(0, 0, 24, 9, "#1c2233") + R(0, 9, 24, 9, "#3a3128"))
        o.append(R(0, 13, 24, 1, "#463b30") + R(0, 16, 24, 1, "#4f4235"))
        ramp = ["#2b3247", "#3b4560", "#4f5b7a", "#66739a", "#8290b8"]
        for x in range(24):
            d = abs(x - 11.5)
            h = 4 if d < 3 else min(18, int(4 + (d - 2.5) * 1.6))
            shade = ramp[min(4, int(d / 2.6))] if d >= 3 else "#232a3d"
            top = 9 - h // 2
            o.append(R(x, top, 1, h, shade))
            if d >= 3 and (x % 3 == 0):
                o.append(R(x, top, 1, h, "#000000", ' opacity=".22"'))
        o.append(R(11, 8, 2, 2, "#ffcf6b", ' class="blink"'))
    elif kind == "dl":
        o.append(R(0, 0, 24, 18, "#14161c"))
        for i, (col, dur) in enumerate([("#7fd18b", 3.2), ("#46c2ff", 4.1), ("#f2b84b", 2.6),
                                        ("#ff7aa8", 5.0)]):
            y = 2 + i * 4
            o.append(R(2, y, 20, 2, "#2a2e38"))
            o.append(f'<rect x="2" y="{y}" width="20" height="2" fill="{col}" class="bar" '
                     f'style="animation-duration:{dur}s"/>')
    frame = "#30363d" if dark else "#1f2328"
    return ("".join(o) + R(0, 0, 24, 1, frame, ' opacity=".9"') + R(0, 17, 24, 1, frame, ' opacity=".9"')
            + R(0, 0, 1, 18, frame, ' opacity=".9"') + R(23, 0, 1, 18, frame, ' opacity=".9"'))


THUMB_CSS = (
    ".blink{animation:blink 1.1s steps(1) infinite}@keyframes blink{50%{opacity:0}}"
    ".fa{animation:fa .5s steps(1) infinite}.fb{animation:fa .5s steps(1) infinite reverse}"
    "@keyframes fa{0%{opacity:1}50%{opacity:0}}"
    ".ball{animation:ball 2.4s linear infinite}"
    "@keyframes ball{0%{transform:translate(3px,4px)}25%{transform:translate(11px,14px)}"
    "50%{transform:translate(19px,9px)}75%{transform:translate(11px,2px)}100%{transform:translate(3px,4px)}}"
    ".pl{animation:pl 2.4s steps(6) infinite alternate}@keyframes pl{to{transform:translateY(-2px)}}"
    ".pr{animation:pr 2.4s steps(6) infinite alternate}@keyframes pr{to{transform:translateY(-6px)}}"
    ".eat{animation:eat 4s steps(1) infinite}@keyframes eat{0%{fill:#ff7a4d}20%{fill:#e9e3f5}}"
    ".bar{transform-box:fill-box;transform-origin:left;animation:bar 3s steps(10) infinite}"
    "@keyframes bar{from{transform:scaleX(0)}to{transform:scaleX(1)}}"
)

WORK = [  # (slug, title, meta, description, thumb)
    ("flockfall", "Flockfall", "2026  ·  MOBILE GAME  ·  GOOGLE PLAY",
     "Guide a flock of birds through a handcrafted 2D sky and keep your numbers growing.", "flock"),
    ("cagrex", "Cagrex", "2025  ·  PRODUCT  ·  FOUNDER",
     "Developer assessments for the AI era: real build tasks with an AI assistant in a sandbox.", "dash"),
    ("ft_transcendence", "ft_transcendence", "1337  ·  WEB  ·  TEAM PROJECT",
     "Team project, the 42 finale: pong in the browser, 42 sign-in, tournaments.", "pong"),
    ("smalloc", "smalloc", "1337  ·  SYSTEMS  ·  C",
     "A small malloc on top of mmap, to learn how allocators manage memory.", "mem"),
    ("syncmaster", "SyncMaster", "1337  ·  SYSTEMS  ·  C",
     "Dining philosophers with pthreads: mutex ordering, no data races, nobody starves.", "table"),
    ("cub3d", "cub3d", "1337  ·  GRAPHICS  ·  C",
     "A Wolfenstein-style raycasting engine: textures, map parsing, all by hand.", "ray"),
    ("downloader", "multithreading-downloader", "SYSTEMS  ·  C++",
     "Parallel file downloads with libcurl and mutex-guarded state.", "dl"),
]


def work_row(th, c, slug, title, meta, desc, kind):
    H = 104
    b = [pix(thumb(kind, th), 0, 14, 4)]
    b.append(t(124, 30, meta, 11, c["faint"], MONO, ' letter-spacing="1.3"'))
    s, _ = ptext(title, 124, 40, 3, c["ink"])
    b.append(s)
    b.append(t(124, 92, escape(desc), 15.5, c["muted"]))
    # pixel arrow
    arrow = "".join(R(x, 0, 1, 1, c["accent"]) for x in range(7)) + R(4, -2, 1, 1, c["accent"]) \
        + R(5, -1, 1, 1, c["accent"]) + R(5, 1, 1, 1, c["accent"]) + R(4, 2, 1, 1, c["accent"])
    b.append(pix(arrow, W - 24, 52, 3))
    b.append(R(0, H - 1, W, 1, c["rule"]))
    save(f"work-{slug}", th, doc(H, "".join(b), THUMB_CSS, f"{title} — {desc}"))


# ───────────────────────── experience ─────────────────────────
LOG = [
    ("2026 — NOW", "Freelance Web Engineer", "Upwork, remote",
     "Next.js builds and AWS deployments for clients, incl. a repeat engagement.", True),
    ("FEB — AUG 2026", "Full-Stack Developer", "Lysi Consulting",
     "AI features in TypeScript & Node.js for a live HR and recruitment platform.", False),
    ("JUN — DEC 2025", "Founder &amp; Full-Stack Engineer", "Cagrex",
     "Built a developer-assessment platform alone, end to end.", False),
    ("THE START", "Common Core", "1337 · 42 Network",
     "C and C++ from scratch: allocators, shells, threads, servers.", False),
]


def experience(th, c):
    row = 84
    H = len(LOG) * row + 6
    b = [R(150, 10, 1, H - 20, c["rule"])]
    for i, (date, role, org, note, now) in enumerate(LOG):
        y = i * row
        b.append(t(0, y + 32, date, 11, c["accent"] if now else c["faint"], MONO, ' letter-spacing="1.3"'))
        b.append(R(147, y + 24, 7, 7, c["accent"] if now else c["muted"]))
        b.append(t(176, y + 32, role, 20, c["ink"]))
        b.append(t(176, y + 54, f'<tspan font-style="italic">{org}</tspan>  —  {escape(note)}'
                   .replace("&amp;amp;", "&amp;"), 14.5, c["muted"]))
        if i < len(LOG) - 1:
            b.append(R(176, y + row - 6, W - 176, 1, c["rule"]))
    save("experience", th, doc(H, "".join(b), "", "Experience"))


# ───────────────────────── toolbox ─────────────────────────
ICONS = {
    "chip": ".#.#.|#####|#...#|#.#.#|#...#|#####|.#.#.",
    "globe": ".###.|#.#.#|#####|#.#.#|#####|#.#.#|.###.",
    "spark": "..#..|..#..|.###.|#####|.###.|..#..|..#..",
    "pad": ".....|.###.|#####|#.#.#|#####|##.##|.....",
    "rack": "#####|#...#|#####|#...#|#####|#...#|#####",
}
TOOLS = [
    ("chip", "LANGUAGES", ["C", "C++", "TypeScript", "JavaScript", "Python", "SQL"]),
    ("globe", "WEB", ["Next.js", "NestJS", "React", "Node.js", "PostgreSQL", "Prisma"]),
    ("spark", "AI", ["Claude API", "Gemini API", "E2B sandboxes", "Claude Code"]),
    ("pad", "GAMES", ["Godot", "Unity"]),
    ("rack", "OPS", ["Docker", "Nginx", "AWS EC2", "Linux", "Git", "K3s"]),
]


def toolbox(th, c):
    b = []
    y = 0
    for icon, label, items in TOOLS:
        ic = "".join(R(x, r, 1, 1, c["accent"]) for r, line in enumerate(ICONS[icon].split("|"))
                     for x, ch in enumerate(line) if ch == "#")
        b.append(pix(ic, 0, y + 11, 2))
        b.append(t(22, y + 23, label, 11, c["muted"], MONO, ' letter-spacing="1.4"'))
        x = 150
        for it in items:
            w = int(len(it) * 7.9 + 26)
            if x + w > W:
                x, y = 150, y + 40
            b.append(f'<rect x="{x}" y="{y + 4}" width="{w}" height="28" rx="14" fill="{c["pill"]}" '
                     f'stroke="{c["rule"]}"/>')
            b.append(t(x + 13, y + 22.5, escape(it), 13, c["ink"], MONO))
            x += w + 8
        y += 46
    save("toolbox", th, doc(y + 4, "".join(b), "", "Toolbox: " +
                            "; ".join(f"{l}: {', '.join(i)}" for _, l, i in TOOLS)))


# ───────────────────────── contact + footer ─────────────────────────
def contact(th, c):
    H = 236
    b = [t(0, 30, "05", 12, c["accent"], MONO, ' font-weight="700" letter-spacing="1"'),
         t(26, 30, "/  CONTACT", 12, c["muted"], MONO, ' letter-spacing="1.6"'),
         R(26 + 10 * 8.6 + 14, 25, W - (26 + 10 * 8.6 + 14), 1, c["rule"])]
    s, w = ptext("Say hello.", 0, 46, 7, c["ink"], 9, c["accent"])
    b.append(s)
    b.append(t(0, 162, "Open to full-time roles and freelance projects. Systems, full-stack or games:",
               18, c["muted"]))
    b.append(t(0, 188, "tell me what you’re building.", 18, c["muted"]))
    b.append(t(0, 226, "adilasselman137@gmail.com", 22, c["ink"], MONO))
    b.append(R(0, 232, 352, 2, c["accent"]))
    save("contact", th, doc(H, "".join(b), "", "Say hello: adilasselman137@gmail.com"))


def footer(th, c):
    H = 56
    lh = ("..#..|.###.|.#.#.|.###.|..#..|..#..|.###.|.#.#.|.###.|.#.#.|.###.|#####")
    tower = "".join(R(x, r, 1, 1, c["muted"]) for r, line in enumerate(lh.split("|"))
                    for x, ch in enumerate(line) if ch == "#")
    tower += R(2, 0, 1, 1, c["accent"], ' class="blink"')
    b = [R(0, 8, W, 1, c["rule"]), pix(tower, 0, 22, 2)]
    b.append(t(22, 44, "© 2026 ADIL ASSELMAN", 11, c["faint"], MONO, ' letter-spacing="1.4"'))
    b.append(t(W, 44, "BUILT IN TANGER, WHERE TWO SEAS MEET", 11, c["faint"], MONO,
               ' letter-spacing="1.4" text-anchor="end"'))
    save("footer", th, doc(H, "".join(b), ".blink{animation:b 2s steps(1) infinite}@keyframes b{50%{opacity:0}}",
                           "Footer"))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for th, c in THEMES.items():
        hero(th, c)
        section(th, c, "01", "ABOUT", "Under the hood", 10)
        section(th, c, "02", "WORK", "Selected work", 9)
        section(th, c, "03", "EXPERIENCE", "The logbook", 4)
        section(th, c, "04", "TOOLBOX", "On the desk", 7)
        for row in WORK:
            work_row(th, c, *row)
        experience(th, c)
        toolbox(th, c)
        contact(th, c)
        footer(th, c)
    print("generated", len([f for f in os.listdir(OUT) if "-light" in f or "-dark" in f]), "svgs")
