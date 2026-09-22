<p align="center"><img src="localsky/icon.png" alt="" width="88" height="88"></p>
<h1 align="center">LocalSky for Home Assistant OS</h1>
<p align="center"><strong>Run LocalSky alongside Home Assistant.</strong></p>
<p align="center"><a href="https://localsky.io/docs/home-assistant-app">Installation guide</a> · <a href="https://demo.localsky.io">Try LocalSky</a> · <a href="https://github.com/silenthooligan/localsky">Main project</a></p>

This app installs the LocalSky server on your Home Assistant OS machine. It includes the weather dashboard, irrigation engine, history, and setup wizard, with access from the Home Assistant sidebar.

LocalSky uses your weather, soil, and watering history to plan each zone's next run. You can also use it for weather alone.

## Install

[![Add the LocalSky app repository](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fsilenthooligan%2Flocalsky-apps)

1. Add this repository to **Settings → Apps → App store → Repositories**:
   `https://github.com/silenthooligan/localsky-apps`
2. Install **LocalSky**, then start it.
3. Select **Open web UI** and follow setup.

Supported architectures: **amd64** and **aarch64**. The app needs port **8090** available on the host.

Running Home Assistant Container? Install the [LocalSky Docker container](https://localsky.io/docs/getting-started) on a reachable host instead. Existing Supervised installations with an app store can also use this package.

## App or integration?

| Package | Its job |
|---|---|
| **This app** | Runs the LocalSky server and web interface |
| **[HACS integration](https://github.com/silenthooligan/localsky-ha)** | Adds LocalSky weather, sensors, valves, and actions to Home Assistant |

Install the companion integration if you want LocalSky entities in dashboards and automations. It connects to this app or to a LocalSky server running elsewhere.

## Weather and devices

Connect supported stations and controllers directly, or use HA weather sensors through passthrough. The default `home_assistant` app option enables the Supervisor connection without a separate HA token.

For Tempest, choose which application receives the local UDP feed. If HA's WeatherFlow integration already receives it, LocalSky can use the HA readings.

[App configuration and networking →](localsky/DOCS.md)

## Data and updates

The app keeps configuration and history in its persistent data directory. Home Assistant backups include that data; LocalSky also offers its own backup download.

Update through the app store after reviewing the release notes. LocalSky is in beta, so verify zone bindings and run limits before enabling automatic watering.

[App guide](localsky/DOCS.md) · [LocalSky documentation](https://localsky.io/docs/) · [Report a packaging issue](https://github.com/silenthooligan/localsky-apps/issues)
