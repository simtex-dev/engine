from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    """dataclass for configuration of the latex file."""
    TexConf: tuple[
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
        ]


@dataclass(frozen=True)
class Rules:
    """dataclass for configuration of the parser."""
    Rule: tuple[
            list[str],
            dict[str, str],
            str,
            str,
            str,
            str,
            str,
            str,
            str,
            dict[str, str],
            dict[str, str]
        ]
