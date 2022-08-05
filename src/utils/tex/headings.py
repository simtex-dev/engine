from typing import TextIO, NoReturn

from src.misc.signs import Signs
from src.misc.type_alias import DataTypes


def headings(
        conf: DataTypes.TexConf,
        title: str,
        tex_template: TextIO = None
    ) -> None | NoReturn:
    """create the headings for the latex file."""

    SECTIONS: dict[str, str] = {
            "main": (
                    "\n% size config\n\sectionfont{\\fontsize{"
                    "<SECTION_SIZES>}{15}\selectfont}"
                ),
            "sub": (
                    "\subsectionfont{\\fontsize{"
                    "<SECTION_SIZES>}{15}\selectfont}"
                ),
            "subsub": (
                    "\subsubsectionfont{\\fontsize{"
                    "<SECTION_SIZES>}{15}\selectfont}"
                ),
        }

    headings: list[str] = [
            f"\documentclass[{conf[2]}pt]{conf[0]}\n",
            f"% font\n\\usepackage{{{conf[1]}}}\n\n% packages"
        ]

    pkgs: str
    for pkgs in conf[4]:
        headings.append(f"\\usepackage{pkgs}")

    sec_sizes: int
    sec_val: str
    for sec_sizes, sec_val in zip(
            conf[5].values(), SECTIONS.values()
        ):
        headings.append(
            sec_val.replace(
                "<SECTION_SIZES>", str(sec_sizes)
            )
        )

    items: str
    for items in [
            f"\n% paper info\n\\title{{{title}}}",
            f"\\author{{{conf[6]}}}",
            f"\date{{{conf[7]}}}"
        ]:
        headings.append(items)

    try:
        items: str
        for items in headings:
            tex_template.write(
                f"{items}\n"
            )
    except (
        IOError,
        SystemError,
        BlockingIOError,
        PermissionError
    ) as Err:
        raise SystemExit(f"{Signs.FAIL} Encountered {Err}, aborting ...")
