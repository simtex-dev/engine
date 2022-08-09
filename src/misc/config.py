from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Config:
    TexPkg: list[str]
    """Configuration of the latex file."""
    SecSizes: dict[str, int]
    TexConf: tuple(
            str,
            str,
            int,
            str,
            int,
            str,
            float,
            str,
            list[str],
            dict[str, int],
            bool,
            str,
            str,
            str,
            bool,
            str
        )
    RawConf: dict[str, Any]
