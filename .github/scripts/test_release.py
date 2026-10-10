"""Release failures must leave registry tags and the app-store manifest alone."""
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('release', Path(__file__).with_name('release.py'))
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class PublicationGuards(unittest.TestCase):
    def setUp(self):
        self.previous = Path.cwd()
        self.temp = tempfile.TemporaryDirectory()
        os.chdir(self.temp.name)
        Path('localsky').mkdir()
        Path('localsky/config.yaml').write_text('version: "1.0.1"\n')

    def tearDown(self):
        os.chdir(self.previous)
        self.temp.cleanup()

    def test_invalid_versions_never_reach_external_tools(self):
        for value in ('v1.0.2', '1.0.2;exit', '1.0.2\n', '../1.0.2', '1.0.2-beta'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                release.version(value)

    def test_older_and_current_versions_stop_before_network(self):
        with patch.object(release, 'run') as command, patch.object(release.urllib.request, 'urlopen') as request:
            for value in ('1.0.0', '1.0.1'):
                with self.assertRaises(AssertionError):
                    release.validate(value)
            command.assert_not_called()
            request.assert_not_called()

    def test_concurrent_main_update_stops_before_promotion(self):
        with patch.object(release, 'run', side_effect=['', 'old', 'new']) as command:
            with self.assertRaises(AssertionError):
                release.publish('1.0.2')
            self.assertFalse(any(call.args[0] == 'docker' for call in command.call_args_list))

    def test_missing_or_mismatched_second_architecture_cannot_publish(self):
        Path('digests').mkdir()
        Path('digests/amd64.json').write_text(json.dumps({'architecture': 'amd64', 'digest': 'sha256:' + 'a' * 64}))
        for mismatch in (False, True):
            if mismatch:
                Path('digests/arm64.json').write_text(json.dumps({'architecture': 'amd64', 'digest': 'sha256:' + 'b' * 64}))
            with patch.object(release, 'run', side_effect=['', 'same', 'same']) as command:
                with self.assertRaises((FileNotFoundError, AssertionError)):
                    release.publish('1.0.2')
                self.assertFalse(any(call.args[0] == 'docker' for call in command.call_args_list))
            self.assertEqual(Path('localsky/config.yaml').read_text(), 'version: "1.0.1"\n')


if __name__ == '__main__':
    unittest.main()
