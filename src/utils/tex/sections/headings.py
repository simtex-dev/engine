from typing import Any, TextIO, NoReturn

from src.misc.stdout import Signs


def headings(
        log: object,
        conf: tuple[Any],
        title: str,
        tex_template: TextIO = None
    ) -> None | NoReturn:
    """Create the headings of the LaTeX file."""

    SECTIONS: dict[str, str] = {
            "main": (
                    "\n"
                    r"% size config of sections"
                    "\n\sectionfont{\\fontsize{"
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
            f"\documentclass[{conf[2]}pt]{{{conf[0]}}}\n",
            f"% font\n\\usepackage{{{conf[1]}}}\n\n% packages"
        ]

    pkgs: str
    for pkgs in conf[6]:
        headings.append(f"\\usepackage{pkgs}")
    headings.append(f"\\usepackage[scaled={conf[4]}]{{{conf[3]}}}")

    sec_sizes: int
    sec_val: str
    for sec_sizes, sec_val in zip(
            conf[7].values(), SECTIONS.values()
        ):
        headings.append(
            sec_val.replace(
                "<SECTION_SIZES>", str(sec_sizes)
            )
        )

    lstconf: TextIO
    # with open(conf[5], "r", encoding="utf-8") as lstconf:
    #     headings.append(f"\n% lst listings config\n{lstconf.read()}")

    items: str
    for items in [
            f"% paper info\n\\title{{{title}}}",
            f"\\author{{{conf[10]}}}",
            f"\date{{{conf[11]}}}"
        ]:
        headings.append(items)

    try:
        print(f"{Signs.PROC} Writing headings to file ...")
        items: str
        # for items in headings:
        #     tex_template.write(f"{items}\n")
    except (
        IOError,
        SystemError,
        BlockingIOError,
        PermissionError
    ) as Err:
        log.logger("E", f"Encountered {Err}, aborting ...")
        raise SystemExit
