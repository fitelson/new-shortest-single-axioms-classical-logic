import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from Globals import ConstantSpec, ModelSpec, OperationSpec, PredicateSpec
from ModelTools import VampireOutputTools
from TheoremProverUtils import TheoremProverWrapper, VampireWrapper
from TreeForms import ProcessStatistics


ROOT = Path(__file__).resolve().parents[1]
VAMPIRE = ROOT / "theorem_provers" / "vampire"


CANDIDATES = {
    "baan": "a(A,A)=A",
    "bac": "i(A,A)=A",
    "bacf": "i(A,f)=A",
    "bacn": "i(n(A),A)=A",
    "baon": "o(n(A),A)=A",
    "cf": "t(i(A,f))",
    "cn": "t(i(n(A),A))",
    "ct": "t(i(A,o))",
    "hadn": "t(o(n(A),A))",
    "luk3vi": "t(i(n(A),A))",
    "ran": "t(n(a(A,A)))",
}


def load_spec(config: dict) -> ModelSpec:
    return ModelSpec(
        PredicateSpec.parse(config["predicate"]),
        tuple(OperationSpec.parse(op) for op in config["operators"]),
        tuple(ConstantSpec.parse(constant) for constant in config["constants"]),
    )


class Vampire501CompatibilityTests(unittest.TestCase):
    def test_reference_version(self) -> None:
        result = subprocess.run(
            [str(VAMPIRE), "--version"], capture_output=True, text=True, check=True
        )
        self.assertTrue(result.stdout.startswith("Vampire 5.0.1"), result.stdout)

    def test_generated_quantifier_scopes_entire_formula(self) -> None:
        wrapper = TheoremProverWrapper("", None, "")
        line = wrapper._fof_formula_to_fof_line(
            "(p(P,Q) & q(Q,R))", "scope", "conjecture"
        )
        self.assertEqual(
            line,
            "fof(scope, conjecture, ![P,Q,R]: ((p(P,Q) & q(Q,R)))).\n",
        )

    def test_every_run_template_parses_in_vampire_5_0_1(self) -> None:
        for config_path in sorted((ROOT / "runs").glob("*_definition.json")):
            run_name = config_path.stem.removesuffix("_definition")
            with self.subTest(run=run_name):
                config = json.loads(config_path.read_text())
                wrapper = TheoremProverWrapper("", load_spec(config), "")
                contents = "\n".join(config["vampire_template"]) + "\n"
                contents += wrapper._fof_formula_to_fof_line(
                    CANDIDATES[run_name], "cand", "axiom"
                )
                with tempfile.NamedTemporaryFile(
                    mode="w", suffix=".in", encoding="utf-8"
                ) as input_file:
                    input_file.write(contents)
                    input_file.flush()
                    result = subprocess.run(
                        [
                            str(VAMPIRE),
                            "--mode",
                            "clausify",
                            "--input_syntax",
                            "tptp",
                            input_file.name,
                        ],
                        capture_output=True,
                        text=True,
                    )
                output = result.stdout + result.stderr
                self.assertEqual(result.returncode, 0, output)
                self.assertNotIn("User error:", output)
                self.assertNotIn("Parsing Error", output)

    def test_vampire_result_classification(self) -> None:
        self.assertEqual(
            VampireWrapper.classify_output("% SZS status Theorem for p"), "proof"
        )
        self.assertEqual(
            VampireWrapper.classify_output("% SZS status Unsatisfiable for p"),
            "proof",
        )
        self.assertEqual(
            VampireWrapper.classify_output(
                "% Finite Model Found!\n% SZS status CounterSatisfiable for p"
            ),
            "finite_model",
        )
        self.assertEqual(
            VampireWrapper.classify_output(
                "% SZS status CounterSatisfiable for p\n"
                "% Termination reason: Satisfiable"
            ),
            "saturated",
        )
        self.assertEqual(
            VampireWrapper.classify_output(
                "% Refutation not found, non-redundant clauses discarded"
            ),
            "saturated",
        )
        self.assertEqual(
            VampireWrapper.classify_output(
                "% Refutation not found, incomplete strategy\n% SZS status Timeout for p"
            ),
            "unresolved",
        )
        self.assertEqual(
            VampireWrapper.classify_output(
                "% Refutation not found, non-redundant clauses discarded\n"
                "% SZS status Theorem for p"
            ),
            "proof",
        )

    def test_process_statistics_reconcile_disjoint_outcomes(self) -> None:
        statistics = ProcessStatistics(
            candidate_instances_generated=100,
            eliminated_by_target_truth_table=60,
            eliminated_by_cached_countermodels=20,
            eliminated_by_new_countermodels=10,
            eliminated_by_saturation=5,
            survivors_written=5,
        )
        self.assertEqual(statistics.accounted_candidates, 100)
        self.assertTrue(statistics.counters_reconcile)

    def test_vampire_5_0_1_constant_definition(self) -> None:
        output = """
tff('declare_$i1',type,'fmb_$i_1':$i).
tff('declare_$i2',type,'fmb_$i_2':$i).
tff(declare_f,type,f:$i).
tff(f_definition,axiom,f = 'fmb_$i_1').
"""
        _, order, constants = VampireOutputTools.order_and_constants(output)
        self.assertEqual(order, 2)
        self.assertEqual(constants, {"f": 0})


if __name__ == "__main__":
    unittest.main()
