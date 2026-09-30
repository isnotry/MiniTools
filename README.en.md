# MiniTools · Single-file Toolbox

[简体中文](README.md) | **English**

![No network requests](https://img.shields.io/badge/network%20requests-0-brightgreen)
![No build step](https://img.shields.io/badge/build-none-lightgrey)
![11 tools](https://img.shields.io/badge/tools-11-blue)
![Local-only data](https://img.shields.io/badge/data-local--only-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-blue)

> Eleven pure front-end tools, each one a single `index.html` you can double-click — your images and data never leave the browser.

![Screenshot](https://cdn.jsdelivr.net/gh/isnotry/MiniTools@main/docs/screenshot-en.png)

**[Use it online](https://isnotry.github.io/MiniTools/)**

---

## What it is

MiniTools is a set of web tools that need no install, no network and no server: image splitting, batch conversion, watermarking, blurring, stitching and background removal, plus JSON formatting, flowchart editing, HTML-to-PDF, spreadsheet merging and barcode generation.

Each tool lives in its own directory and consists of a single `index.html` (HTML, CSS and JavaScript all inlined). The repository root ships a landing page, [`index.html`](./index.html). Every third-party library is vendored into its tool directory, so the whole thing makes **zero network requests** from the moment you open it until the file is exported.

> Note: every page has a `中` / `EN` switch in the top-right corner, so the whole interface is available in both languages.

## Features

- **Zero install, zero build** —— plain static single files, no Node, no npm, no bundler; double-click and go
- **Works offline** —— Mermaid, SheetJS, JSZip, JsBarcode, Vue 3, heic2any and html2pdf are all loaded from disk; nothing external is fetched at runtime
- **Nothing leaves your browser** —— images, spreadsheets and JSON are processed in local memory; there is no upload endpoint and no backend at all
- **One consistent design language** —— every tool follows Next.js / Geist styling: near-black foreground `#171717`, pure white surface, hairline grey borders, black pill primary button
- **Light and dark themes** —— follows `prefers-color-scheme` by default, with a manual toggle in the top-right corner that remembers your choice
- **Bilingual interface** —— every page has a `中` / `EN` switch in the top-right corner; the choice is stored under `lang` and follows your browser language by default
- **Covers everyday chores** —— 6 image tools, 4 document/data tools and 1 barcode tool, 11 in total
- **Responsive** —— the card grid collapses to a single column on narrow screens, so it works on phones too
- **Docs included** —— every tool folder ships its own `README.md` describing features, usage and dependencies
- **MIT licensed** —— modify and redistribute freely

## Quick start

### Use it online

Open **[Use it online](https://isnotry.github.io/MiniTools/)** — no install, no sign-up.

### Run it locally

Download the repository and open the landing page:

```bash
open MiniTools/index.html        # macOS
start MiniTools\index.html       # Windows
xdg-open MiniTools/index.html    # Linux
```

You can also grab just one tool — it is self-contained:

```bash
git clone git@github.com:isnotry/MiniTools.git
```

## Tools

| Tool | What it does | Open | Docs |
| --- | --- | --- | --- |
| Image Splitter | Grid / smart slice / smart crop / free selection, exported as ZIP | [Open](./image-splitter/index.html) | [Docs](./image-splitter/README.md) |
| Image Batch | Convert formats (HEIC / JPG / PNG / WebP), resize and compress up to 99 files, showing before → after sizes | [Open](./image-batch/index.html) | [Docs](./image-batch/README.md) |
| Image Watermark | Tiled or positioned text / image watermark with opacity, size, rotation and spacing controls | [Open](./image-watermark/index.html) | — |
| Image Blur | Brush-on mosaic, blur or solid block over selected areas, with undo and redo | [Open](./image-mosaic/index.html) | [Docs](./image-mosaic/README.md) |
| Image Stitch | Lay out multiple photos into one sheet automatically, with drag-to-reorder | [Open](./image-stitch/index.html) | [Docs](./image-stitch/README.md) |
| Background Remover | Detect the background colour and remove it in one click, with tolerance, feathering and an eraser | [Open](./image-cutout/index.html) | [Docs](./image-cutout/README.md) |
| JSON Formatter | Validate, format and minify JSON, pinpoint errors by line and column, sort keys and download | [Open](./json-formatter/index.html) | [Docs](./json-formatter/README.md) |
| Flowchart Editor | Mermaid-based diagram editor with live preview, PNG / SVG export | [Open](./mermaid-editor/index.html) | [Docs](./mermaid-editor/README.md) |
| HTML to PDF | Paste or upload HTML, preview it live, then export to PDF with page size and margins | [Open](./html-to-pdf/index.html) | [Docs](./html-to-pdf/README.md) |
| Spreadsheet Merge | Upload two sheets, pick the key columns, then full / inner / left / right join and export xlsx | [Open](./table-merge/index.html) | [Docs](./table-merge/README.md) |
| Barcode Generator | Generate 1D barcodes in bulk, export PNG or ZIP | [Open](./barcode/index.html) | [Docs](./barcode/README.md) |

## UI reference

| Where | Element | Purpose |
| --- | --- | --- |
| Top-right of every page | Theme button 🌙 / ☀️ | Switches light and dark; the choice is stored under `theme` and shared by the landing page and all 11 tools |
| Left of the theme button | Language button `中` / `EN` | Switches Chinese and English; the choice is stored under `lang` and shared by all 12 pages |
| Left of the language button | GitHub Star button ⭐ / Star | Opens the `isnotry/MiniTools` repository; on narrow screens only the ⭐ icon is shown |
| Middle of the landing page | Tool cards | Click to enter a tool |
| Bottom of the landing page | GitHub repository | Opens the source repository |
| Top of each tool page | Title + subtitle | The subtitle states in one line what the tool does and that it runs locally |
| Middle of image tools | Canvas preview | Preview is real; export re-renders at full source resolution |
| Feedback | Toast / status bar | Success and info use inverted foreground; only errors get the semantic red |

## Dependencies

Third-party libraries are vendored per tool — no CDN anywhere:

| Tool | Local dependency | Size |
| --- | --- | --- |
| Flowchart Editor | Mermaid | about 3.2 MB |
| Image Batch | heic2any + JSZip | about 1.4 MB |
| Spreadsheet Merge | SheetJS + Vue 3 | about 1.0 MB |
| HTML to PDF | html2pdf.bundle | about 885 KB |
| Barcode Generator | JsBarcode + JSZip | about 155 KB |
| Image Splitter, Image Watermark | JSZip | about 95 KB each |
| Background Remover, Image Blur, Image Stitch, JSON Formatter | none | 0 |

Only tools that need to package several files pull in JSZip; the rest are native implementations.

## How it works

**Image Stitch · automatic column count** ([source](./image-stitch/index.html))

```js
cols = Math.ceil(Math.sqrt(n * ratio));                          // ratio = cell aspect
cols = Math.max(1, Math.min(Math.min(n, MAX_AUTO_COLS), cols));
rows = Math.ceil(n / cols);
```

- The goal is to keep the finished sheet close to the chosen aspect ratio rather than simply filling rows
- Short last rows can either stretch to fill or stay centred with the columns aligned

**Background Remover · background decision** ([source](./image-cutout/index.html))

```js
band = clamp(round(min(W, H) * 0.04), 2, 128);   // sample only the four border strips
d    = sqrt(dr² + dg² + db²) / √3;                // colour distance normalised to 0-255
d <= t        → alpha = 0
d >= t + soft → alpha = 255
otherwise     → alpha = 255 * (d - t) / soft       // soft = feather × 2.5 + 1
```

- Border pixels are quantised to 4 bits and counted into a histogram; the top 3 most frequent colours are treated as background
- With "keep interior regions of the same colour" enabled, a flood fill starts from the four borders so only connected candidates become background
- Manual erase / restore strokes live in a separate `delta` layer, so changing the tolerance does not discard your edits

**JSON Formatter · locating errors** ([source](./json-formatter/index.html))

```js
pos  = parseInt(/position\s+(\d+)/i.exec(err.message)[1], 10);   // character offset from the engine
line = raw.slice(0, pos).split('\n').length;
col  = pos - raw.slice(0, pos).lastIndexOf('\n');
```

- If no `position` is found, the raw engine message is shown as-is instead of guessing

## Data & privacy

- No backend: the repository contains no server-side code and nothing that calls an external address
- Files are read and processed in your own browser; exports download through a local Blob
- The only things written to your machine are two preferences:

| Storage | Key | Content |
| --- | --- | --- |
| localStorage | `theme` | `light` or `dark`, the theme you picked manually; shared by the landing page and all 11 tools |
| localStorage | `lang` | `zh` or `en`, the interface language you picked manually; shared by all 12 pages |

## Project layout

```text
MiniTools/
├── index.html                  # landing page with all tool cards
├── README.md                   # Chinese version
├── README.en.md                # this file
├── LICENSE                     # MIT license
├── scripts/                    # developer self-check script (untranslated strings)
│   └── check_i18n.py
├── docs/                       # design spec and README screenshots
│   ├── design.md               # shared design spec (Next.js / Geist style)
│   ├── screenshot.png          # Chinese UI cover
│   └── screenshot-en.png       # English UI cover
├── image-splitter/             # grid / smart slice / smart crop / free selection
├── image-batch/                # convert / resize / compress
├── image-watermark/            # tiled or positioned watermark
├── image-mosaic/               # brush-on mosaic and blur
├── image-stitch/               # photo collage
├── image-cutout/               # background removal
├── json-formatter/             # validate, format, minify
├── mermaid-editor/             # flowchart editor
├── html-to-pdf/                # render to PDF
├── table-merge/                # spreadsheet joins
├── barcode/                    # bulk barcode generator
└── <tool>/vendor/              # third-party libs for that tool (kept offline)
```

## Design system

Every tool follows [`docs/design.md`](./docs/design.md); the essentials:

- **Colour** —— near-black foreground `#171717`, pure white surface, hairline borders `#eaeaea`; the accent blue `#0070f3` is reserved for links, focus rings and branding, never for buttons
- **Buttons** —— black pill primary with inverted foreground; secondary and ghost buttons use grey borders
- **Feedback** —— toasts use inverted foreground for success and info; red is the only semantic colour, reserved for errors
- **Type** —— system font stack first (`-apple-system` / `Segoe UI` / `PingFang SC`), no web fonts, saving one more request
- **Dark mode** —— driven by `<html class="dark">` with two sets of variables under `:root` and `:root.dark`, no branchy CSS

## Development notes

- **Adding a language** —— every page carries a `/* ========== 中英切换 ========== */` block before `</body>` (plus a small lang-detection snippet in `<head>`). Copy the whole block into a new tool and **replace only `MAP` (Chinese → English pairs) and `PAIRS` (fragment replacements for dynamically composed strings)**; the page keeps its Chinese source text and English lives in the table alone. At runtime the block walks text nodes plus `placeholder` / `title` / `aria-label`, and a `MutationObserver` covers strings inserted by JavaScript later. If a page uses `alert` / `confirm`, wrap that copy in `window.mtT()`
- **Spotting untranslated strings** —— `python3 scripts/check_i18n.py <page path>` lists Chinese that has no entry yet, split into text / attr / js. It is an offline, dependency-free helper for developers
- **Adding a tool** —— copy the most recent dependency-free tool (e.g. `image-mosaic/index.html`) as your skeleton and keep its tokens, cards, buttons, toasts and theme toggle; default values stay consistent (spacing 12, outer margin 16, single cell 600)
- **Vendoring is mandatory** —— put new libraries in `<tool>/vendor/` and load them by relative path; **never point at a CDN**, or you break offline usage
- **Colour and radius** —— always through CSS variables, never hardcoded; dark mode lives in `:root.dark`
- **No flash** —— the inline script that reads `theme` must run synchronously in `<head>`; anything later shows a white flash
- **Local check** —— serve the repository root and open each tool with the console open (avoid debugging `vendor/` loading over `file://`):

```bash
python3 -m http.server 8765 --bind 127.0.0.1 --directory .
```

- **Keep docs in sync** —— when you add or change a capability, update four places: the tool page subtitle, the tool folder's `README.md`, the tool table and layout above, and the card description in [`index.html`](./index.html)

## Browser support

| Case | Requirement | Known limits |
| --- | --- | --- |
| All tools | Canvas 2D, File API and Blob download (recent two years of Chrome / Edge / Safari / Firefox) | Legacy engines such as IE are not supported |
| HEIC input | Your browser must decode HEIC natively; heic2any does the transcoding | A file that fails to decode is flagged; the remaining files continue processing |
| Flowchart Editor | Mermaid loads from disk, about 3.2 MB | First render is slower; being offline changes nothing |
| HTML to PDF | Relies on the browser's print pipeline | On mobile use the system "Print → Save as PDF" instead |

## License

[MIT](LICENSE) © 2026 isnotry
