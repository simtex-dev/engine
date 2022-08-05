from typing import Any, NewType


class DataTypes:
    """custom type annotations."""

    TexPkg = NewType("TexPkg", list[str]) # packages imported
    SecSizes = NewType("SecSizes", dict[str, int]) # sizes of sections e.g. subsection, etc ...
    RawConf = NewType("RawConf", dict[str, Any])
    TexConf = NewType( # general configuration file
            "TexConf",
            tuple[
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
        )
