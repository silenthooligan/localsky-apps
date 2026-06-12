# LocalSky app

Packages the released [LocalSky](https://github.com/silenthooligan/localsky)
container image as a Home Assistant app: local-first weather hub and smart
irrigation engine for Tempest, Ecowitt, and OpenSprinkler hardware.

See [DOCS.md](DOCS.md) for installation and usage. Installs pull the
prebuilt `ghcr.io/silenthooligan/localsky-haos` image, built from the
[Dockerfile](Dockerfile) by the publish-image workflow. On each LocalSky
release the workflow is run with the new version, then `version` in
[config.yaml](config.yaml) is bumped to match.
