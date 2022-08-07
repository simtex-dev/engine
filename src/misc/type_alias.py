from typing import NewType


class DataTypes:
    """custom type annotations."""

    TexPkg = NewType("TexPkg", list[str]) # packages imported
    SecSizes = NewType("SecSizes", dict[str, int]) # sizes of sections e.g. subsection, etc ...
    TexConf = NewType( # general configuration file
            "TexConf",
            (
                str,
                str,
                int,
                str,
                int,
                str,
                float,
                str,
                TexPkg,
                SecSizes,
                bool,
                str,
                str,
                str,
                bool,
                str
            )
        )
    RawConf = NewType("RawConf", dict[str, TexConf])

