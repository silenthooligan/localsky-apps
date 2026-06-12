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
UI on port 8090.

Supported architectures: `amd64`, `aarch64`.

## Pair it with the LocalSky integration

The app is the server. The
[LocalSky integration](https://github.com/silenthooligan/localsky-hacs)
(via HACS) is what turns it into Home Assistant entities: weather, soil,
zone valves, verdicts, and services for automations. It discovers the
running app automatically over mDNS, so the pairing is install-and-done:

[![Open your Home Assistant instance and add this repository to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=silenthooligan&repository=localsky-hacs&category=integration)

## Links

- Main project: https://github.com/silenthooligan/localsky
- Documentation: https://localsky.io/docs/home-assistant-app
- LocalSky integration (HACS): https://github.com/silenthooligan/localsky-hacs
- Live demo: https://demo.localsky.io
