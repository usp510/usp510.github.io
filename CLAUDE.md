# CLAUDE.md

## Project

Course website for USP 410/510 Urban Data Science (Portland State University, Spring 2026), hosted on GitHub Pages at usp510.github.io.

## Build

- Run `uv run build.py` to regenerate `syllabus.html`, `resources.html`, and `flyer.pdf`
- `index.html` is hand-crafted — edit directly, not via the build script
- `syllabus.md` and `resources.md` are the source of truth for those pages
- `style.css` is shared across all pages and includes `@media print` rules for the 1-page flyer PDF

## Conventions

- Use `uv run build.py` (not `python build.py`) — dependencies are declared inline via PEP 723
- All site files live at the repo root (no `docs/` subdirectory) for GitHub Pages compatibility
- The `2023` branch preserves the old site; `main` is the active branch
- After editing `syllabus.md` or `resources.md`, always run the build script to regenerate HTML
- `flyer.pdf` must fit on exactly 1 letter-size page — if content grows, adjust print CSS in `style.css`
