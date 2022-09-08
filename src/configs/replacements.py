from dataclasses import dataclass


@dataclass(frozen=True)
class Replacements:
    """Replacement of some math symbols and their respective LaTeX commands."""

    replacements: dict[str, str]
