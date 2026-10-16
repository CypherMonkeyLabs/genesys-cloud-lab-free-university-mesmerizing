# Kit notes for this lab

The chrome, footer, and guide started from the Webex lab kit on `main` (`assets/css/frame.css`, `wow.css`, `footer.css`, `scripts/gzip-static.mjs`). Those CSS files are copied here and then overridden by `campus/assets/round2.css` and `campus/guide/guide.css`.

`campus/assets/js/frame.js` and `campus/assets/js/university.js` are thin on purpose. The Webex copies inject a sister-lab strip and social icons. This lab does not load those. The Genesys page already has its drawer, banner, and footer.

Reusable pieces for another lab:

- Boxed disclaimer: `.disclaimer-panel` in `footer.css`, with the contrast overrides in `round2.css`.
- Three brand icons only: website, `https://github.com/CypherMonkeyLabs`, `https://linktr.ee/cypherMonkey`.
- First-open tour and the monkey guide: `campus/guide/guide.js` plus `guide.css`. The monkey is a layered SVG (ears, face, eyes, glasses). The phone panel is a bottom sheet at most 60vh, above the bottom bar.
- Download buttons: `downloadBar()` in `campus/assets/app.js` and `campus/assets/round2.js`.
- Gzip check server: `scripts/gzip-static.mjs` (port 8741).

Do not copy Webex `verify-university.mjs` brand rules. That file still requires other social hosts. This lab's check is `scripts/verify.mjs`.
