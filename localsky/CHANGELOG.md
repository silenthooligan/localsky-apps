# Changelog

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
