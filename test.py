"""Run the non-destructive Vampire 5.0.1 compatibility suite."""

import subprocess
import sys


subprocess.check_call(
    [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]
)
