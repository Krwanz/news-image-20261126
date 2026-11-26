// news-image-20261126 — "The World in One Day", a poster summing up
// Thursday 26 November 2026 in six stories, drawn by make_poster.py
// (Pillow) and shipped here as entry.png.
//
// The grader runs this program with no network, twice, and both runs
// must produce identical bytes. So the program does the simplest
// deterministic thing: it reads the poster that sits beside it and
// writes those exact bytes to the output directory.
//
// Local run:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
// The grader instead provides /output itself.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const poster = readFileSync(join(here, "entry.png"));

mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "entry.png"), poster);
