# LocalSky Home Assistant Apps

App repository for [LocalSky](https://github.com/silenthooligan/localsky),
the local-first weather hub and smart irrigation engine.

> ### This repository is for Home Assistant OS only
>
> Apps (formerly add-ons) are a feature of the Supervisor, which exists
> **only** on the **Home Assistant OS** and **Supervised** installation
> types. If your Home Assistant runs as a **Container** or **Core**
> install, there is no app store and nothing here applies to you: run the
> LocalSky server with [Docker](https://localsky.io/docs/getting-started)
> instead, it is the exact same software.
>
> Not sure which you have? In Home Assistant open **Settings > About** and
> read the **Installation method** line.

## What is what

| Piece | What it is | Works on |
|---|---|---|
| **This app** | Runs the LocalSky *server* on your Home Assistant machine | Home Assistant OS / Supervised only |
| [LocalSky integration](https://github.com/silenthooligan/localsky-ha) (HACS) | Turns a running LocalSky server into HA entities | Every HA installation type |
| [LocalSky via Docker](https://localsky.io/docs/getting-started) | The same server, run anywhere Docker runs | Any machine, HA optional |

You always need exactly one server (this app **or** Docker, never both)
plus, optionally, the integration for entities. Docker is the preferred
and most widely tested way to run the server; this app packages the exact
same image as a convenience for Home Assistant OS.

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
[LocalSky integration](https://github.com/silenthooligan/localsky-ha)
(via HACS) is what turns it into Home Assistant entities: weather, soil,
zone valves, verdicts, and services for automations. It discovers the
running app automatically over mDNS, so the pairing is install-and-done:

[![Open your Home Assistant instance and add this repository to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=silenthooligan&repository=localsky-ha&category=integration)

## Links

- Main project: https://github.com/silenthooligan/localsky
- Documentation: https://localsky.io/docs/home-assistant-app
- LocalSky integration (HACS): https://github.com/silenthooligan/localsky-ha
- Live demo: https://demo.localsky.io
