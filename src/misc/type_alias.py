from typing import Any


class DataTypes:
    """custom type annotations."""

    TexPkg: list[str] # packages imported
    SecSizes: dict[str, int] # sizes of sections e.g. subsection, etc ...
    RawConf: dict[str, Any]
    TexConf: tuple[ # general configuration file
            str,
            str,
            int,
            bool,
            TexPkg,
            SecSizes,
            str,
            str,
            bool
        ]

