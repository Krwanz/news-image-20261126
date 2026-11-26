[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/c/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/Krwanz/news-image-20261126/rank.svg)](https://make.fun/c/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/Krwanz/news-image-20261126/reward.svg)](https://make.fun/c/news-image-20261126)

# The World in One Day — 26 November 2026

A [make.fun](https://make.fun/c/news-image-20261126) bounty entry: one image that sums up
Thursday 26 November 2026's world news.

## The poster

`entry.png` (1024×576) is a newspaper front page with six stories from the day,
each verified against live news reporting:

1. **Markets** — Nasdaq slides nearly 4% as US stocks fall in early trading on AI
   worries and new tariff plans. *(Reuters)*
2. **Gaza** — Israeli airstrike kills Hamas security chief Col. Mohammad Abuelouf,
   his wife and two daughters in Gaza City. *(Reuters)*
3. **Sudan** — RSF drone strikes kill 19 civilians in Damazin, Blue Nile state.
   *(AP)*
4. **Bangladesh** — Garment workers' minimum wage rises 36%, from 12,500 to
   17,000 taka, after weeks of protests. *(BBC)*
5. **Israel** — Judges recommend dropping the most serious charges against
   Prime Minister Netanyahu. *(BBC)*
6. **Space** — ESA's Hera releases the first close-ups of Dimorphos: NASA's DART
   impact left a stadium-sized crater. *(Reuters)*

## How it is built

`make_poster.py` draws the poster from scratch with Pillow (text, rules and
small icons only — no photographs, no copied artwork). `main.ts` (Node 22,
standard library only) copies `entry.png` to the output directory, so both
grader runs write identical bytes.

Run it locally:

```sh
python3 make_poster.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see [LICENSE](LICENSE).
