class DataTypes:
    """custom type annotations."""

    TexPkg: list[str] # packages imported
    SecSizes: dict[str] # sizes of sections e.g. subsection, etc ...
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

