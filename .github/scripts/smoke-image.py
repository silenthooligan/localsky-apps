"""Native wrapper checks with synthetic data, no network and no host mounts."""
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import time


def run(*args, **kwargs):
    return subprocess.check_output(args, **kwargs)


def get(cid, route):
    return run('docker', 'exec', cid, 'curl', '-fsS', '--max-time', '5',
               'http://127.0.0.1:8090' + route, stderr=subprocess.DEVNULL)


def ready(cid):
    for _ in range(45):
        try:
            info = json.loads(get(cid, '/api/v1/info'))
            health = json.loads(get(cid, '/api/v1/health?strict=1'))
            if health['status'] == 'ok':
                return info, health
        except (subprocess.CalledProcessError, ValueError):
            pass
        time.sleep(2)
    raise RuntimeError('Image did not become healthy within 90 seconds')


def main():
    arch = os.environ['ARCH']
    assert platform.machine() == {'amd64': 'x86_64', 'arm64': 'aarch64'}[arch]
    containers = []

    def start(image, wrapper=False):
        args = ['docker', 'run', '-d', '--network', 'none', '--tmpfs', '/data',
                '--tmpfs', '/keys', '-e', 'LOCALSKY_DEMO=1', '-e', 'LOCALSKY_SMART_DRY_RUN=1']
        if wrapper:
            args += ['--entrypoint', '/bin/sh', image, '-c',
                     'while [ ! -f /data/ready ]; do sleep 1; done; exec /run.sh']
        else:
            args += [image]
        cid = run(*args, text=True).strip()
        assert re.fullmatch(r'[a-f0-9]{64}', cid)
        containers.append(cid)
        return cid

    try:
        base = start(os.environ['BASE_IMAGE'])
        ready(base)
        fixture = run('docker', 'exec', base, 'cat', '/data/localsky.toml')
        cid = start(os.environ['SMOKE_IMAGE'], wrapper=True)
        run('docker', 'exec', '-i', cid, 'sh', '-c',
            'cat > /data/localsky.toml && printf \'{"home_assistant":false}\' > /data/options.json && touch /data/ready', input=fixture)
        info, health = ready(cid)
        assert info['service_version'] == os.environ['VERSION']
        assert info['build_revision'] == os.environ['REVISION']
        assert info['demo'] and info['dry_run'] and not health['valves_unclosed']
        assert all(not z['running'] for z in json.loads(get(cid, '/api/v1/irrigation/snapshot'))['zones'])
        routes = ['/', '/irrigation', '/zones', '/history', '/setup', '/docs/']
        pages = {route: get(cid, route).decode() for route in routes}
        assert all('<html' in body.lower() for body in pages.values())
        assets = set(re.findall(r'[/]pkg/[^"\s<>]+\.(?:js|wasm|css)', pages['/']))
        assert len(assets) >= 3 and all(len(get(cid, asset)) > 100 for asset in assets)
        status = run('docker', 'exec', cid, 'cat', '/proc/1/status', text=True)
        assert re.search(r'^Uid:\s+(\d+)', status, re.M)[1] == '10001'
        run('docker', 'exec', cid, 'test', '-s', '/data/keys/vapid-private.pem')
        inspected = json.loads(run('docker', 'inspect', cid))[0]
        assert inspected['HostConfig']['NetworkMode'] == 'none'
        assert not inspected['HostConfig']['Binds'] and not inspected['HostConfig']['PortBindings']
        run('docker', 'stop', '--time', '15', cid)
        stopped = json.loads(run('docker', 'inspect', cid))[0]['State']
        assert stopped['ExitCode'] == 0 and not stopped['OOMKilled']
        proof = {'result': 'pass', 'architecture': arch, 'native': True,
                 'version': info['service_version'], 'revision': info['build_revision'],
                 'image': os.environ['SMOKE_IMAGE'], 'health': health['status'],
                 'routes': routes, 'assets': sorted(assets), 'uid': 10001,
                 'generated_push_key': True, 'network': 'none', 'host_mounts': False,
                 'shutdown_exit': stopped['ExitCode'], 'actual_supervisor_install': False}
        Path('runtime-proof.json').write_text(json.dumps(proof, indent=2))
        print(json.dumps(proof))
    except Exception:
        for cid in containers:
            subprocess.run(['docker', 'logs', '--tail', '50', cid], check=False)
        raise
    finally:
        for cid in containers:
            subprocess.run(['docker', 'rm', '-f', cid], check=True)


if __name__ == '__main__':
    main()
