"""Test suite for the First-Year LLC Handbook.

Covers the build pipeline (build, link verification, markdown conversion),
content guarantees (chapters exist, disclaimers present, no secrets), and the
meta-files required of every Asdale Dynamics, LLC repo (LICENSE, README).

Run:  python3 -m pytest tests/ -q
"""

import importlib.util
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
WORKSHEETS = DOCS / "checklists"
BUILD = ROOT / "build.py"
SITE = ROOT / "site"

MANUAL_PAGES = [
    "index.md",
    "bank-accounts.md",
    "records.md",
    "money-dates.md",
    "taxes.md",
    "insurance.md",
    "annual-report.md",
    "professionals.md",
]
CHECKLIST_PAGES = [
    "index.md",
    "first-30-days.md",
    "quarterly-money-date.md",
    "year-end.md",
]

DISCLAIMER = "never legal, tax, or financial advice"
COPYRIGHT_LINE = "Copyright (c) 2026 Asdale Dynamics, LLC"

OFFICIAL_LINK_SETS = [
    {"index", "bank-accounts", "records", "money-dates", "taxes", "annual-report"},
]


def _load_build_module():
    spec = importlib.util.spec_from_file_location("handbook_build", BUILD)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture
def build():
    return _load_build_module()


# ---------------------------------------------------------------------------
# Build pipeline
# ---------------------------------------------------------------------------

def test_build_script_check_mode_passes():
    """python3 build.py --check must exit 0 (build + verify + clean up)."""
    result = subprocess.run(
        [sys.executable, str(BUILD), "--check"],
        capture_output=True, text=True, cwd=ROOT,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Build OK" in result.stdout
    assert "all internal links verified" in result.stdout
    assert "Check mode" in result.stdout
    # Check mode must clean up after itself.
    assert not SITE.exists()


def _clean_site():
    if SITE.exists():
        shutil.rmtree(SITE)


def test_full_build_produces_expected_pages(build):
    assert build.build() == []
    try:
        for stem in MANUAL_PAGES:
            assert (SITE / stem.replace(".md", ".html")).exists()
        for stem in CHECKLIST_PAGES:
            assert (SITE / "checklists" / stem.replace(".md", ".html")).exists()
        html = (SITE / "index.html").read_text(encoding="utf-8")
        assert "The First-Year LLC Handbook" in html
        # Self-contained: inline CSS, nothing that would force a network fetch.
        assert "<style>" in html
        assert "http-equiv" not in html
        for page in SITE.rglob("*.html"):
            src = page.read_text(encoding="utf-8")
            assert '<link rel="stylesheet"' not in src
    finally:
        _clean_site()


def test_every_rendered_page_carries_disclaimer(build):
    assert build.build() == []
    try:
        for page in SITE.rglob("*.html"):
            assert DISCLAIMER in page.read_text(encoding="utf-8"), page
    finally:
        _clean_site()


def test_verify_catches_broken_internal_link(build):
    generated = {"index.html": '<a href="nonexistent.html">oops</a>'}
    assert any("broken link" in p for p in build.verify(generated))


def test_verify_ignores_external_links(build):
    generated = {
        "index.html": '<a href="https://www.irs.gov">IRS</a><a href="mailto:x@y.z">mail</a>'
    }
    assert build.verify(generated) == []


# ---------------------------------------------------------------------------
# Markdown conversion
# ---------------------------------------------------------------------------

def test_headings_get_anchor_ids(build):
    body, anchors = build.convert_blocks("## The Kind Sentence\n\ntext", "")
    assert 'id="the-kind-sentence"' in body
    assert "the-kind-sentence" in anchors


def test_task_list_items_render_checkboxes(build):
    body, _ = build.convert_blocks("- [ ] first todo\n- [x] done thing", "")
    assert '<span class="cbx">[ ]</span>' in body
    assert '<span class="cbx">[x]</span>' in body


def test_tables_render_as_html(build):
    body, _ = build.convert_blocks("| a | b |\n|---|---|\n| 1 | 2 |", "")
    assert "<table>" in body and "<th>a</th>" in body and "<td>2</td>" in body


def test_inline_markdown_and_links(build):
    body, _ = build.convert_blocks(
        "A **bold** *slant* `code` [IRS](https://www.irs.gov)", ""
    )
    for frag in ("<strong>bold</strong>", "<em>slant</em>", "<code>code</code>",
                 'href="https://www.irs.gov"'):
        assert frag in body


def test_relative_link_from_checklists_reaches_manual(build):
    body, _ = build.convert_blocks("[money dates](money-dates.md)", "checklists/")
    assert 'href="../money-dates.html"' in body


def test_html_is_escaped_in_text(build):
    body, _ = build.convert_blocks("Tom <Jerry> & friends", "")
    assert "&lt;Jerry&gt;" in body and "&amp;" in body


# ---------------------------------------------------------------------------
# Content guarantees
# ---------------------------------------------------------------------------

def test_all_chapters_exist_and_are_substantial():
    for stem in MANUAL_PAGES:
        text = (DOCS / stem).read_text(encoding="utf-8")
        assert len(text) > 2500, f"{stem} is unexpectedly short ({len(text)} chars)"
        assert len(re.findall(r"^## ", text, flags=re.M)) >= 3, stem


def test_checklists_contain_checkbox_items():
    for stem in CHECKLIST_PAGES:
        text = (WORKSHEETS / stem).read_text(encoding="utf-8")
        if stem == "index.md":  # the hub page links to the others
            assert re.search(r"^- \[", stem, flags=re.M) or "first-30-days" in text, stem
            continue
        assert re.search(r"^- \[ \] ", text, flags=re.M), stem


def test_factual_chapters_link_official_sources():
    """Pages that state numbers/dates must chain back to an authority."""
    required = {"bank-accounts", "records", "money-dates", "taxes", "annual-report"}
    for stem in required & {p[:-3] for p in MANUAL_PAGES}:
        text = (DOCS / f"{stem}.md").read_text(encoding="utf-8")
        sources = re.findall(r"https?://[^\s)\]]+", text)
        official = [u for u in sources if re.search(
            r"irs\.gov|in\.gov|inbiz\.in\.gov|fincen\.gov", u)]
        assert official, f"{stem} states facts without linking a source"


def test_docs_link_official_sources_abundantly():
    all_text = "".join(p.read_text(encoding="utf-8") for p in DOCS.rglob("*.md"))
    official = re.findall(r"https?://[^\s)\]]+", all_text)
    hits = [u for u in official if re.search(r"irs\.gov|in\.gov|fincen\.gov|inbiz", u)]
    assert len(hits) >= 10, f"only {len(hits)} official links throughout docs"


def test_no_todo_or_placeholder_markers_in_content():
    for md in list(DOCS.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        assert not re.search(r"\b(TODO|FIXME|TBD|PLACEHOLDER)\b", text, flags=re.I), md


def test_sibling_project_references_are_local_relative():
    """Siblings are referenced by name / local relative path, not invented URLs."""
    all_text = "".join(p.read_text(encoding="utf-8") for p in DOCS.rglob("*.md"))
    assert "cashflow-simple-ledger" in all_text
    assert "small-business-ai-playbook" in all_text
    for p in DOCS.rglob("*.md"):
        for ref in re.findall(
            r"\]\(([^)]*small-business-ai-playbook[^)]*)\)", p.read_text(encoding="utf-8")
        ):
            assert ref.startswith("../"), (p, ref)


def test_all_internal_md_links_resolve_to_built_pages(build):
    """Replicate build.resolve_link and require the built pages to exist."""
    assert build.build() == []
    try:
        for md in DOCS.rglob("*.md"):
            page_dir = "checklists/" if md.parent.name == "checklists" else ""
            text = md.read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)#]+)#?[^)]*\)", text):
                if target.startswith(("http://", "https://", "mailto:", "../")):
                    continue
                href = build.resolve_link(target.strip(), page_dir)
                assert (SITE / page_dir / href).exists(), f"{md}: {target} -> {href}"
    finally:
        _clean_site()


# ---------------------------------------------------------------------------
# Meta files required of the repo
# ---------------------------------------------------------------------------

def test_license_has_exact_copyright_line():
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert "MIT License" in license_text
    assert COPYRIGHT_LINE in license_text


def test_readme_credits_the_llc_and_gives_run_instructions():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "Asdale Dynamics, LLC" in readme
    assert "python3 build.py" in readme
    assert "never legal, tax, or financial advice" in readme
    assert COPYRIGHT_LINE in readme


def test_no_secrets_anywhere():
    """Cheap secret-leak tripwire across all tracked file types."""
    patterns = [
        r"AKIA[0-9A-Z]{16}", r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
        r"api[_-]?key\s*[=:]\s*['\"][A-Za-z0-9_\-]{16,}",
        r"secret\s*[=:]\s*['\"][A-Za-z0-9_\-]{16,}",
        r"\b\d{3}-\d{2}-\d{4}\b",  # SSN-shaped (EINs are XX-XXXXXXX)
    ]
    in_scope = [p for p in ROOT.rglob("*") if p.is_file()
                and p.suffix in {".md", ".py", ".html", ".json", ".toml", ".csv"}
                and "site/" not in str(p)]
    assert in_scope, "scan found nothing to guard"
    for path in in_scope:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pat in patterns:
            assert not re.search(pat, text), f"{path} matches {pat}"
