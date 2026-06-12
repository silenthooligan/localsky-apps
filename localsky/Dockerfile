# Thin wrapper over the released multi-arch LocalSky image, published as a
# prebuilt app image by .github/workflows/publish-image.yml so installs are
# a pull, not a local build.
#
# Why a wrapper instead of the upstream image directly: the upstream image
# runs as uid 10001, but the Supervisor creates the app's /data volume
# root-owned. This layer starts as root, fixes /data ownership, wires
# Supervisor-provided config (HA proxy token, options.json) into LocalSky's
# environment, then drops back to uid 10001 before exec'ing the server.
ARG BASE_VERSION=0.3.0-beta.1
FROM ghcr.io/silenthooligan/localsky:${BASE_VERSION}

USER 0

# jq parses /data/options.json; openssl generates the per-install VAPID
# keypair for Web Push. setpriv (util-linux) is already in the base.
RUN apt-get update && apt-get install -y --no-install-recommends jq openssl \
    && rm -rf /var/lib/apt/lists/*

COPY run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
