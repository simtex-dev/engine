from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
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
