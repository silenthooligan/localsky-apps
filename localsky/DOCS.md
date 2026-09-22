# Run LocalSky on Home Assistant OS

This app runs the LocalSky server: weather collection, irrigation planning, history, and the web interface. The optional [HACS integration](https://github.com/silenthooligan/localsky-ha) adds the server's entities and actions to Home Assistant.

## First setup

1. Start the app and select **Open web UI**.
2. Set your location and timezone.
3. Add weather sources. If HA already receives your station, choose HA passthrough.
4. Add a supported controller if you want irrigation. Check its connection and zone bindings.
5. Set each zone's plants, soil, application rate, and run limit.
6. Finish setup and review the Irrigation page before enabling unattended watering.

All of these settings remain editable in LocalSky. [Full setup guide](https://localsky.io/docs/getting-started).

## App options

| Option | Default | What it changes |
|---|---|---|
| `home_assistant` | `true` | Enables the Supervisor API connection for HA device import and passthrough. No separate HA URL or access token is needed for this connection. |
| `log_level` | `info` | Sets LocalSky log detail. Use `debug` when collecting evidence for a problem. |

These options configure the app wrapper. Configure weather sources, irrigation, accounts, and notifications inside LocalSky.

## Network access

The app uses the host network for local device access, Tempest UDP broadcasts, and mDNS discovery. Its direct web address is **http://YOUR_HA_HOST:8090**. The Home Assistant sidebar uses ingress.

Port 8090 must be free. Devices on other subnets must be reachable through your network rules; multicast and UDP broadcasts do not automatically cross VLANs.

If HA's WeatherFlow integration already listens on UDP 50222, disable or remove LocalSky's Tempest UDP source and use HA passthrough. Choose **Rain last minute (accumulate today)** for WeatherFlow's preceding-minute precipitation reading. Keep a forecast provider enabled.

## Backups and updates

The persistent `/data` directory contains LocalSky's configuration, identity, and history. Home Assistant includes it in app backups and stops the app briefly for a consistent backup. LocalSky also offers a downloadable backup under Settings.

Before an update, take a backup and read the release notes. Update the app and companion integration to matching releases. Afterward, check the version, source health, and zone status in LocalSky.

[Backup and restore guide](https://localsky.io/docs/backup-restore).

## Notifications

The app creates Web Push keys on first boot. Browser push also requires an HTTPS origin, browser support, and subscription permission. Direct HTTP access on a LAN does not meet the HTTPS requirement. Configure delivery in LocalSky's Notifications settings.

## When something goes wrong

| Symptom | First check |
|---|---|
| App does not start | Open the app log and check for a port conflict or data-directory error. |
| No station readings | Check LocalSky's Devices status and whether broadcasts reach the host. |
| HA entities are missing | Install and pair the HACS integration; the app alone does not create them. |
| HA passthrough reports HTTP 500 | Read the LocalSky technical details and HA log at the same timestamp. In 0.9.2, mapped entity reads can recover a failed bulk request. |
| Irrigation is held | Open Watering decisions for the zone's reason and missing inputs. |

The watchdog checks `/api/v1/info` and can restart an unresponsive app. That checks server reachability; use LocalSky's health and decision views to assess sources and watering.

[LocalSky troubleshooting](https://localsky.io/docs/troubleshooting) · [Packaging issues](https://github.com/silenthooligan/localsky-apps/issues) · [Server issues](https://github.com/silenthooligan/localsky/issues)
