"""
ci_cd_pipeline.py
-----------------
CI/CD pipeline module for Jetstream LLC.

Includes:
- Full error handling
- Detection of missing tools (flake8, pytest)
- Clear console output
- Safe execution even if tests/linters are missing

This module can be run locally or inside GitHub Actions.
"""

import subprocess
import sys
from pathlib import Path


class CICDPipeline:
    """
    Encapsulates CI/CD-related commands so they can be reused
    across local development and automated pipelines.
    """

    def __init__(self, project_root: str = "."):
        """
        project_root:
            Base directory of the Jetstream project.
        """
        self.root = Path(project_root).resolve()

    # ---------------------------------------------------------
    # Helper: Run a shell command safely
    # ---------------------------------------------------------
    def _run_command(self, command: list, description: str) -> int:
        """
        Runs a shell command with error handling.

        Parameters:
            command: List of command arguments
            description: Text describing what the command does

        Returns:
            Exit code (0 = success, non-zero = failure)
        """
        print(f"[CI/CD] {description}...")

        try:
            result = subprocess.run(
                command,
                cwd=self.root,
                check=False  # Do not raise exceptions on failure
            )
            return result.returncode

        except FileNotFoundError:
            print(f"[CI/CD] ERROR: Required tool not found → {command[0]}")
            return 1

    # ---------------------------------------------------------
    # Step 1: Linting
    # ---------------------------------------------------------
    def run_lint(self) -> int:
        """
        Runs linting using flake8.
        Returns exit code.
        """
        return self._run_command(
            ["flake8", "."],
            "Running lint with flake8"
        )

    # ---------------------------------------------------------
    # Step 2: Testing
    # ---------------------------------------------------------
    def run_tests(self) -> int:
        """
        Runs the test suite using pytest.
        Returns exit code.
        """

        # Check if tests folder exists
        tests_path = self.root / "tests"
        if not tests_path.exists():
            print("[CI/CD] WARNING: No tests/ directory found. Skipping tests.")
            return 0  # Not an error

        return self._run_command(
            [sys.executable, "-m", "pytest", "tests"],
            "Running tests with pytest"
        )

    # ---------------------------------------------------------
    # Full Pipeline
    # ---------------------------------------------------------
    def run_pipeline(self) -> int:
        """
        Runs the full CI/CD pipeline sequence.

        Steps:
        1. Lint
        2. Tests

        Returns:
            0 if all steps succeed, non-zero otherwise.
        """

        # Step 1: Lint
        lint_code = self.run_lint()
        if lint_code != 0:
            print("[CI/CD] ❌ Linting failed.")
            return lint_code

        # Step 2: Tests
        test_code = self.run_tests()
        if test_code != 0:
            print("[CI/CD] ❌ Tests failed.")
            return test_code

        print("[CI/CD] ✅ Pipeline completed successfully.")
        return 0


# ---------------------------------------------------------
# Script Entry Point
# ---------------------------------------------------------
if __name__ == "__main__":
    """
    Allows: python ci_cd_pipeline.py
    to run the full pipeline locally or in CI.
    """
    pipeline = CICDPipeline(".")
    exit_code = pipeline.run_pipeline()
    sys.exit(exit_code)
