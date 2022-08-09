from typing import Any, TextIO, NoReturn

from src.misc.stdout import Signs


def headings(
        log: object,
        conf: object,
        title: str,
        out_file: TextIO = None
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
            f"\documentclass[{conf.font_size}pt]{{{conf.doc_class}}}\n",
            f"% font\n\\usepackage{{{conf.doc_font}}}\n\n% packages"
        ]

    pkgs: str
    for pkgs in conf.packages:
        headings.append(f"\\usepackage{pkgs}")
    headings.append(
        f"\\usepackage[scaled={conf.cfont_scale}]{{{conf.code_font}}}"
    )

    sec_sizes: int
    sec_val: str
    for sec_sizes, sec_val in zip(
            conf.section_sizes.values(), SECTIONS.values()
        ):
        headings.append(
            sec_val.replace(
                "<SECTION_SIZES>", str(sec_sizes)
            )
        )

    lstconf: TextIO
    with open(conf[5], "r", encoding="utf-8") as lstconf:
        headings.append(f"\n% lst listings config\n{lstconf.read()}")

    items: str
    for items in [
            f"\n% paper info\n\\title{{{title}}}",
            f"\\author{{{conf.author}}}",
            f"\date{{{conf.date}}}"
        ]:
        headings.append(items)

    try:
        print(f"{Signs.PROC} Writing headings to file ...")
        items: str
        for items in headings:
            out_file.write(f"{items}\n")
    except (
        IOError,
        SystemError,
        BlockingIOError,
        PermissionError
    ) as Err:
        log.logger("E", f"Encountered {Err}, aborting ...")
        raise SystemExit
