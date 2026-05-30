from datetime import date, timedelta

ORDER = ["Red","Blue","Green","Yellow","Peach","White"]  # rotation of "new" color
TR = {"Red":"Kirmizi","Blue":"Mavi","Green":"Yesil","Yellow":"Sari","Peach":"Seftali","White":"Beyaz"}
ANCHOR = date(2026,5,27)   # White becomes new
ANCHOR_IDX = 5             # index of White in ORDER

def period_start(d):
    t = d
    while t.weekday() not in (2,6):  # Wed=2, Sun=6
        t -= timedelta(days=1)
    return t

def period_counter(d):
    # count Wed/Sun boundaries from a fixed epoch to period_start(d)
    epoch = date(2025,1,1)
    ps = period_start(d)
    t = period_start(epoch)
    c = 0
    while t <= ps:
        c += 1
        t += timedelta(days=1)
        while t.weekday() not in (2,6):
            t += timedelta(days=1)
    return c

BASE = period_counter(ANCHOR)

def status_for(d):
    new_idx = (ANCHOR_IDX + (period_counter(d)-BASE)) % 6
    out = {}
    for i,c in enumerate(ORDER):
        age = (new_idx - i) % 6
        if age == 0:   out[c] = "NEW (full price)"
        elif age <=2:  out[c] = "Full price"
        elif age <=4:  out[c] = "50% OFF"
        else:          out[c] = "75% OFF"
    return new_idx, out

# ---- verify against the 5 photos ----
photos = [
 (date(2026,5,15), "Blue",  {"Peach":"50% OFF","Yellow":"50% OFF","Green":"75% OFF"}),
 (date(2026,5,18), "Green", {"White":"50% OFF","Peach":"50% OFF","Yellow":"75% OFF"}),
 (date(2026,5,22), "Yellow",{"Red":"50% OFF","White":"50% OFF","Peach":"75% OFF"}),
 (date(2026,5,25), "Peach", {"Blue":"50% OFF","Red":"50% OFF","White":"75% OFF"}),
 (date(2026,5,29), "White", {"Green":"50% OFF","Blue":"50% OFF","Red":"75% OFF"}),
]
allok=True
for d,newc,board in photos:
    nidx,out = status_for(d)
    ok = ORDER[nidx]==newc
    for col,disc in board.items():
        if out[col]!=disc: ok=False
    allok = allok and ok
    print(d, "new=",ORDER[nidx], "OK" if ok else "MISMATCH", out)
print("ALL PHOTOS MATCH:", allok)
