# Al Maher Cleaning Services

Arabic-first, bilingual client presentation on `feature/expanded-scope`. The existing design and stack are retained; this branch extends the website and administration layouts.

```sh
npm run build
npm run serve
npm test
node tests/expanded.cjs
```

Open `index.html`, `services.html`, `corporate.html`, or `admin.html`. Campaign pages live under `campaigns/<slug>/`.

This is design-only: no backend or live tracking is connected. Forms prepare WhatsApp messages. Administration changes remain in memory for the browser session. See [design scope](docs/DESIGN_SCOPE.md) for implemented presentation interactions and deferred production work. Older production/proposal documents are historical and are not the scope of this branch.
