#!/usr/bin/env python3
"""Draw the 26 November 2026 world-news poster (1024x576 PNG).

A newspaper front page: masthead with the date, then six story cards,
each with a small hand-drawn icon, a headline and one factual line.
Everything is drawn with Pillow primitives; no external assets.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 576
PAPER = (247, 243, 234)      # warm newsprint
INK = (18, 30, 51)           # deep navy ink
RED = (178, 34, 34)          # accent red
GOLD = (201, 162, 39)
TEAL = (18, 110, 105)
NAVY2 = (38, 64, 110)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

f_mast = ImageFont.truetype(SERIF_B, 44)
f_date = ImageFont.truetype(SANS_B, 19)
f_tag = ImageFont.truetype(SANS_B, 13)
f_head = ImageFont.truetype(SERIF_B, 22)
f_body = ImageFont.truetype(SANS, 16)
f_src = ImageFont.truetype(SANS_B, 12)
f_foot = ImageFont.truetype(SANS, 12)


def wrap(draw, text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def icon_chart(d, x, y, c):
    d.line([(x, y + 26), (x + 12, y + 16), (x + 24, y + 20), (x + 36, y + 4)],
           fill=c, width=4)
    d.polygon([(x + 36, y + 4), (x + 30, y + 4), (x + 36, y + 10)], fill=c)
    d.line([(x, y + 32), (x + 40, y + 32)], fill=c, width=2)


def icon_flame(d, x, y, c):
    d.polygon([(x + 20, y - 2), (x + 32, y + 14), (x + 36, y + 26), (x + 28, y + 36),
               (x + 12, y + 36), (x + 4, y + 26), (x + 8, y + 14)], fill=c)
    d.ellipse([x + 14, y + 20, x + 26, y + 32], fill=(255, 210, 90))


def icon_drone(d, x, y, c):
    d.ellipse([x + 12, y + 12, x + 28, y + 28], fill=c)
    for cx, cy in [(x, y), (x + 40, y), (x, y + 40), (x + 40, y + 40)]:
        d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], outline=c, width=3)
        d.line([(cx, cy), (x + 20, y + 20)], fill=c, width=2)


def icon_shirt(d, x, y, c):
    d.polygon([(x + 12, y + 4), (x + 28, y + 4), (x + 38, y + 12), (x + 34, y + 22),
               (x + 28, y + 16), (x + 28, y + 38), (x + 12, y + 38), (x + 12, y + 16),
               (x + 6, y + 22), (x + 2, y + 12)], fill=c)


def icon_scales(d, x, y, c):
    d.line([(x + 20, y + 2), (x + 20, y + 34)], fill=c, width=3)
    d.line([(x + 4, y + 8), (x + 36, y + 8)], fill=c, width=3)
    d.line([(x, y + 38), (x + 40, y + 38)], fill=c, width=3)
    d.polygon([(x + 2, y + 10), (x + 10, y + 10), (x + 6, y + 20)], fill=c)
    d.polygon([(x + 30, y + 10), (x + 38, y + 10), (x + 34, y + 20)], fill=c)


def icon_rock(d, x, y, c):
    d.ellipse([x + 2, y + 6, x + 38, y + 36], fill=c)
    d.ellipse([x + 12, y + 12, x + 30, y + 26], fill=(247, 243, 234))
    for bx, by in [(x + 36, y), (x, y + 30), (x + 38, y + 34)]:
        d.ellipse([bx, by, bx + 5, by + 5], fill=c)


STORIES = [
    ("MARKETS", RED, icon_chart,
     "Nasdaq slides nearly 4%",
     "US stocks fall in early trading as AI worries and new tariff plans spook investors.",
     "Reuters"),
    ("GAZA", RED, icon_flame,
     "Hamas security chief killed in Gaza strike",
     "Israeli airstrike kills Col. Mohammad Abuelouf, his wife and two daughters in Gaza City.",
     "Reuters"),
    ("SUDAN", TEAL, icon_drone,
     "Sudan drone strikes kill 19",
     "RSF drones hit Damazin in Blue Nile state, killing 19 civilians, a rights group says.",
     "AP"),
    ("BANGLADESH", GOLD, icon_shirt,
     "Garment pay up 36%",
     "Minimum wage rises from 12,500 to 17,000 taka after weeks of factory protests.",
     "BBC"),
    ("ISRAEL", NAVY2, icon_scales,
     "Judges: drop Netanyahu charges",
     "Court recommends the most serious charges against the prime minister be dropped.",
     "BBC"),
    ("SPACE", NAVY2, icon_rock,
     "Asteroid's crater seen up close",
     "ESA's Hera shows NASA's DART left a stadium-sized crater on Dimorphos.",
     "Reuters"),
]

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# Masthead
d.rectangle([0, 0, W, 118], fill=INK)
title = "THE WORLD IN ONE DAY"
tw = d.textlength(title, font=f_mast)
d.text(((W - tw) / 2, 14), title, font=f_mast, fill=PAPER)
date = "THURSDAY  26  NOVEMBER  2026"
dw = d.textlength(date, font=f_date)
d.text(((W - dw) / 2, 72), date, font=f_date, fill=(232, 196, 90))
d.line([(40, 108), (W - 40, 108)], fill=(232, 196, 90), width=2)

# Story grid: 3 columns x 2 rows
GX, GY, CW, CH, GAP = 24, 134, 312, 196, 20
for i, (tag, color, icon, head, body, src) in enumerate(STORIES):
    col, row = i % 3, i // 3
    x = GX + col * (CW + GAP)
    y = GY + row * (CH + GAP)
    d.rectangle([x, y, x + CW, y + CH], outline=(190, 182, 165), width=2)
    d.rectangle([x, y, x + CW, y + 30], fill=color)
    d.text((x + 10, y + 7), tag, font=f_tag, fill=(255, 255, 255))
    icon(d, x + CW - 52, y + 42, color)
    lines = wrap(d, head, f_head, CW - 66)
    ly = y + 40
    for ln in lines[:2]:
        d.text((x + 10, ly), ln, font=f_head, fill=INK)
        ly += 25
    blines = wrap(d, body, f_body, CW - 20)
    by = y + 40 + len(lines[:2]) * 25 + 6
    for ln in blines[:3]:
        d.text((x + 10, by), ln, font=f_body, fill=(52, 58, 68))
        by += 20
    d.line([(x + 10, y + CH - 26), (x + CW - 10, y + CH - 26)], fill=(190, 182, 165), width=1)
    d.text((x + 10, y + CH - 21), "Source: " + src, font=f_src, fill=(110, 104, 90))

# Footer
d.line([(24, H - 26), (W - 24, H - 26)], fill=(190, 182, 165), width=1)
d.text((24, H - 21), "Sources: Reuters  ·  BBC  ·  AP  ·  CNN  —  Thursday's world news, 26 November 2026",
       font=f_foot, fill=(110, 104, 90))

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
