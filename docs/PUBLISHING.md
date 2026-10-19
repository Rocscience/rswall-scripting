# Publishing the RSWall Scripting Reference Manual

The desktop **Scripting → Reference Manual** command opens:

https://rocscience.github.io/rswall-scripting/

That path is fixed in `RSWall` (`SCRIPTING_REFERENCE_MANUAL_LOCATION`). Do **not**
change the C# URL unless the published site intentionally moves.

## Build locally

From the `RSWallScripting` repo root:

```bash
pip install -e ".[docs]"
python -m sphinx -W -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` in a browser.

## What fixes the 404

Sphinx HTML in this repository is necessary but not sufficient. GitHub Pages
must serve that HTML at `rocscience.github.io/rswall-scripting/`.

Typical org setup (pick one):

1. **Dedicated docs repo** named `rswall-scripting` under the `rocscience`
   GitHub organization, with Pages enabled (GitHub Actions or `gh-pages`
   branch) publishing the Sphinx `html` output from this tree.
2. **Mirror / sync** this `docs/` tree (or the built `_build/html`) into that
   Pages repository on release.
3. If `RSWallScripting` itself is published on GitHub under a different name,
   Pages project sites use the **repository name** in the URL. The in-app link
   expects the repo (or Pages project) to be named `rswall-scripting`.

Until Pages is enabled and the first successful deploy finishes, the in-app
link will continue to return 404.

## CI

See [`.github/workflows/docs.yml`](../.github/workflows/docs.yml). The build
job always runs `sphinx-build -W`. The deploy job is commented until org Pages
permissions are ready — uncomment `deploy` after enabling Pages with source
**GitHub Actions**.
