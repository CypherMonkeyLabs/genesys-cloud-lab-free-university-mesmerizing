# Third-party notices

This lab vendors a few libraries so the page does not call a CDN. Hashes are in `THIRD_PARTY_MANIFEST.json`. `python3 scripts/licence_manifest.py` checks them.

| Component | Version | Licence |
| --- | --- | --- |
| three.js, including the r186 postprocessing files under `campus/vendor/three-post/` | r186 | MIT. See `campus/vendor/THREE-LICENSE.txt`. |
| d3 | 7.9.0 | ISC |
| anime.js | 4.5.0 | MIT |
| rough.js | 4.6.6 | MIT |
| canvas-confetti | 1.9.3 | ISC |
| markmap-lib and markmap-view, bundled with d3 | 0.18.12 | MIT |

The readable summary of those licences is `campus/vendor/LICENSES.txt`. Mermaid is used only while building SVGs and is not shipped to the browser. No font files are vendored. The chat engine in `campus/shared/pybot-chat/` is lab code (MIT), copied from the Python Lab in this same GitHub organization and adapted for Genesys Cloud CX.
