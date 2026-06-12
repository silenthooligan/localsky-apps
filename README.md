# LocalSky Home Assistant Apps

App repository for [LocalSky](https://github.com/silenthooligan/localsky),
the local-first weather hub and smart irrigation engine.

[![Add repository to my Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fsilenthooligan%2Flocalsky-apps)

Or add it manually: in Home Assistant go to **Settings > Apps > App store**,
open the overflow menu, choose **Repositories**, and paste:

```
https://github.com/silenthooligan/localsky-apps
```

## Apps

### [LocalSky](localsky/)

Runs the LocalSky server on your Home Assistant machine: native Tempest,
Ecowitt, and OpenSprinkler support, a first-run setup wizard, and a full web
UI on port 8090. Pair it with the LocalSky integration (available through
HACS) to get weather, soil, and irrigation entities in Home Assistant; the
integration discovers the app automatically.

Supported architectures: `amd64`, `aarch64`.

## Links

- Main project: https://github.com/silenthooligan/localsky
- Live demo: https://demo.localsky.io
