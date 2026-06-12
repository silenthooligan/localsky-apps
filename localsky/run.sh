#!/bin/sh
# HAOS app entrypoint: translate Supervisor-land into LocalSky's environment.
# Runs as root (see Dockerfile), execs the server as uid 10001.
set -eu

OPTIONS=/data/options.json

opt() { jq -r "$1 // empty" "$OPTIONS" 2>/dev/null || true; }

# Booleans need their own reader: jq's // operator falls through on false
# as well as null, so `.key // empty` would erase an explicit false.
opt_bool() { jq -r "if $1 == false then \"false\" else \"true\" end" "$OPTIONS" 2>/dev/null || echo "true"; }

# Log level option -> RUST_LOG. debug/trace raise only the localsky
# namespaces so tower/hyper transport chatter stays at info.
case "$(opt '.log_level')" in
  error) RUST_LOG="error" ;;
  warn)  RUST_LOG="warn" ;;
  debug) RUST_LOG="info,localsky=debug,tower_http=info,axum=info" ;;
  trace) RUST_LOG="info,localsky=trace,tower_http=info,axum=info" ;;
  *)     RUST_LOG="info" ;;
esac
export RUST_LOG

export LEPTOS_SITE_ADDR="0.0.0.0:8090"
export HISTORY_DB_PATH="/data/irrigation.db"
export CONFIG_PATH="/data/localsky.toml"

# Home Assistant connection through the Supervisor proxy: REST under
# {HA_URL}/api/* and WebSocket at /core/api/websocket, both authenticated
# by SUPERVISOR_TOKEN. No long-lived token setup for the user.
if [ "$(opt_bool '.home_assistant')" = "true" ] && [ -n "${SUPERVISOR_TOKEN:-}" ]; then
  export HA_URL="http://supervisor/core"
  export HA_TOKEN="$SUPERVISOR_TOKEN"
fi

# Web Push: per-install VAPID P-256 keypair, generated once on first boot.
# Browsers only register the service worker over HTTPS, so push stays
# dormant until the instance is fronted by TLS; the keys cost nothing.
KEYS="/data/keys"
PRIV="$KEYS/vapid-private.pem"
mkdir -p "$KEYS"
[ -f "$PRIV" ] || openssl ecparam -name prime256v1 -genkey -noout -out "$PRIV"
VAPID_PUBLIC_KEY="$(openssl ec -in "$PRIV" -pubout -outform DER 2>/dev/null \
  | tail -c 65 | base64 | tr -d '\n=' | tr '+/' '-_')"
export VAPID_PUBLIC_KEY
export VAPID_PRIVATE_KEY_PATH="$PRIV"

# The Supervisor creates /data root-owned; the server runs as uid 10001.
chown -R 10001:10001 /data

exec setpriv --reuid 10001 --regid 10001 --clear-groups /app/localsky
