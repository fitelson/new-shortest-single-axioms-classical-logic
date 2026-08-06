import json
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from audit_lengths import HEADLINE_RUNS, equation_generator_length  # noqa: E402
from compare_survivors import (  # noqa: E402
    canonical_polish_from_functional,
    canonicalize_legacy,
)
from TreeForms import ProcessStatistics, shard_item_count  # noqa: E402


class ReproducibilityToolTests(unittest.TestCase):
    def test_displayed_equational_generator_lengths(self) -> None:
        expected = {"BACF": 17, "BAAN": 20, "BAON": 20, "BACN": 17}
        for name, target in expected.items():
            formula = HEADLINE_RUNS[name][2]
            self.assertIsNotNone(formula)
            self.assertEqual(equation_generator_length(formula), target)

    def test_survivor_normalization_is_alpha_invariant(self) -> None:
        current = canonical_polish_from_functional("t(i(i(Z,Y),n(Z)))")
        legacy = canonicalize_legacy("CC78N7")
        self.assertEqual(current, "CC01N0")
        self.assertEqual(current, legacy)

    def test_numpy_statistics_are_json_serializable(self) -> None:
        statistics = ProcessStatistics(
            candidate_instances_generated=np.int64(3),
            eliminated_by_target_truth_table=np.int64(3),
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "stats.json"
            statistics.write_json(str(output))
            saved = json.loads(output.read_text())
        self.assertEqual(saved["candidate_instances_generated"], 3)
        self.assertTrue(saved["counters_reconcile"])

    def test_completed_form_statistics_accumulate_transactionally(self) -> None:
        run = ProcessStatistics(candidate_instances_generated=10, eliminated_by_saturation=10)
        completed_form = ProcessStatistics(
            structural_forms_completed=1,
            candidate_instances_generated=5,
            eliminated_by_target_truth_table=3,
            eliminated_by_saturation=2,
        )
        run.accumulate(completed_form)
        self.assertEqual(run.structural_forms_completed, 1)
        self.assertEqual(run.candidate_instances_generated, 15)
        self.assertEqual(run.eliminated_by_saturation, 12)
        self.assertTrue(run.counters_reconcile)

    def test_later_model_can_eliminate_an_unresolved_call_without_double_counting(self) -> None:
        statistics = ProcessStatistics(
            candidate_instances_generated=1,
            vampire_calls=1,
            vampire_unresolved=1,
            eliminated_by_new_countermodels=1,
            survivors_written=0,
        )
        self.assertTrue(statistics.counters_reconcile)

    def test_round_robin_shards_are_complete_and_balanced(self) -> None:
        for total in range(20):
            counts = [shard_item_count(total, index, 3) for index in range(3)]
            self.assertEqual(sum(counts), total)
            self.assertLessEqual(max(counts) - min(counts), 1)


if __name__ == "__main__":
    unittest.main()
