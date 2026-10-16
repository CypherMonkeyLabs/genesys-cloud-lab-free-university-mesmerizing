# Publishing

## Built

The lab is a static site under `campus/`. `campus/manifest.webmanifest` and `campus/sw.js` make it an installable PWA when it is served over HTTPS, or on localhost. Icons are `icon-192.png` and `icon-512.png`. There is no account and no analytics beacon.

`npm run serve` runs `scripts/gzip-static.mjs` and serves this repository. Open `/campus/`.

## Prepared, not built

These are notes for a later package. They are not in this repository as installable projects.

- Chrome extension: a thin wrapper could point `manifest.json` at `campus/index.html` and list the same icons. No extension manifest is included.
- Capacitor iOS and Android: the web dir would be `campus/`. No `capacitor.config` and no native projects are generated here.
- Embed widget: a host page can iframe `campus/index.html`. No separate widget script is shipped.

Confirm before relying on store-review rules. This lab does not submit to a store.
