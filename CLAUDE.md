# CLAUDE.md

## Project

Course website for USP 410/510 Urban Data Science (Portland State University, Spring 2026), hosted on GitHub Pages at usp510.github.io.

## Build

- Run `uv run build.py` to regenerate `syllabus.html`, `resources.html`, and slide PDFs
- `index.html` is hand-crafted — edit directly, not via the build script
- `syllabus.md` and `resources.md` are the source of truth for those pages
- `style.css` is shared across all pages and includes `@media print` rules for the 1-page flyer PDF
- Flyer PDF build is currently commented out in `build.py` (weasyprint dependency disabled)

## Slides

- Slides use [Slidev](https://sli.dev/) and live at the repo root as `week<N>_slides.md`
- `build.py` auto-exports each `*_slides.md` to PDF via `npx slidev export`
- `build.py` auto-injects `[Slides](weekN_slides.pdf)` links into the syllabus schedule table for weeks that have a corresponding PDF
- Preview slides locally: `npx slidev week<N>_slides.md`
- Slidev dependencies (`@slidev/cli`, `@slidev/theme-seriph`, `playwright-chromium`) are managed via `pnpm` in the root `package.json`
- The `node_modules/` directory is gitignored; run `pnpm install` after a fresh clone

## Conventions

- Use `uv run build.py` (not `python build.py`) — dependencies are declared inline via PEP 723
- All site files live at the repo root (no `docs/` subdirectory) for GitHub Pages compatibility
- The `2023` branch preserves the old site; `main` is the active branch
- After editing `syllabus.md` or `resources.md`, always run the build script to regenerate HTML
- After creating or editing `*_slides.md`, run the build script to regenerate slide PDFs and update syllabus links
