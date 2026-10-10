"""Package only a published base, exposing updates after both native checks."""
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import urllib.parse
import urllib.request


def run(*args):
    return subprocess.check_output(args, text=True).strip()


def version(value):
    if not re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+', value):
        raise ValueError('A stable numeric version is required')
    return tuple(map(int, value.split('.')))


def validate(candidate):
    current = re.search(r'^version: "([^"]+)"', Path('localsky/config.yaml').read_text(), re.M)[1]
    assert version(candidate) > version(current), 'Refusing to rebuild an already offered or older version'
    release = json.loads(run('gh', 'api', f'repos/silenthooligan/localsky/releases/tags/v{candidate}'))
    assert not release['draft'] and not release['prerelease']
    revision = json.loads(run('gh', 'api', f'repos/silenthooligan/localsky/commits/v{candidate}'))['sha']
    scope = urllib.parse.quote('repository:silenthooligan/localsky:pull', safe='')
    with urllib.request.urlopen('https://ghcr.io/token?service=ghcr.io&scope=' + scope, timeout=30) as response:
        token = json.load(response)['token']
    request = urllib.request.Request(f'https://ghcr.io/v2/silenthooligan/localsky/manifests/{candidate}', headers={
        'Authorization': 'Bearer ' + token, 'Accept': 'application/vnd.oci.image.index.v1+json, application/vnd.docker.distribution.manifest.list.v2+json'})
    with urllib.request.urlopen(request, timeout=30) as response:
        digest = response.headers['Docker-Content-Digest']
        manifest = json.load(response)
    assert {'amd64', 'arm64'} <= {m['platform']['architecture'] for m in manifest['manifests'] if m['platform']['os'] == 'linux'}
    assert re.fullmatch(r'sha256:[0-9a-f]{64}', digest)
    assert re.fullmatch(r'[0-9a-f]{40}', revision)
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
        output.write(f'revision={revision}\nimage=ghcr.io/silenthooligan/localsky@{digest}\n')


def publish(candidate):
    run('git', 'fetch', 'origin', 'main')
    assert run('git', 'rev-parse', 'HEAD') == run('git', 'rev-parse', 'origin/main'), 'Concurrent main update; rebase before publication'
    image = 'ghcr.io/silenthooligan/localsky-haos'
    digests = []
    for arch in ('amd64', 'arm64'):
        proof = json.loads(Path('digests', arch + '.json').read_text())
        assert proof['architecture'] == arch and re.fullmatch(r'sha256:[0-9a-f]{64}', proof['digest'])
        digests.append(image + '@' + proof['digest'])
    run('docker', 'buildx', 'imagetools', 'create', '-t', image + ':' + candidate, '-t', image + ':latest', *digests)
    config = Path('localsky/config.yaml')
    config.write_text(re.sub(r'^version: "[^"]+"', f'version: "{candidate}"', config.read_text(), count=1, flags=re.M))
    dockerfile = Path('localsky/Dockerfile')
    dockerfile.write_text(re.sub(r'^ARG BASE_VERSION=.*', f'ARG BASE_VERSION={candidate}', dockerfile.read_text(), count=1, flags=re.M))
    changelog = Path('localsky/CHANGELOG.md')
    title, body = changelog.read_text().split('\n', 1)
    note = os.environ.get('CHANGELOG') or f'Packages LocalSky {candidate}.'
    changelog.write_text(f'{title}\n\n## {candidate}\n\n{note}\n{body}')
    run('git', 'config', 'user.name', 'silenthooligan')
    run('git', 'config', 'user.email', 'erik@skean.net')
    run('git', 'add', 'localsky/config.yaml', 'localsky/Dockerfile', 'localsky/CHANGELOG.md')
    run('git', 'commit', '-m', f'feat: LocalSky {candidate}')
    run('git', 'push', 'origin', 'HEAD:main')


if __name__ == '__main__':
    candidate = os.environ['VERSION']
    version(candidate)
    {'validate': validate, 'publish': publish}[sys.argv[1]](candidate)
