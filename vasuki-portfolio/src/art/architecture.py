"""A concrete cantilever drawn in perspective, printed over the introduction's coral disc."""

from random import Random

from studies import OUT, line, polygon
rng = Random(76)


def mix(a, b, t):
    return (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))


def face(tl, tr, br, bl, fill, cols, rows, joints, pits=True):
    def point(u, v):
        return mix(mix(tl, tr, u), mix(bl, br, u), v)
    art = polygon([tl, tr, br, bl], fill)
    for col in range(cols):
        u0, u1 = col / cols, (col + 1) / cols
        for row in range(rows):
            v0, v1 = row / rows, (row + 1) / rows
            tile = [point(u0, v0), point(u1, v0), point(u1, v1), point(u0, v1)]
            art += polygon(tile, "#f5f2e9" if rng.random() > .53 else "#363439", "none", 0, rng.uniform(.013, .09))
            if pits:
                for u in (u0 + (u1-u0)*.18, u1 - (u1-u0)*.18):
                    x, y = point(u, v0 + (v1-v0)*.20)
                    art += f'<circle cx="{x:.1f}" cy="{y:.1f}" r=".94" fill="#363338" opacity=".44"/>'
    for i in range(1, cols):
        art += line([point(i/cols, 0), point(i/cols, 1)], joints, .9, .72)
    for i in range(1, rows):
        art += line([point(0, i/rows), point(1, i/rows)], joints, .9, .72)
    return art


def draw():
    art = ''
    art += face((276, 555), (642, 319), (642, 715), (276, 715), "url(#concrete)", 10, 8, "#686665")
    art += face((642, 319), (819, 394), (819, 715), (642, 715), "url(#right)", 5, 8, "#37363a")
    art += polygon([(0,693), (270,554), (425,512), (317,693)], "#a9a6a4")
    left, corner, right = (27, 453), (548, 85), (813, 204)
    bottom = [(27, 531), (548, 380), (813, 432)]
    art += polygon([bottom[0], bottom[1], bottom[2], (611, 510), (216, 624)], "url(#soffit)")
    for i in range(1, 11):
        art += line([mix(bottom[0],bottom[1],i/11), mix((216,624),(611,510),i/11)], "#49474a", 1, .64)
    for i in range(1, 4):
        art += line([mix(bottom[0],(216,624),i/4), mix(bottom[1],(611,510),i/4)], "#49474a", 1, .7)
    for a, b, ba, bb, light in [(left, corner, bottom[0], bottom[1], True), (corner, right, bottom[1], bottom[2], False)]:
        def section(v):
            return (mix(a, ba, v), mix(b, bb, v))
        top_l, top_r = section(0)
        slot_l, slot_r = section(.48)
        end_l, end_r = section(.80)
        art += face(top_l, top_r, slot_r, slot_l, "url(#concrete)" if light else "url(#right)", 12 if light else 6, 3, "#76736e")
        art += face(slot_l, slot_r, end_r, end_l, "url(#windows)", 17 if light else 7, 1, "#6b686a", False)
        art += face(end_l, end_r, bb, ba, "url(#concrete)" if light else "url(#right)", 12 if light else 6, 2, "#686764")
        art += line([top_l, top_r], "#f1eae2", 1.4, .75)
        art += line([slot_l, slot_r], "#74706f", 1.2, .8)
        art += line([end_l, end_r], "#e1d9d1", 1.3, .87)
    defs = '''<defs>
      <linearGradient id="concrete" x1="0" x2=".9" y1=".8" y2="0"><stop stop-color="#a8a5a2"/><stop offset=".55" stop-color="#ccc9c2"/><stop offset="1" stop-color="#e2ded5"/></linearGradient>
      <linearGradient id="right" x1="0" y1=".2" x2="1" y2=".6"><stop stop-color="#9d9997"/><stop offset="1" stop-color="#686768"/></linearGradient>
      <linearGradient id="windows"><stop stop-color="#716e6d"/><stop offset=".44" stop-color="#363538"/><stop offset=".75" stop-color="#4f4e4e"/><stop offset="1" stop-color="#2c2b30"/></linearGradient>
      <linearGradient id="soffit" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#6b6868"/><stop offset=".6" stop-color="#3d3c40"/><stop offset="1" stop-color="#28282b"/></linearGradient>
      <filter id="aggregate" x="0" y="0" width="100%" height="100%">
        <feTurbulence type="fractalNoise" baseFrequency=".69" numOctaves="3" stitchTiles="stitch" result="noise"/>
        <feColorMatrix in="noise" type="saturate" values="0" result="mono"/>
        <feComposite in="mono" in2="SourceGraphic" operator="in" result="masked"/>
        <feComponentTransfer in="masked" result="texture"><feFuncA type="linear" slope=".15"/></feComponentTransfer>
        <feBlend in="SourceGraphic" in2="texture" mode="multiply"/>
      </filter></defs>'''
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="800" height="680" viewBox="0 0 800 680">{defs}<g filter="url(#aggregate)">{art}</g></svg>'


if __name__ == "__main__":
    (OUT / "about-architecture.svg").write_text(draw(), encoding="utf-8")
