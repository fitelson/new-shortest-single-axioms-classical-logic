"""Small non-search regressions for the candidate-evidence archive."""
import importlib.util
import json
from pathlib import Path
import sys
import unittest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'tools'))
import candidate_index as ci
import archive_cn19_padding as padding
import verify_candidate_reductions as reductions


class CandidateArchiveTests(unittest.TestCase):
    def test_fresh_padding_and_renumbering(self):
        self.assertTrue(padding.fresh_padding('C0CCN1CCN23C24CC41C21'))
        self.assertFalse(padding.fresh_padding('C0CCN0CCN23C24CC41C21'))
        self.assertEqual(padding.renumber('CCN1CCN23C24CC41C21'), 'CCN0CCN12C13CC30C10')

    def test_finite_reduction_checks(self):
        result = reductions.verify()
        self.assertEqual(result['proper_tautological_generalizations'], 0)
        self.assertEqual(result['O5_prime_designated_valuations'], 2401)

    def test_c1915_not_counted_as_tautology(self):
        rows = json.loads((ci.ROOT / 'named_candidates.json').read_text())
        row = next(r for r in rows if r['id'] == 'CD_CN19_c1915')
        self.assertIn('truth table', row['method'])
        self.assertIn('not a tautology', row['note'])

    def test_exception_map_is_closed(self):
        rows = json.loads((ci.ROOT / 'cn19_padding_exceptions.json').read_text())
        self.assertEqual(len(rows), 77)
        self.assertEqual(sum('output_sha256' in r for r in rows), 59)
        self.assertEqual(sum('named_candidate' in r for r in rows), 18)
        for r in rows:
            self.assertTrue((REPO / r['evidence']).is_file())

    def test_unquoted_legacy_model(self):
        import re
        rows = json.loads((ci.ROOT / 'cn19_padding_exceptions.json').read_text())
        row = next(r for r in rows if r['method'] == 'finite model')
        text = (REPO / row['evidence']).read_text()
        quoted = re.sub(r"'?(fmb_\$i_\d+)'?", r"'\1'", text)
        self.assertEqual(ci.model_from_text(text), ci.model_from_text(quoted))


if __name__ == '__main__':
    unittest.main()
