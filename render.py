"""Draw an original, static news atlas. Build-time dependency: Pillow."""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
S = 2
im = Image.new('RGB', (1024*S, 1024*S), '#F5F2E9')
d = ImageDraw.Draw(im)
NAVY = '#142F40'
MUTED = '#526570'
COLORS = ['#A64B73', '#C35436', '#246F97', '#377A65', '#7060A0', '#9A7028']
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(n, bold=False): return ImageFont.truetype(BOLD if bold else FONT, n*S)
def text(x, y, value, n=18, fill=NAVY, bold=False): d.text((x*S,y*S), value, font=font(n,bold), fill=fill)
def line(points, fill, width=1): d.line([(x*S,y*S) for x,y in points], fill=fill, width=width*S)
def ellipse(box, fill, outline=None, width=1): d.ellipse(tuple(int(v*S) for v in box),fill=fill,outline=outline,width=width*S)
def rect(box, fill, radius=0, outline=None, width=1): d.rounded_rectangle(tuple(v*S for v in box), radius=radius*S,fill=fill,outline=outline,width=width*S)

def pin(x,y,num,color):
    ellipse((x-17,y-17,x+17,y+17), '#F5F2E9')
    ellipse((x-14,y-14,x+14,y+14),color)
    label=str(num); box=d.textbbox((0,0),label,font=font(15,True))
    d.text((x*S-(box[2]-box[0])/2,(y-11)*S),label,font=font(15,True),fill='white')

text(38,25,'THE WORLD / ONE DAY',15,bold=True)
text(38,53,'THURSDAY 19 NOVEMBER 2026',36,bold=True)
text(40,107,'Six signals from a connected planet',21,fill=MUTED)
line([(38,145),(986,145)],NAVY,2)

# Hand-drawn, deliberately simplified land silhouettes sampled into a dot atlas.
continents = [
 [(-168,70),(-145,71),(-130,59),(-123,51),(-125,42),(-114,30),(-99,18),(-84,9),(-79,9),(-87,22),(-81,26),(-81,32),(-67,46),(-55,51),(-65,59),(-85,63),(-100,73),(-130,72)],
 [(-73,60),(-49,61),(-25,80),(-45,84),(-63,77)],
 [(-81,12),(-65,10),(-50,0),(-35,-8),(-42,-23),(-54,-35),(-68,-55),(-75,-43),(-70,-20),(-80,-4)],
 [(-10,36),(-17,17),(-15,5),(-3,4),(10,-5),(12,-18),(20,-35),(32,-32),(43,-12),(50,10),(39,16),(33,30),(12,37)],
 [(-11,36),(-10,57),(5,59),(17,71),(30,70),(34,58),(56,70),(90,76),(130,71),(174,64),(160,52),(143,45),(130,35),(122,21),(106,7),(96,7),(82,23),(75,7),(68,22),(47,31),(36,42),(25,36),(15,41),(3,43)],
 [(95,5),(106,-6),(116,-8),(130,-5),(139,-8),(152,-5),(148,-11),(130,-10),(113,-10),(102,-4)],
 [(113,-22),(122,-15),(132,-12),(141,-11),(153,-26),(151,-38),(137,-39),(126,-33),(115,-34)],
 [(166,-34),(178,-38),(173,-42),(167,-47),(164,-44),(171,-39)],
 [(46,-13),(50,-16),(49,-25),(44,-25)], [(130,32),(135,34),(141,43),(145,45),(142,35)]
]
def project(lon,lat): return (70+(lon+180)/360*884, 166+(82-lat)/142*283)
def inside(x,y,p):
    result=False
    for i in range(len(p)):
        a,b=p[i-1],p[i]
        if (a[1]>y)!=(b[1]>y) and x<(b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]: result=not result
    return result
for lat in range(-55,82,4):
    for lon in range(-178,179,4):
        if any(inside(lon,lat,p) for p in continents):
            x,y=project(lon,lat); ellipse((x-1.7,y-1.7,x+1.7,y+1.7),'#B3C0BA')
places=[(-80,26),(85,14),(127,37),(134,-25),(174,-37),(4.6,46)]
for i,(lon,lat) in enumerate(places):
    x,y=project(lon,lat); pin(x,y,i+1,COLORS[i])
text(40,455,'LOCATIONS ARE APPROXIMATE',11,fill=MUTED)
text(730,455,'EVENTS + REPORTS / 19 NOV',11,fill=MUTED)

def icon(kind,x,y,c):
    if kind==0:
        rect((x,y+9,x+46,y+37),None,10,c,3)
        line([(x+9,y+23),(x+21,y+23)],c,3);line([(x+15,y+17),(x+15,y+29)],c,3)
        ellipse((x+31,y+18,x+36,y+23),c);ellipse((x+37,y+25,x+42,y+30),c)
    elif kind==1:
        for r,start,end in [(21,15,285),(14,180,465),(7,20,290)]:
            d.arc(((x+23-r)*S,(y+23-r)*S,(x+23+r)*S,(y+23+r)*S),start,end,fill=c,width=3*S)
        ellipse((x+20,y+20,x+26,y+26),c)
    elif kind==2:
        rect((x+6,y+2,x+39,y+44),None,3,c,3)
        for yy in [13,23,33]: line([(x+15,y+yy),(x+31,y+yy)],c,2)
    elif kind==3:
        for yy in [2,17,32]:
            rect((x+2,y+yy,x+44,y+yy+11),None,2,c,2);ellipse((x+7,y+yy+4,x+10,y+yy+7),c)
    elif kind==4:
        line([(x+3,y+2),(x+3,y+42),(x+45,y+42)],c,3)
        line([(x+9,y+31),(x+20,y+20),(x+30,y+25),(x+43,y+9)],c,3)
        line([(x+34,y+9),(x+43,y+9),(x+43,y+18)],c,3)
    else:
        d.arc((x*S,y*S,(x+44)*S,(y+38)*S),0,180,fill=c,width=3*S)
        line([(x,y+19),(x,y+2),(x+44,y+2),(x+44,y+19)],c,3)
        line([(x+22,y+38),(x+22,y+47)],c,3);line([(x+11,y+47),(x+33,y+47)],c,3)

stories=[
 ('GLOBAL / VICE CITY','GTA VI arrives','The long-awaited global launch begins.'),
 ('BAY OF BENGAL','Akvan warning','IMD issues a fresh cyclone bulletin.'),
 ('SOUTH KOREA','Exam day, AI checks','Suneung proceeds under tighter scrutiny.'),
 ('AUSTRALIA','Data-centre warning','Report flags emissions risk without renewables.'),
 ('NEW ZEALAND','Inflation in focus','RBNZ governor cites an uneven recovery.'),
 ('FRANCE / WORLDWIDE','Nouveau is here','The 2026 Beaujolais vintage goes on sale.')
]
for i,(place,title,sub) in enumerate(stories):
    x=38+(i%2)*484; y=494+(i//2)*153; c=COLORS[i]
    rect((x,y,x+464,y+137),'#FFFFFF',12)
    rect((x,y+13,x+4,y+124),c,2)
    icon(i,x+19,y+48,c)
    text(x+80,y+17,f'{i+1:02d}  {place}',12,c,True)
    text(x+80,y+43,title,24,bold=True)
    # Sublines have deliberate, fixed wraps; no variable-width auto-layout.
    words=sub.split(); first=''
    while words and d.textlength((first+' '+words[0]).strip(),font=font(14))<=350*S:
        first=(first+' '+words.pop(0)).strip()
    text(x+80,y+80,first,14,fill=MUTED)
    if words: text(x+80,y+101,' '.join(words),14,fill=MUTED)
line([(38,972),(986,972)],'#C9CEC7')
text(38,986,'A DAILY ATLAS',12,bold=True)
text(686,986,'SOURCE NOTES IN README',12,fill=MUTED)
im.resize((1024,1024),Image.Resampling.LANCZOS).save(ROOT/'entry.png',optimize=True)
print('Rendered', ROOT/'entry.png')
