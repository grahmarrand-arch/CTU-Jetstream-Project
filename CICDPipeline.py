# CI/CD pipeline module for Jetstream LLC.
# This version is Render-safe and avoids triple-quoted strings.
# Includes:
# - Error handling
# - Detection of missing tools (flake8, pytest)
# - Clear console output
# - Safe execution even if tests/linters are missing

import subprocess
import sys
from pathlib import Path


class CICDPipeline:
    # Encapsulates CI/CD-related commands for local and automated pipelines.

    def __init__(self, project_root: str = "."):
        # project_root: Base directory of the Jetstream project.
        self.root = Path(project_root).resolve()

    def _run_command(self, command: list, description: str) -> int:
        # Runs a shell command with error handling.
        print(f"[CI/CD] {description}...")

        try:
            result = subprocess.run(
                command,
                cwd=self.root,
                check=False  # Do not raise exceptions on failure
            )
            return result.returncode

        except FileNotFoundError:
            print(f"[CI/CD] ERROR: Required tool not found -> {command[0]}")
            return 1

    def run_lint(self) -> int:
        # Runs linting using flake8.
        return self._run_command(
            ["flake8", "."],
            "Running lint with flake8"
        )

    def run_tests(self) -> int:
        # Runs the test suite using pytest.

        tests_path = self.root / "tests"
        if not tests_path.exists():
            print("[CI/CD] WARNING: No tests/ directory found. Skipping tests.")
            return 0  # Not an error

        return self._run_command(
            [sys.executable, "-m", "pytest", "tests"],
            "Running tests with pytest"
        )

    def run_pipeline(self) -> int:
        # Runs the full CI/CD pipeline sequence: lint then tests.

        lint_code = self.run_lint()
        if lint_code != 0:
            print("[CI/CD] Linting failed.")
            return lint_code

        test_code = self.run_tests()
        if test_code != 0:
            print("[CI/CD] Tests failed.")
            return test_code

        print("[CI/CD] Pipeline completed successfully.")
        return 0


if __name__ == "__main__":
    # Allows: python ci_cd_pipeline.py
    # to run the full pipeline locally or in CI.
    pipeline = CICDPipeline(".")
    exit_code = pipeline.run_pipeline()
    sys.exit(exit_code)
