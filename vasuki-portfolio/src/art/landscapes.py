"""Editorial landscapes used when photographic plates are absent."""

from math import exp, sin
from random import Random

from studies import OUT, line, polygon, save
RNG = Random(28)
SKY = '''<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop stop-color="#7c6879"/><stop offset=".53" stop-color="#ec9d93"/><stop offset="1" stop-color="#f7c9aa"/>
</linearGradient></defs><rect width="800" height="500" fill="url(#sky)"/>'''


def farm():
    art = SKY + '<circle cx="600" cy="137" r="67" fill="#fbd6b5" opacity=".88"/>'
    for j in range(4):
        ridge = []
        for x in range(-10, 818, 7):
            height = (40 - j*5)*sin(x/70 + j) + 18*sin(x/30 + j*.6) + 22*sin(x/160)
            ridge.append((x, 179+23*j-height))
        art += polygon(ridge+[(820,500),(-10,500)], ["#b99b9a","#aa8785","#8d7473","#6c6461"][j])
    def edge(x):
        return 285 + 26*sin(x/160) + 9*sin(x/74)
    skyline = [(x,edge(x)) for x in range(-12,820,8)]
    art += polygon(skyline+[(824,500),(-12,500)], "#77715d")
    for i in range(58,-20,-1):
        x0=i*21-180
        stripe = []
        for n in range(51):
            t=n/50
            x=x0 + (x0-380)*t*1.15-124*sin(t*1.85)+20*t
            y=edge(x0)*(1-t) + 518*t + 26*sin(t*2.8)
            stripe.append((x,y))
        lower=[(x + 3+13*(n/50)**1.23,y+2) for n,(x,y) in enumerate(stripe)]
        art += polygon(stripe+list(reversed(lower)),["#4e5948","#566046","#4b5445","#626c4d"][i%4])
        art += line(stripe,["#c9b779","#e0bd79","#a8a978"][i%3],1.7,.85)
    return art


def city():
    art=SKY
    for depth in range(3):
        x=-50
        while x<825:
            w=RNG.randint(29+depth*13,52+depth*17)
            h=RNG.randint(48+depth*20,130+depth*45)
            base=262+depth*105
            y=base-h
            shade=["#aa8d91","#776c74","#49484e"][depth]
            art+=polygon([(x,y),(x+w,y-3),(x+w,base),(x,base)],shade)
            art+=polygon([(x+w,y-3),(x+w+9,y+2),(x+w+9,base),(x+w,base)],["#927d82","#665b64","#393941"][depth])
            for col in range(5,w-3,7+depth):
                art+=line([(x+col,y+5),(x+col,base)],"#dec0b5",.65,.42)
            for row in range(y+7,base,7+depth*2):
                art+=line([(x+1,row),(x+w-1,row-3)],"#24262c",1.15,.32)
            if depth==2:
                for _ in range(19):
                    xx=x+RNG.randrange(2,max(3,w-5))
                    yy=RNG.randrange(y+9,base-4)
                    art+=f'<rect x="{xx}" y="{yy}" width="3" height="2" fill="#f0bd9c" opacity=".71"/>'
            x+=w+RNG.randint(-4,12)
    return art


def parking():
    s='<rect width="800" height="500" fill="#4f4b4d"/>'
    s+=polygon([(0,0),(800,0),(479,231),(297,231)],"#6f6b67")
    s+=polygon([(0,500),(800,500),(510,265),(286,265)],"#77716c")
    s+='<rect x="296" y="227" width="210" height="42" fill="#b19a89"/>'
    for n in range(9,0,-1):
        t=n/9
        w=357*(1-t*.89)
        x=400-w
        top=28+199*t; bot=472-201*t
        width=39*(1-t*.84)
        for xx in [x,800-x-width]:
            s+=polygon([(xx,top),(xx+width,top),(xx+width,bot),(xx,bot+4)],"#8b8480")
            s+=polygon([(xx+width,top),(xx+width+width*.4,top+5),(xx+width+width*.4,bot-1),(xx+width,bot)],"#5a5658")
            s+=polygon([(xx,top+(bot-top)*.66),(xx+width,top+(bot-top)*.66),(xx+width,top+(bot-top)*.72),(xx,top+(bot-top)*.72)],"#e39a85")
        s+=polygon([(x-65,top-24),(800-x+65,top-24),(800-x+62,top-14),(x-59,top-13)],"#514e50")
        s+=line([(x+width+18,top-6),(x+width+30+29*(1-t),top-6)],"#f7deca",2+.8*(1-t))
    for x in [-650,-290,4,245,565,800,1120,1450]:
        s+=line([(410+(x-410)*.13,280),(x,500)],"#d7cec0",2.5,.8)
    for y in [326,364,417]:
        s+=line([(-20,y),(250,y+2)],"#d5ccbb",2.1,.61)
    return s


if __name__=="__main__":
    for key, draw in [("farm",farm),("city",city),("parking",parking)]:
        if not (OUT / f"{key}.webp").exists():
            save(f"scene-{key}.svg", draw())
