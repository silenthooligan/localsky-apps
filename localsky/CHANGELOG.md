# Changelog

## 0.9.0

Packages LocalSky 0.9.0: shared weather decisions, HA WeatherFlow input, rain-aware planning, daily history and restart recovery.

## 0.8.1

Tracks LocalSky 0.8.1. The zone editor opens where you clicked it, adding a zone opens a dialog instead of a form below the fold, and the watering-targets notice no longer implies something is unfinished.

## 0.8.0

Tracks LocalSky 0.8.0. Every zone shows its real soil deficit, and a new soil scheduling model waters each zone by its own soil instead of a weekly quota. A sandy yard no longer skips a whole week of watering after one storm.

## 0.7.22

Zones now say why they are not watering, the soil deficit no longer shows a number nothing measured, and Home Assistant helpers are migrated into LocalSky's own settings.

## 0.7.21

Zones now bind to a controller zone you pick from a list, so the names in LocalSky and in your controller app no longer have to match. Existing bindings are carried over automatically. A scan can bind several zones at once, the bound zone is shown on the zone, and a zone nothing can water now says so instead of failing silently.

## 0.7.20

Zones on a cloud controller start again: a station number typed into a zone could overwrite the zone id the controller scan found, so the app asked the vendor to run a zone that does not exist. A start that fails now names the reason, and when a zone is not matched to a controller zone it shows the controller's zone list and the two ways to fix it.

## 0.7.19

Settings and navigation clarity: the restart notice stays on screen while you work, scan results open and scroll into view, unsaved changes are flagged on the save button, and the Zones navigation entry shows how many zones have tuning suggestions.

## 0.7.18

Scan zones in the controller editor now fills the zone map, zones imported through the setup wizard work on Rachio, Hydrawise, B-hyve, and Rain Bird, and Rachio gets live running state with API-budget-friendly polling. Stopping a Rachio zone stops all watering on the device (its API has no per-zone stop); the app says so when it happens.

## 0.7.17

Watering sessions are now sized by a real weekly water balance: rain that already fell, watering already done, and a forecast credit corrected against your yard's own history all count toward the weekly target, so sessions shrink or skip when the week is already covered. Installs without a rain gauge fall back to weather-source data with the source named. Tuning suggestions can be snoozed for 30 days or dismissed permanently, which also silences the weekly notification.

## 0.7.16

Set each zone's own maximum run time, with a confirmation step and a notification when raising it past 60 minutes. Tuning suggestions now offer to raise the run limit before splitting sessions, pause while a watering restriction is active, and the tuning surfaces got a clearer look with suggestion badges on zone cards.

## 0.7.15

LocalSky now watches your zones for a week or two and hands you plain-language tuning suggestions with a one-click apply: session splits when a duration cap is shorting a zone, soil texture when a probe disagrees with the model, your real sprinkler rate measured from probe readings, and an honest scorecard of its rain-skip calls.

## 0.7.14

Values LocalSky never measured now read as unknown instead of a fabricated number (water level, ET0 during outages, precipitation probability, and more), unlocated installs no longer show another city's weather, and Home Assistant only gets sensors your install can actually feed.

## 0.7.13

Setup wizard cloud toggles now save to the setup draft and apply when setup finishes; failed settings loads show the server's reason. Full notes: https://github.com/silenthooligan/localsky/releases/tag/v0.7.13

## 0.7.12

A refused settings save now names the failing validation rules instead of a bare config_invalid code, and precipitation probability becomes a sensor. Full notes: https://github.com/silenthooligan/localsky/releases/tag/v0.7.12

## 0.7.11

Packages LocalSky v0.7.11. Hourly forecasts now reach Home Assistant; no add-on changes.

## 0.7.10

Lightning fixes: the one-hour strike counter now decays after a storm (a stuck counter left 'strikes above 0' automations silent), the average strike distance reports unknown instead of 0 when no strikes were detected, and a new last-strike distance sensor persists between strikes. Full notes: https://github.com/silenthooligan/localsky/releases/tag/v0.7.10

## 0.7.9

Interleaving on by default with a wizard water-supply question, cycle-and-soak settings apply without a restart, sign-in via an authenticating reverse proxy, new Engine settings page. Full notes: https://github.com/silenthooligan/localsky/releases/tag/v0.7.9

## 0.7.8

ET0 unit fix (displayed and projected ET read 25x low on the default forecast source), opt-in cycle interleaving across zones, and timezone-correct day boundaries for containerized deployments. Full notes: https://github.com/silenthooligan/localsky/releases/tag/v0.7.8

## 0.7.5

LocalSky 0.7.5: in-app restart for restart-required changes, Ecowitt gateway login in the source editor (enables gateway-side probe removal), source-ranking self-repair, and removed probes no longer linger as offline.

## 0.7.4

LocalSky 0.7.4: in-place soil-probe management, HA ingress write fixes (wizard and settings saves from the sidebar now work), fresh-install Settings fix, and a major sensors/devices query performance win.

## 0.7.3

LocalSky 0.7.3: one-click soil-probe removal (including Ecowitt gateway unregistration), and a fix for in-app navigation 404s when LocalSky is opened from the Home Assistant sidebar (ingress). No breaking changes.

## 0.7.2

Forecast failover chain, condition-aware dashboard, and extended weather data.

## 0.7.0

Per-reading backup chains, unified source list, display units, cloud-first setup, smarter rain-skip safety.

## 0.7.0

Per-reading backup chains, unified source list, display units, cloud-first setup, smarter rain-skip safety.

## 0.5.0-beta.1

First-class DIY/ESP32 controllers (HTTP or MQTT), sticky overrides, wind-gust forecast, PWA reliability fix.

## 0.4.0-beta.3

Fix the addon so it starts on the non-root base image (the initial 0.4.0-beta.3 addon crash-looped at startup).

## 0.4.0-beta.3

Packages LocalSky v0.4.0-beta.3: security fixes and hardening.

## 0.4.0-beta.2

Packages LocalSky v0.4.0-beta.2: flow metering, a first-class Sensors view, point-and-click data-source setup, built-in docs and in-app help, plus setup-wizard fixes (license acceptance and notification choices now persist).

## 0.4.0-beta.1

Packages LocalSky v0.4.0-beta.1.

## 0.3.0-beta.2

LocalSky 0.3.0-beta.2: the UI now embeds in the Home Assistant sidebar (ingress), and fresh installs start with a clean zone list and working push notifications.

## 0.3.0-beta.1

Initial Home Assistant App release, packaging LocalSky v0.3.0-beta.1.

- One-click install from the LocalSky app repository
- Automatic Home Assistant connection through the Supervisor, no long-lived
  token setup needed
- Setup wizard on first boot, web UI on port 8090
- LocalSky data is part of Home Assistant backups
- Web Push keys generated automatically on first boot
