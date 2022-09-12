from dataclasses import dataclass


@dataclass(frozen=True)
class Replacements:
    """Replacement of some math symbols, that may either be UTF8
    or raw utf8 symbols with their respective LaTeX commands."""

    replacements: dict[str, str]
