from PIL import Image, ImageDraw
COLORS=["#dc2626","#2563eb","#16a34a","#eab308","#fdba74","#f8fafc"]
def make(sz):
    img=Image.new("RGBA",(sz,sz),(15,23,42,255))
    d=ImageDraw.Draw(img)
    # rounded bg
    r=int(sz*0.18)
    d.rounded_rectangle([0,0,sz-1,sz-1],radius=r,fill=(15,23,42,255))
    # 6 color dots in 2x3 grid
    pad=int(sz*0.18); gap=int(sz*0.06)
    cols,rows=2,3
    cw=(sz-2*pad-(cols-1)*gap)/cols
    ch=(sz-2*pad-(rows-1)*gap)/rows
    for i,c in enumerate(COLORS):
        cx=i%2; cy=i//2
        x0=pad+cx*(cw+gap); y0=pad+cy*(ch+gap)
        rad=int(min(cw,ch)*0.16)
        outline=(255,255,255,60) if c!="#f8fafc" else (148,163,184,255)
        d.rounded_rectangle([x0,y0,x0+cw,y0+ch],radius=rad,fill=c,outline=outline,width=max(2,sz//120))
    img.save(f"rwb-site/icon-{sz}.png")
for s in (192,512): make(s)
# maskable (more padding) 512
img=Image.new("RGBA",(512,512),(15,23,42,255))
img.save("rwb-site/icon-512.png") if False else None
print("icons done")
