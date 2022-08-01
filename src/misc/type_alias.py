from typing import Any


class DataTypes:
    """custom type annotations."""

    TexPkg: list[str] # packages imported
    SecSizes: dict[str, int] # sizes of sections e.g. subsection, etc ...
    RawConf: dict[str, Any]
    TexConf: tuple[ # general configuration file
            str,
            TexPkg,
            int,
            str,
            str,
            SecSizes,
            str,
            str,
            bool,
            str,
            str,
            bool,
            str
        ]

