# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "markdown>=3.5",
#     # "weasyprint>=62",
# ]
# ///
"""Build course website HTML from syllabus.md and resources.md."""

import markdown
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
DOCS = ROOT

SITE_TITLE = "USP 410/510 Urban Data Science"
SITE_SUBTITLE = "Spring 2026"
SITE_FOOTER = "USP 410/510 Urban Data Science &middot; Portland State University &middot; Spring 2026"

PAGES = [
    {
        "src": ROOT / "syllabus.md",
        "dst": DOCS / "syllabus.html",
        "title": "Syllabus",
        "nav_id": "syllabus",
    },
    {
        "src": ROOT / "resources.md",
        "dst": DOCS / "resources.html",
        "title": "Resources",
        "nav_id": "resources",
    },
]

MD_EXTENSIONS = ["tables", "smarty", "attr_list", "fenced_code"]


def build_nav(active_id: str) -> str:
    links = [
        ("index.html", "Home", "home"),
        ("syllabus.html", "Syllabus", "syllabus"),
        ("resources.html", "Resources", "resources"),
    ]
    items = []
    for href, label, nav_id in links:
        cls = ' class="active"' if nav_id == active_id else ""
        items.append(f'      <li><a href="{href}"{cls}>{label}</a></li>')
    return "\n".join(items)


def build_page(page: dict) -> None:
    src = page["src"]
    if not src.exists():
        print(f"  Skipping {src.name} (not found)")
        return

    md_text = src.read_text(encoding="utf-8")

    # Strip the top-level bold title line if it matches the site title
    lines = md_text.split("\n")
    if lines and lines[0].strip().startswith("**") and "Urban Data Science" in lines[0]:
        lines = lines[1:]
        md_text = "\n".join(lines)

    if page["nav_id"] == "syllabus":
        md_text = inject_slide_links(md_text)

    body_html = markdown.markdown(md_text, extensions=MD_EXTENSIONS)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page["title"]} | {SITE_TITLE}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>

<nav>
  <div class="nav-inner">
    <span class="nav-brand">{SITE_TITLE}</span>
    <ul class="nav-links">
{build_nav(page["nav_id"])}
    </ul>
  </div>
</nav>

<main>
  <div class="page-header">
    <h1>{page["title"]}</h1>
    <div class="subtitle">{SITE_TITLE} &middot; {SITE_SUBTITLE}</div>
  </div>

  <div class="content">
{body_html}
  </div>
</main>

<footer>
  <p>{SITE_FOOTER}</p>
</footer>

</body>
</html>
"""
    page["dst"].write_text(html, encoding="utf-8")
    print(f"  {src.name} -> {page['dst'].relative_to(ROOT)}")


def build_slide_pdfs() -> None:
    """Export each *_slides.md to PDF via slidev."""
    slide_files = sorted(ROOT.glob("*_slides.md"))
    if not slide_files:
        print("  No slide files found")
        return
    for src in slide_files:
        dst = src.with_suffix(".pdf")
        result = subprocess.run(
            ["npx", "slidev", "export", str(src), "--output", str(dst)],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(f"  {src.name} -> {dst.name}")
        else:
            print(f"  {src.name} -> FAILED")
            if result.stderr:
                print(f"    {result.stderr.strip()}")


def inject_slide_links(md_text: str) -> str:
    """Add slide PDF links to the schedule table where *_slides.pdf exists."""
    # Map week number -> pdf filename for existing slide PDFs
    slide_pdfs = {}
    for pdf in ROOT.glob("week*_slides.pdf"):
        m = re.match(r"week(\d+)_slides\.pdf", pdf.name)
        if m:
            slide_pdfs[int(m.group(1))] = pdf.name

    if not slide_pdfs:
        return md_text

    def add_link(match):
        week_num = int(match.group(1))
        date = match.group(2)
        topic = match.group(3)
        if week_num in slide_pdfs:
            pdf = slide_pdfs[week_num]
            topic = f"[Slides]({pdf}) &middot; {topic}"
        return f"| W{week_num} | {date} | {topic} |"

    return re.sub(
        r"\| W(\d+) \| (\d{2}/\d{2}) \| (.+?) \|(?= )",
        add_link,
        md_text,
    )


# def build_flyer_pdf() -> None:
#     """Convert index.html landing page to a single-page PDF flyer."""
#     from weasyprint import HTML
#
#     src = DOCS / "index.html"
#     dst = DOCS / "flyer.pdf"
#
#     HTML(filename=str(src), base_url=str(DOCS)).write_pdf(str(dst))
#     print(f"  index.html -> {dst.relative_to(ROOT)}")


def main() -> None:
    print("Building site:")
    for page in PAGES:
        build_page(page)
    print("Building slide PDFs:")
    build_slide_pdfs()
    # print("Building PDF flyer:")
    # build_flyer_pdf()
    print("Done.")


if __name__ == "__main__":
    main()
