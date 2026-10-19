"""Sphinx configuration for the RSWall Scripting Reference Manual."""

from __future__ import annotations

import sys
from pathlib import Path

# Package lives in ../src
_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT / "src"))

from rswall import __version__ as _package_version  # noqa: E402

project = "RSWall Scripting Reference Manual"
copyright = "2026, Rocscience Inc."
author = "Rocscience Inc."
version = _package_version
release = _package_version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "pr-review",
    "PUBLISHING.md",
]

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_extra_path = ["example_models"]
html_title = "RSWall Scripting Reference Manual"
html_theme_options = {
    "show_prev_next": True,
    "navigation_with_keys": True,
    "collapse_navigation": False,
    "navigation_depth": 4,
    "show_nav_level": 2,
    "show_toc_level": 2,
    "header_links_before_dropdown": 4,
    # Right-hand "On this page" only — no Show Source / [source] links.
    "secondary_sidebar_items": ["page-toc"],
}

# Left sidebar: section/sibling links only — no duplicate page TOC.
html_sidebars = {
    "**": ["sidebar-nav-bs"],
}

# Never expose RST or Python source in the published manual.
html_show_sourcelink = False
html_copy_source = False

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "private-members": False,
    "special-members": "__enter__,__exit__",
    "show-inheritance": True,
    "member-order": "bysource",
}
autodoc_typehints = "description"
autodoc_class_signature = "separated"
autoclass_content = "class"

# Module names match class names (e.g. rswall.Wall). Always document
# ``rswall.Wall.Wall``, never treat ``from rswall import Wall`` as the class.
autodoc_mock_imports = []

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_use_param = True
napoleon_use_rtype = True

autosummary_generate = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# Suppress noisy warnings for missing cross-refs to typing aliases.
nitpicky = False


def setup(app):
    """Skip private and generated members that autodoc might otherwise pick up."""

    def _skip_member(app, what, name, obj, skip, options):
        if name.startswith("_") and name not in ("__enter__", "__exit__"):
            return True
        return skip

    app.connect("autodoc-skip-member", _skip_member)
