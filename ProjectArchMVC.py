"""

Creates the MVC-style folder structure for Jetstream.

- Prints clean folder names
- Avoids confusing absolute paths unless needed
- Keeps full comments for clarity
"""

from pathlib import Path


class ProjectArchitecture:
    """
    Handles creation of the Jetstream MVC-style directory structure.
    """

    def __init__(self, root_dir: str = "."):
        """
        root_dir:
            Base directory where the structure will be created.
            Using Path(root_dir) keeps paths relative and clean.
        """
        self.root = Path(root_dir)

        # Define the folder structure
        self.directories = [
            self.root / "models",
            self.root / "views",
            self.root / "controllers",
            self.root / "services",
            self.root / "tests",
            self.root / "config",
            self.root / "utils",
        ]

    def create_structure(self) -> None:
        """
        Creates all directories and adds __init__.py files
        so each folder becomes a Python package.
        """
        for directory in self.directories:
            directory.mkdir(parents=True, exist_ok=True)

            # Create __init__.py if missing
            init_file = directory / "__init__.py"
            if not init_file.exists():
                init_file.write_text(
                    f"# Jetstream package: {directory.name}\n"
                )

    def summary(self) -> None:
        """
        Prints a clean summary of created folders.
        """
        print("Jetstream MVC-style structure created:")
        for directory in self.directories:
            print(f" - {directory.name}")


if __name__ == "__main__":
    arch = ProjectArchitecture(".")
    arch.create_structure()
    arch.summary()
