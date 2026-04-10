# Jetstream MVC-style project structure generator.

from pathlib import Path


class ProjectArchitecture:
    # Creates the folder structure for Jetstream.

    def __init__(self, root_dir: str = "."):
        # Base directory where the structure will be created.
        self.root = Path(root_dir)

        self.directories = [
            self.root / "models",
            self.root / "views",
            self.root / "controllers",
            self.root / "services",
            self.root / "tests",
            self.root / "config",
            self.root / "utils"
        ]

    def create_structure(self) -> None:
        # Creates directories and adds __init__.py files.
        for directory in self.directories:
            directory.mkdir(parents=True, exist_ok=True)

            init_file = directory / "__init__.py"
            if not init_file.exists():
                init_file.write_text(f"# Jetstream package: {directory.name}\n")

    def summary(self) -> None:
        # Prints a clean summary of created folders.
        print("Jetstream MVC-style structure created:")
        for directory in self.directories:
            print(f" - {directory.name}")


if __name__ == "__main__":
    arch = ProjectArchitecture(".")
    arch.create_structure()
    arch.summary()


if __name__ == "__main__":
    arch = ProjectArchitecture(".")
    arch.create_structure()
    arch.summary()
