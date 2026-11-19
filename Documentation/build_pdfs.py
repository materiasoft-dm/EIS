"""Convert the exported Notion markdown pages in Documentation/ to PDFs using Edge headless."""
import subprocess
import sys
from pathlib import Path

import markdown

DOCS = Path(__file__).parent
EDGE_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]

CSS = """
@page { size: A4; margin: 18mm 16mm; }
* { box-sizing: border-box; }
body {
  font-family: "Segoe UI", "Calibri", Arial, sans-serif;
  font-size: 10.5pt; line-height: 1.55; color: #1f2430; margin: 0;
}
h1 { font-size: 20pt; color: #0b3d66; border-bottom: 2.5px solid #0b3d66;
     padding-bottom: 6px; margin: 0 0 14px 0; line-height: 1.25; }
h2 { font-size: 14.5pt; color: #0b3d66; border-bottom: 1px solid #c9d6e2;
     padding-bottom: 3px; margin: 22px 0 8px; page-break-after: avoid; }
h3 { font-size: 12pt; color: #14507f; margin: 16px 0 6px; page-break-after: avoid; }
h4 { font-size: 11pt; color: #14507f; margin: 12px 0 4px; page-break-after: avoid; }
p { margin: 6px 0; }
ul, ol { margin: 6px 0 6px 0; padding-left: 22px; }
li { margin: 2.5px 0; }
table { border-collapse: collapse; width: 100%; margin: 10px 0; font-size: 9.5pt; page-break-inside: avoid; }
th { background: #0b3d66; color: #fff; text-align: left; padding: 6px 8px; font-weight: 600; }
td { border: 1px solid #c9d6e2; padding: 5px 8px; vertical-align: top; }
tr:nth-child(even) td { background: #f2f6fa; }
blockquote { margin: 8px 0; padding: 6px 12px; border-left: 4px solid #7aa7cc;
             background: #f2f6fa; color: #3d4a5c; font-size: 9.5pt; }
code { font-family: Consolas, "Courier New", monospace; font-size: 9pt;
       background: #eef2f6; padding: 1px 4px; border-radius: 3px; }
pre { background: #f4f6f8; border: 1px solid #d7dee6; border-radius: 4px;
      padding: 10px; overflow-x: auto; page-break-inside: avoid; }
pre code { background: none; padding: 0; font-size: 8.5pt; line-height: 1.4; }
a { color: #0b5cad; text-decoration: none; word-break: break-word; }
hr { border: none; border-top: 1px solid #c9d6e2; margin: 16px 0; }
strong { color: #10243a; }
input[type="checkbox"] { margin-right: 5px; }
li.task-list-item { list-style: none; margin-left: -18px; }
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
{body}
</body>
</html>"""


def find_browser() -> str:
    for path in EDGE_CANDIDATES:
        if Path(path).exists():
            return path
    raise SystemExit("No Edge/Chrome executable found")


def md_to_html(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists"],
    )


def main() -> None:
    browser = find_browser()
    md_files = sorted(DOCS.glob("*.md"))
    # Skip helper scripts/readmes that are not exported pages
    md_files = [f for f in md_files if f.name != "README.md"]
    if not md_files:
        raise SystemExit("No markdown files found")

    for md in md_files:
        html_path = md.with_suffix(".html")
        pdf_path = md.with_suffix(".pdf")
        text = md.read_text(encoding="utf-8")
        body = md_to_html(text)
        html_path.write_text(
            TEMPLATE.format(title=md.stem, css=CSS, body=body), encoding="utf-8"
        )
        cmd = [
            browser,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if pdf_path.exists() and pdf_path.stat().st_size > 1000:
            print(f"OK   {pdf_path.name} ({pdf_path.stat().st_size // 1024} KB)")
        else:
            print(f"FAIL {md.name}")
            print(result.stdout, result.stderr)
            sys.exit_code = 1
    print("Done.")


if __name__ == "__main__":
    main()
