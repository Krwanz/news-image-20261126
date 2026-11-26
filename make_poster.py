#!/usr/bin/env python3
"""Build the news poster for Thursday 26 November 2026.

Fresh rebuild: six verified stories from the day's news cycle, drawn as a
newspaper front page with PIL. Deterministic output: fixed layout, fixed
text, no timestamps, no randomness.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 576
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (246, 241, 231)
INK = (26, 26, 26)
NAVY = (19, 41, 75)
GOLD = (242, 183, 5)
WHITE = (255, 255, 255)
CARD = (255, 255, 255)
GREY = (90, 90, 90)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


STORIES = [
    dict(
        kicker="TRADE",
        accent=(179, 84, 30),
        icon="tariff",
        headline="Trump's new tariff salvo hits 14 partners",
        body="China faces +20%, rising to 40% if the truce fails; the EU, Japan and India are hit too.",
    ),
    dict(
        kicker="ENERGY",
        accent=(192, 57, 43),
        icon="refinery",
        headline="Houthis claim strike on Saudi refinery",
        body="Satellite images show thick black smoke over Ras Tanura; Brent crude jumps past $93 a barrel.",
    ),
    dict(
        kicker="GAZA",
        accent=(91, 91, 138),
        icon="city",
        headline="Israeli strike kills Hamas security chief",
        body="Mohammad Abuelouf, his wife and two daughters die in Gaza City \u2014 the second senior Hamas official killed in 24 hours.",
    ),
    dict(
        kicker="SUDAN",
        accent=(46, 111, 94),
        icon="drone",
        headline="Drone strikes kill 19 civilians in Blue Nile",
        body="RSF drones hit homes in Damazin; 20 wounded. Drones also struck the Roseires dam and power sites.",
    ),
    dict(
        kicker="SPACE",
        accent=(31, 78, 121),
        icon="rocket",
        headline="Pakistan's first astronaut in orbit",
        body="Muhammad Zeeshan Ali docks at China's Tiangong station on Shenzhou-24 \u2014 its first foreign visitor.",
    ),
    dict(
        kicker="INDIA",
        accent=(176, 124, 12),
        icon="candle",
        headline="India marks 18 years since Mumbai attacks",
        body="The nation honours the 26/11 victims and celebrates Constitution Day on 26 November.",
    ),
]


def draw_icon(d, kind, cx, cy, accent):
    """Simple flat pictogram centred at (cx, cy), about 64x52."""
    if kind == "tariff":
        # bar chart + percent
        base = cy + 22
        for i, h in enumerate((16, 26, 38)):
            x0 = cx - 30 + i * 20
            d.rectangle([x0, base - h, x0 + 13, base], fill=accent)
        d.text((cx + 12, cy - 26), "%", font=font(SANS_B, 26), fill=accent)
    elif kind == "refinery":
        # towers + flame
        d.rectangle([cx - 30, cy - 6, cx - 14, cy + 22], fill=accent)
        d.rectangle([cx - 8, cy - 16, cx + 8, cy + 22], fill=accent)
        d.rectangle([cx + 14, cy + 2, cx + 30, cy + 22], fill=accent)
        d.polygon([(cx - 4, cy - 16), (cx + 2, cy - 32), (cx + 8, cy - 16)],
                  fill=(242, 183, 5))
        d.polygon([(cx - 1, cy - 16), (cx + 2, cy - 26), (cx + 5, cy - 16)],
                  fill=(230, 90, 30))
    elif kind == "city":
        # skyline, one building cracked/tilted
        d.rectangle([cx - 32, cy - 4, cx - 16, cy + 22], fill=accent)
        d.rectangle([cx - 12, cy - 18, cx + 4, cy + 22], fill=accent)
        d.polygon([(cx + 8, cy + 22), (cx + 12, cy - 10), (cx + 28, cy - 14),
                   (cx + 30, cy + 22)], fill=accent)
        d.line([cx - 12, cy - 18, cx - 4, cy - 8, cx - 12, cy + 2],
               fill=WHITE, width=2)
        for bx, by in ((-28, 2), (-8, -12), (16, 4)):
            d.rectangle([cx + bx, cy + by, cx + bx + 4, cy + by + 4],
                        fill=(242, 183, 5))
    elif kind == "drone":
        # quadcopter: body + 4 rotors
        d.ellipse([cx - 10, cy - 6, cx + 10, cy + 8], fill=accent)
        d.ellipse([cx - 3, cy - 2, cx + 3, cy + 4], fill=WHITE)
        for sx, sy in ((-26, -16), (26, -16), (-26, 14), (26, 14)):
            d.line([cx, cy, cx + sx, cy + sy], fill=accent, width=2)
            d.ellipse([cx + sx - 9, cy + sy - 3, cx + sx + 9, cy + sy + 3],
                      outline=accent, width=3)
    elif kind == "rocket":
        # rocket + flame + stars
        d.polygon([(cx, cy - 28), (cx - 9, cy - 6), (cx + 9, cy - 6)],
                  fill=accent)
        d.rectangle([cx - 9, cy - 8, cx + 9, cy + 12], fill=accent)
        d.polygon([(cx - 9, cy + 12), (cx - 16, cy + 22), (cx - 9, cy + 16)],
                  fill=accent)
        d.polygon([(cx + 9, cy + 12), (cx + 16, cy + 22), (cx + 9, cy + 16)],
                  fill=accent)
        d.polygon([(cx - 4, cy + 12), (cx, cy + 26), (cx + 4, cy + 12)],
                  fill=(242, 183, 5))
        d.ellipse([cx - 4, cy - 2, cx + 4, cy + 6], fill=WHITE)
        for sx, sy in ((-30, -20), (30, -14), (-28, 14)):
            d.text((cx + sx, cy + sy), "*", font=font(SANS_B, 16),
                   fill=(242, 183, 5))
    elif kind == "candle":
        # memorial candle + flame
        d.rectangle([cx - 7, cy - 2, cx + 7, cy + 22], fill=accent)
        d.rectangle([cx - 11, cy + 22, cx + 11, cy + 26], fill=INK)
        d.polygon([(cx, cy - 26), (cx - 6, cy - 10), (cx + 6, cy - 10)],
                  fill=(242, 183, 5))
        d.polygon([(cx, cy - 20), (cx, cy - 10), (cx + 3, cy - 10)],
                  fill=(230, 90, 30))


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 84], fill=NAVY)
    d.text((18, 12), "THE WORLD IN ONE DAY",
           font=font(SERIF_B, 40), fill=WHITE)
    d.text((18, 58), "Six stories that defined the day",
           font=font(SERIF, 16), fill=(200, 210, 225))
    date_f = font(SANS_B, 21)
    d.text((W - 18 - d.textlength("THURSDAY 26 NOVEMBER 2026", font=date_f),
            16), "THURSDAY 26 NOVEMBER 2026", font=date_f, fill=GOLD)
    d.text((W - 18 - d.textlength("THE DAY IN SIX PICTURES",
                                  font=font(SANS, 13)),
            50), "THE DAY IN SIX PICTURES", font=font(SANS, 13),
           fill=(200, 210, 225))
    d.rectangle([0, 84, W, 88], fill=GOLD)

    # ---- deck ----
    deck = ("A tariff salvo, a refinery in flames, a ceasefire under strain "
            "\u2014 and a first Pakistani in orbit.")
    d.text((18, 98), deck, font=font(SERIF, 17), fill=INK)

    # ---- story grid: 3 x 2 ----
    margin, gutter = 16, 12
    cw = (W - 2 * margin - 2 * gutter) // 3
    ch = 196
    y0 = 132
    for i, s in enumerate(STORIES):
        col, row = i % 3, i // 3
        x = margin + col * (cw + gutter)
        y = y0 + row * (ch + gutter)
        accent = s["accent"]
        d.rectangle([x, y, x + cw, y + ch], fill=CARD, outline=INK, width=2)
        d.rectangle([x, y, x + cw, y + 6], fill=accent)
        # pictogram on tinted panel (left) with text on the right
        d.rectangle([x + 2, y + 8, x + 82, y + 66], fill=(246, 241, 231))
        draw_icon(d, s["icon"], x + 42, y + 38, accent)
        tx = x + 92
        d.text((tx, y + 14), s["kicker"], font=font(SANS_B, 13), fill=accent)
        head_lines = wrap(d, s["headline"], font(SANS_B, 17), cw - 102)[:2]
        hy = y + 34
        for ln in head_lines:
            d.text((tx, hy), ln, font=font(SANS_B, 17), fill=INK)
            hy += 21
        # body under the pictogram row, below however many headline lines
        body_lines = wrap(d, s["body"], font(SANS, 13), cw - 20)[:3]
        by = y + 34 + 21 * len(head_lines) + 8
        for ln in body_lines:
            d.text((x + 10, by), ln, font=font(SANS, 13), fill=(60, 60, 60))
            by += 17
        # thin divider above footer of card
        d.line([x + 10, y + ch - 26, x + cw - 10, y + ch - 26],
               fill=(220, 220, 220), width=1)
        d.text((x + 10, y + ch - 22), "26 NOV 2026",
               font=font(SANS_B, 10), fill=GREY)

    # ---- footer ----
    fy = y0 + 2 * ch + gutter
    d.rectangle([0, fy + 4, W, H], fill=NAVY)
    d.text((18, fy + 16),
           "Sources: Reuters  \u00b7  France 24  \u00b7  Al Jazeera  \u00b7  Xinhua  \u2014  the day's front pages",
           font=font(SANS, 13), fill=WHITE)
    d.text((W - 18 - d.textlength("All six stories reported 25\u201326 November 2026",
                                  font=font(SANS, 13)),
            fy + 16),
           "All six stories reported 25\u201326 November 2026",
           font=font(SANS, 13), fill=(200, 210, 225))

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    build()
