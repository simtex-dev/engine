from dataclasses import dataclass


@dataclass
class Replacements:
    """Replacement of some math symbols and their respective LaTeX commands."""

    replacements: dict[str, str]
