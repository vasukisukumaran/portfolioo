"""Draw lightweight vector plates for the portfolio's project and exploration sections."""

from math import cos, exp, pi, sin
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = (ROOT if (ROOT / "site.css").is_file() else ROOT / "dist") / "assets"
OUT.mkdir(parents=True, exist_ok=True)


def points(coords):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in coords)


def polygon(coords, fill, stroke="none", width=1, opacity=1):
    return f'<polygon points="{points(coords)}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" opacity="{opacity}"/>'


def line(coords, stroke, width=1, opacity=1):
    return f'<polyline points="{points(coords)}" fill="none" stroke="{stroke}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round" opacity="{opacity}"/>'


DEFS = """
<defs>
  <linearGradient id="bg" x2="1" y2="1" gradientUnits="objectBoundingBox">
    <stop stop-color="#51484d"/><stop offset=".44" stop-color="#302d33"/><stop offset="1" stop-color="#242328"/>
  </linearGradient>
  <radialGradient id="mist" cx=".74" cy=".24" r=".85">
    <stop stop-color="#a87678"/><stop offset=".52" stop-color="#51454e"/><stop offset="1" stop-color="#26262c"/>
  </radialGradient>
  <linearGradient id="salmon" x1="0" y1="1" x2="1" y2="0">
    <stop stop-color="#c06864"/><stop offset=".53" stop-color="#f58f7c"/><stop offset="1" stop-color="#ffd1c6"/>
  </linearGradient>
  <linearGradient id="shadow" x1="0" y1="0" x2="1" y2="1">
    <stop stop-color="#514247"/><stop offset="1" stop-color="#241f26"/>
  </linearGradient>
  <linearGradient id="pink" x1="0" y1=".1" x2=".9" y2=".85">
    <stop stop-color="#f7c9c8"/><stop offset=".5" stop-color="#e9a3a1"/><stop offset="1" stop-color="#8e666c"/>
  </linearGradient>
  <linearGradient id="glassA" x1="0" y1="0" x2="1" y2="1">
    <stop stop-color="#ffb4aa" stop-opacity=".74"/><stop offset=".5" stop-color="#ef8f8a" stop-opacity=".23"/><stop offset="1" stop-color="#74363f" stop-opacity=".54"/>
  </linearGradient>
  <linearGradient id="glassB" x1="0" y1="1" x2="1" y2="0">
    <stop stop-color="#5e353e" stop-opacity=".72"/><stop offset=".62" stop-color="#e7827d" stop-opacity=".39"/><stop offset="1" stop-color="#ffd5c9" stop-opacity=".75"/>
  </linearGradient>
  <linearGradient id="glassTop" x1="0" y1="0" x2="1" y2="1">
    <stop stop-color="#ffb1a7" stop-opacity=".9"/><stop offset=".5" stop-color="#f39a92" stop-opacity=".37"/><stop offset="1" stop-color="#84545e" stop-opacity=".66"/>
  </linearGradient>
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency=".72" numOctaves="3" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/>
  </filter>
</defs>
"""


def save(filename, content, width=800, height=500, grain=True):
    texture = f'<rect width="{width}" height="{height}" filter="url(#grain)" opacity=".052"/>' if grain else ""
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">{DEFS}{content}{texture}</svg>'
    (OUT / filename).write_text(svg, encoding="utf-8")


def glass_block(x, y, size, height=None, solid=False):
    height = height if height is not None else size * 1.14
    dy = size * .45
    a, b, c, d = (x, y), (x + size, y + dy), (x, y + 2 * dy), (x - size, y + dy)
    down = lambda p: (p[0], p[1] + height)
    rim = "#ffbcb1"
    return "".join([
        line([down(d), down(a), down(b)], rim, 1.3, .38),
        line([a, down(a)], rim, 1.05, .46),
        polygon([a, b, c, d], "url(#salmon)" if solid else "url(#glassTop)", rim, 1.25, .99),
        polygon([d, c, down(c), down(d)], "url(#pink)" if solid else "url(#glassA)", rim, 1.15, .96),
        polygon([c, b, down(b), down(c)], "url(#salmon)" if solid else "url(#glassB)", rim, 1.15, .95),
    ])


def make_volume():
    s = '<rect width="800" height="500" fill="url(#bg)"/>'
    s += '<ellipse cx="430" cy="449" rx="245" ry="25" fill="#211e25" opacity=".6"/>'
    s += glass_block(397, 253, 119, 97)
    s += glass_block(279, 308, 92, 78)
    s += glass_block(499, 303, 82, 71)
    s += glass_block(393, 160, 111, 103, True)
    s += glass_block(393, 72, 113, 93)
    return s


def mesh_point(u, v, project):
    if project:
        z = (84 * exp(-((u - .23) / .20) ** 2 - ((v - .58) / .38) ** 2)
             + 95 * exp(-((u - .78) / .24) ** 2 - ((v - .38) / .48) ** 2)
             + 23 * sin(u * 2 * pi + v * 2.7))
        return (-160 + 920 * u + 155 * v, 408 - 168 * v - z * 1.65 + 68 * (u - .5))
    z = 102 * sin(u * 7.5 - 2.2 + v * 2.7) + 21 * cos(v * 5 - u * 4.7)
    return (-142 + u * 920 + v * 180, 405 - v * 178 - z * (0.5 + .58 * sin(pi * v)) + 40 * (u - .5))


def make_mesh(project):
    s = '<rect width="800" height="500" fill="url(#mist)"/>'
    # Back-to-front strips keep the underside of the rolling surface hidden.
    rows, cols = 44, 60
    for j in range(rows, 0, -1):
        v = j / rows
        row = [mesh_point(i / cols, v, project) for i in range(cols + 1)]
        nearer = [mesh_point(i / cols, (j - 1) / rows, project) for i in range(cols + 1)]
        s += polygon(row + list(reversed(nearer)), "#383039" if project else "#332f36")
        s += line(row, "#ffbdba" if project else "#f4c9cf", .85 if project else .82, .65 + .22 * v)
        ribs = " ".join(f"M{row[i][0]:.1f} {row[i][1]:.1f}L{nearer[i][0]:.1f} {nearer[i][1]:.1f}" for i in range(0, cols + 1, 2))
        s += f'<path d="{ribs}" fill="none" stroke="{("#e4a3a7" if project else "#d4aeb3")}" stroke-width=".61" opacity=".65"/>'
    if project:
        highlight = [mesh_point(.15 + .62 * v, v, True) for v in [i / 66 for i in range(67)]]
        s += line(highlight, "#fd967e", 2.8, .98)
        for u, v in [(.15 + .62 * .30, .30), (.15 + .62 * .72, .72)]:
            x, y = mesh_point(u, v, True)
            s += f'<circle cx="{x:.2f}" cy="{y:.2f}" r="6" fill="#f58f7c" stroke="#322831" stroke-width="2"/>'
    return s


def make_certificate():
    s = '<rect width="800" height="500" fill="url(#bg)"/>'
    s += '<circle cx="680" cy="30" r="176" fill="url(#pink)" opacity=".4"/>'
    for n in range(8):
        s += line([(-90 + n * 115, 500), (306 + n * 115, 304)], "#d5a1a4", .8, .22)
        s += line([(120 + n * 116, 500), (-266 + n * 116, 306)], "#d5a1a4", .8, .2)
    s += glass_block(428, 266, 145, 63)
    s += glass_block(428, 171, 145, 68)
    s += glass_block(428, 66, 145, 79)
    s += line([(255, 179), (192, 151), (130, 181)], "#f5b3a6", 1.6, .88)
    s += '<circle cx="127" cy="182" r="4" fill="#faad9e"/>'
    s += line([(575, 299), (622, 321), (669, 298)], "#f5b3a6", 1.6, .88)
    s += '<circle cx="671" cy="297" r="4" fill="#faad9e"/>'
    s += line([(386, 132), (410, 155), (465, 124)], "#ffe2d7", 5, .95)
    return s


def make_steps():
    s = '<rect width="800" height="500" fill="url(#bg)"/>'
    s += polygon([(0, 500), (800, 160), (800, 500)], "#3c353b")
    for x, y, front, side in [
        (464, 112, "url(#pink)", "url(#shadow)"),
        (351, 195, "url(#salmon)", "url(#shadow)"),
        (238, 278, "url(#pink)", "url(#shadow)"),
        (125, 361, "url(#salmon)", "url(#shadow)"),
    ]:
        w, h, dx, dy = 178, 365, 93, -57
        s += polygon([(x, y), (x + dx, y + dy), (x + w + dx, y + dy), (x + w, y)], "#f4c0ba")
        s += polygon([(x + w, y), (x + w + dx, y + dy), (x + w + dx, y + h + dy), (x + w, y + h)], side)
        s += polygon([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], front)
        s += line([(x, y), (x + w, y), (x + w + dx, y + dy)], "#ffe1d3", .9, .7)
    return s


if __name__ == "__main__":
    save("study-volume.svg", make_volume())
    save("study-wave.svg", make_mesh(False))
    save("study-steps.svg", make_steps())
    save("project-pathfinder.svg", make_mesh(True))
    save("project-certificate.svg", make_certificate())
