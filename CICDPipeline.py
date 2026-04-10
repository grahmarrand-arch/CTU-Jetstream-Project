# CI/CD pipeline for Jetstream LLC.

import subprocess
import sys
from pathlib import Path


class CICDPipeline:
    # Encapsulates CI/CD commands for local and automated pipelines.

    def __init__(self, project_root="."):
        self.root = Path(project_root).resolve()

    def _run(self, command, description):
        print(f"[CI/CD] {description}...")
        try:
            result = subprocess.run(
                command,
                cwd=self.root,
                check=False
            )
            return result.returncode
        except FileNotFoundError:
            print(f"[CI/CD] ERROR: Missing tool → {command[0]}")
            return 1

    def install_dependencies(self):
        # Installs all Python dependencies from requirements.txt.
        req_file = self.root / "requirements.txt"
        if not req_file.exists():
            print("[CI/CD] ERROR: requirements.txt not found.")
            return 1

        return self._run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            "Installing dependencies"
        )

    def run_lint(self):
        return self._run(["flake8", "."], "Running flake8 linting")

    def run_tests(self):
        tests_path = self.root / "tests"
        if not tests_path.exists():
            print("[CI/CD] WARNING: No tests/ directory found. Skipping tests.")
            return 0

        return self._run(
            [sys.executable, "-m", "pytest", "tests"],
            "Running pytest test suite"
        )

    def run_pipeline(self):
        if self.install_dependencies() != 0:
            print("[CI/CD] Dependency installation failed.")
            return 1

        if self.run_lint() != 0:
            print("[CI/CD] Linting failed.")
            return 1

        if self.run_tests() != 0:
            print("[CI/CD] Tests failed.")
            return 1

        print("[CI/CD] Pipeline completed successfully.")
        return 0


if __name__ == "__main__":
    pipeline = CICDPipeline(".")
    sys.exit(pipeline.run_pipeline())
