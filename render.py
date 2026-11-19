"""Draw the original flat infographic. Build dependency: Pillow 10.2.0.

Runtime entry point main.py uses only Python's standard library.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
S = 2
BG = '#F5F3EA'
INK = '#16333E'
MUTED = '#526975'
FONT = Path('/usr/share/fonts/truetype/dejavu')
im = Image.new('RGB', (1024*S, 1024*S), BG)
d = ImageDraw.Draw(im)

def font(size, bold=False):
    return ImageFont.truetype(str(FONT / ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf')), round(size*S))

def rect(box, fill, radius=0, outline=None, width=1):
    coords = tuple(round(v*S) for v in box)
    if radius:
        d.rounded_rectangle(coords, round(radius*S), fill=fill, outline=outline, width=width*S)
    else:
        d.rectangle(coords, fill=fill, outline=outline, width=width*S)

def line(points, fill=INK, width=2):
    d.line([(round(x*S), round(y*S)) for x,y in points], fill=fill, width=width*S, joint='curve')

def circle(x,y,r,fill,outline=None,width=1):
    d.ellipse(tuple(round(v*S) for v in (x-r,y-r,x+r,y+r)), fill=fill, outline=outline, width=width*S)

def text(x,y,t,size,fill=INK,bold=False,anchor=None):
    d.text((round(x*S),round(y*S)),t,font=font(size,bold),fill=fill,anchor=anchor)

def fitted(x,y,t,size,width,fill=INK,bold=False):
    assert d.textlength(t,font=font(size,bold)) <= width*S, (t, width)
    text(x,y,t,size,fill,bold)

# Hand-drawn, generalized land polygons in longitude/latitude. Decorative locator
# map only: no borders, no implied sovereignty, no external map dependency.
LAND = [
 [(-168,70),(-150,72),(-139,66),(-125,70),(-108,72),(-93,77),(-74,72),(-59,54),(-67,46),(-80,25),(-86,22),(-96,16),(-106,23),(-116,31),(-125,49),(-140,59),(-164,60)],
 [(-81,12),(-69,11),(-61,6),(-49,-1),(-35,-7),(-40,-22),(-52,-32),(-64,-55),(-73,-49),(-75,-29),(-81,-8)],
 [(-53,83),(-25,80),(-20,68),(-42,59),(-53,64),(-63,76)],
 [(-17,36),(1,37),(12,33),(31,31),(36,22),(51,12),(43,-2),(39,-16),(30,-34),(18,-35),(10,-20),(10,4),(-6,5),(-17,17)],
 [(-10,36),(-10,44),(-1,49),(-5,58),(11,55),(21,70),(42,69),(65,72),(91,76),(115,73),(139,72),(174,65),(179,51),(159,53),(143,44),(134,33),(120,22),(110,20),(105,2),(99,5),(94,19),(88,22),(79,7),(71,22),(55,25),(48,13),(42,13),(35,31),(29,41),(13,45),(2,43)],
 [(112,-11),(129,-12),(137,-10),(145,-18),(153,-28),(146,-39),(129,-34),(115,-35),(112,-23)],
 [(47,-13),(50,-17),(47,-25),(44,-22)],
 [(130,32),(139,36),(142,44),(146,45),(143,36),(135,30)],
 [(120,18),(125,12),(126,7),(121,5),(118,11)],
 [(96,5),(105,-3),(114,-7),(129,-8),(139,-6),(148,-8),(144,-3),(130,0),(119,1),(111,6),(108,0),(101,1)],
 [(166,-35),(174,-40),(178,-38),(178,-42),(168,-47),(166,-44),(172,-40)],
 [(-8,58),(-2,59),(1,51),(-6,50)],
 [( -25,66),(-14,66),(-13,63),(-22,63)],
]

def inside(x,y,poly):
    hit=False
    for i,(ax,ay) in enumerate(poly):
        bx,by=poly[i-1]
        if (ay>y)!=(by>y) and x<(bx-ax)*(y-ay)/(by-ay)+ax:
            hit=not hit
    return hit

def project(lon,lat):
    return (62+(lon+180)/360*900, 183+(83-lat)/143*270)

text(40,25,'THE WORLD, TODAY',44,bold=True)
text(42,84,'THURSDAY 19 NOVEMBER 2026',32,bold=True)
text(43,133,'SIX STORIES  /  ONE DAY  /  AROUND THE GLOBE',16,MUTED,bold=True)
rect((40,166,984,168),INK)

for lon in range(-178,180,3):
    for lat in range(-55,83,3):
        if any(inside(lon,lat,p) for p in LAND):
            x,y=project(lon,lat)
            circle(x,y,1.65,'#AABFC0')

STORIES = [
 dict(n=1, color='#A84070', place='GLOBAL / SYDNEY', title=['GTA VI rolls out'], sub=['Vice City opens to players as', 'the global console launch begins.'], loc=(151.2,-33.9), pin=(804,433), icon='game', source='REUTERS / MARKETSCREENER'),
 dict(n=2, color='#B4562F', place='INDIA / BAY OF BENGAL', title=['Akvan warning issued'], sub=['IMD issues a 19 Nov bulletin;', 'cyclone nears the east coast.'], loc=(85.3,13.9), pin=(690,349), icon='storm', source='INDIA METEOROLOGICAL DEPARTMENT'),
 dict(n=3, color='#317C83', place='SOUTH KOREA', title=['Suneung exam day'], sub=['Half a million students;', 'AI cheating checks tightened.'], loc=(127,37.6), pin=(858,271), icon='exam', source='AFP / AJU PRESS'),
 dict(n=4, color='#557042', place='AUSTRALIA', title=['The cost of AI power'], sub=['Report warns of data-centre', 'emissions without clean energy.'], loc=(151.2,-27.5), pin=(925,386), icon='server', source='ABC / CLIMATE COUNCIL'),
 dict(n=5, color='#4865A1', place='NEW ZEALAND / AUCKLAND', title=['Inflation stays in focus'], sub=['RBNZ governor flags price risks', 'and an uneven recovery.'], loc=(174.8,-36.8), pin=(916,438), icon='bank', source='RBNZ / SCOOP'),
 dict(n=6, color='#89612F', place='FRANCE / BEAUJOLAIS', title=['Nouveau is here'], sub=['The 2026 Beaujolais Nouveau', 'vintage goes on sale today.'], loc=(4.6,46.2), pin=(491,246), icon='wine', source='LA REVUE DU VIN DE FRANCE / COURSES U'),
]

for s in STORIES:
    x,y=project(*s['loc']); px,py=s['pin']
    line([(x,y),(px,py)],s['color'],2)
    circle(x,y,3.3,s['color'])
    circle(px,py,14,BG)
    circle(px,py,11.5,s['color'])
    text(px,py,str(s['n']),14,'#FFFFFF',True,'mm')

text(42,462,'NUMBERED PINS MATCH THE STORIES BELOW',12,MUTED,bold=True)
text(984,462,'Locator map · not to scale',12,MUTED,anchor='ra')

def icon(kind,x,y,c):
    if kind=='game':
        rect((x,y+7,x+42,y+32),None,9,c,2)
        line([(x+11,y+13),(x+11,y+25)],c)
        line([(x+5,y+19),(x+17,y+19)],c)
        circle(x+30,y+15,2.5,c); circle(x+35,y+23,2.5,c)
    elif kind=='storm':
        for a,b in [(12,255),(192,435)]:
            d.arc(((x+2)*S,(y+2)*S,(x+40)*S,(y+39)*S),a,b,fill=c,width=3*S)
        circle(x+21,y+20,7,None,c,3)
        line([(x+38,y+4),(x+39,y+15),(x+29,y+12)],c,2)
        line([(x+4,y+36),(x+3,y+25),(x+13,y+28)],c,2)
    elif kind=='exam':
        rect((x+4,y,x+32,y+39),None,2,c,2)
        for yy in [10,18,26]: line([(x+10,y+yy),(x+25,y+yy)],c,2)
        line([(x+24,y+37),(x+41,y+13),(x+36,y+9),(x+19,y+33),(x+19,y+40),(x+24,y+37)],c,2)
    elif kind=='server':
        for yy in [0,14,28]:
            rect((x,y+yy,x+39,y+yy+10),None,2,c,2)
            circle(x+6,y+yy+5,1.5,c)
            line([(x+25,y+yy+5),(x+33,y+yy+5)],c,2)
    elif kind=='bank':
        line([(x,y+10),(x+21,y),(x+42,y+10),(x,y+10)],c,2)
        for xx in [6,20,34]: line([(x+xx,y+15),(x+xx,y+33)],c,3)
        line([(x,y+38),(x+42,y+38)],c,3)
    elif kind=='wine':
        line([(x+8,y),(x+34,y),(x+31,y+20),(x+21,y+25),(x+11,y+20),(x+8,y)],c,2)
        line([(x+11,y+13),(x+32,y+13)],c,2)
        line([(x+21,y+25),(x+21,y+38)],c,2)
        line([(x+10,y+39),(x+32,y+39)],c,2)

for i,s in enumerate(STORIES):
    x=40+(i%2)*480; y=494+(i//2)*155
    rect((x,y,x+464,y+142),'#FFFFFF',10)
    rect((x,y+13,x+4,y+129),s['color'],2)
    circle(x+25,y+24,11,s['color'])
    text(x+25,y+24,str(s['n']),13,'#FFFFFF',True,'mm')
    fitted(x+44,y+14,s['place'],12,380,s['color'],True)
    icon(s['icon'],x+19,y+52,s['color'])
    for j,t in enumerate(s['title']): fitted(x+80,y+40+26*j,t,23,370,INK,True)
    for j,t in enumerate(s['sub']): fitted(x+80,y+74+21*j,t,17,370,MUTED)
    fitted(x+80,y+122,s['source'],9,370,MUTED,True)

line([(40,970),(984,970)],INK,1)
text(42,985,'19.11.2026',14,INK,True)
text(984,985,'A day in six stories · Sources & date notes in README',12,MUTED,anchor='ra')
im=im.resize((1024,1024),Image.Resampling.LANCZOS)
im.save(ROOT/'entry.png',format='PNG',optimize=True,compress_level=9)
assert (ROOT/'entry.png').stat().st_size <= 1024*1024
print(f'entry.png: {im.size}, {(ROOT/"entry.png").stat().st_size} bytes')
