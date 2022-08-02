from typing import TextIO, NoReturn

from src.misc.signs import Signs
from src.misc.type_alias import DataTypes


def headings(conf: DataTypes.TexConf, file: TextIO) -> None | NoReturn:
    """create the headings for the latex file."""

    SECTIONS: dict[str, str] = {
            "main": "section",
            "sub": "subsection",
            "subsub": "subsubsection",
            "para": "paragraph",
            "subpara": "subparagraph"
        }

    headings: list[str] = []

    try:
        for items in headings:
            pkg: str
            file.write(
                f"{pkg}\n"
            )
    except (
        IOError,
        SystemError,
        BlockingIOError,
        PermissionError
    ) as Err:
        raise SystemExit(f"{Signs.FAIL} Encountered {Err}, aborting ...")


