# LocalSky

LocalSky is a local-first weather hub and smart irrigation engine. It speaks
natively to WeatherFlow Tempest stations (LAN UDP), Ecowitt gateways and soil
sensors, and OpenSprinkler controllers, and makes irrigation decisions from
your own weather data with no cloud dependency.

This app runs the LocalSky server on your Home Assistant machine. It is the
same released container image that runs standalone via Docker. Apps are a
Home Assistant OS / Supervised feature; on a Container or Core install, run
the server with Docker instead (https://localsky.io/docs/getting-started).

## How it fits with Home Assistant

LocalSky on Home Assistant is a two-piece setup:

1. **This app** runs the server: data collection, the irrigation engine, and
   the web UI.
2. **The [LocalSky integration](https://github.com/silenthooligan/localsky-hacs)**
   (available through HACS) turns the running server into Home Assistant
   entities: weather, soil, irrigation status, and more.

The app announces itself over mDNS, so once it is running the integration
discovers it automatically. Add the integration to HACS with one click:

[![Open your Home Assistant instance and add this repository to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=silenthooligan&repository=localsky-hacs&category=integration)

## Installation

1. Add this repository to your app store and install **LocalSky**.
2. Start the app, then click **OPEN WEB UI** (the UI listens on port 8090).
3. The first-run wizard walks you through station setup (Tempest or Ecowitt),
   location, zones, and your irrigation controller.
4. Optional: install the LocalSky integration via HACS to get entities in
   Home Assistant. It will discover this app on its own.

## Options

### `home_assistant` (default: on)

Connects LocalSky to Home Assistant through the Supervisor. No access token
or URL setup is needed. This enables Home Assistant device import and entity
blending inside LocalSky. Turn it off for a fully standalone install.

### `log_level` (default: info)

Server log verbosity. `debug` and `trace` raise only LocalSky's own log
namespaces, so transport-layer chatter stays quiet.

## Networking

The app runs on the host network. That is required so it can:

- hear the Tempest station's LAN broadcast (UDP 50222),
- reach your Ecowitt gateway and OpenSprinkler controller on the LAN,
- announce itself over mDNS for integration discovery.

The web UI binds port 8090 on the host. If another service on your machine
already uses 8090, the app log will show a bind failure on startup.

## Data and backups

Everything LocalSky stores lives in `/data`: the configuration file
(`localsky.toml`) and the irrigation history database (`irrigation.db`).
That directory is included in Home Assistant backups. The app stops briefly
while a backup is taken so the history database is captured consistently.

## Push notifications

A Web Push (VAPID) keypair is generated automatically on first boot.
Browsers only allow notifications over HTTPS, so push stays dormant when you
use the plain `http://` UI. If you front LocalSky with your own TLS reverse
proxy, push notifications work out of the box.

## Troubleshooting

- The app's **Log** tab shows the server log at the configured level.
- The watchdog probes `/api/v1/info` and restarts the app if the server
  stops responding.
- The setup wizard only appears until a configuration exists. After that,
  everything is managed from Settings inside the web UI.

For issues and feature requests, use the main repository:
https://github.com/silenthooligan/localsky
