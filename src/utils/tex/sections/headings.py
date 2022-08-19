from datetime import datetime
from typing import IO, Any, TextIO

from src.config import Config
from src.utils.logger import Logger


def headings(
        log: Logger,
        config: Config,
        title: str,
        out_file: TextIO
    ) -> int:
    """Create the headings of the LaTeX file.

    Arguments:
    log: Logger -- for logging.
    config: Config -- configuration of the document metadata, which includes,
         formatting, packages to use among others, refer to simtex.json.
    title: str -- title of the document.
    out_file: TextIO -- where the translated line will be written.

    Returns the number of lines of the headings.
    """

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
            f"\documentclass[{config.font_size}pt]{{{config.doc_class}}}\n",
            f"% font\n\\usepackage{{{config.doc_font}}}\n\n% packages"
        ]

    if "<NOW>" in config.date:
        config.__setattr__("date", datetime.now().strftime("%B %d, %Y"))

    pkgs: str
    for pkgs in config.packages:
        if "margin" in pkgs:
            pkgs = (
                    pkgs
                        .replace("<MARGIN>", f"{config.margin}in")
                        .replace("<PAPER_SIZE>", config.paper_size)
                )
        elif "colorlinks" in pkgs:
            pkgs = pkgs.replace("<LINK_COLORS>", config.link_color)

        headings.append(f"\\usepackage{pkgs}")

    headings.append(
        f"\\usepackage[scaled={config.cfont_scale}]{{{config.code_font}}}"
    )

    sec_sizes: int; sec_val: str
    for sec_sizes, sec_val in zip(
            config.section_sizes.values(), SECTIONS.values()
        ):
        headings.append(sec_val.replace("<SECTION_SIZES>", str(sec_sizes)))

    headings.append(
        f"\n% basic config\n\setlength\parindent{{{config.indent_size}pt}}"
    )
    headings.append(
        f"\\renewcommand{{\\thefootnote}}{{\\fnsymbol{{{config.footnote}}}}}"
    )

    if config.sloppy:
        headings.append(r"\sloppy")

    lstconf: IO[Any]
    with open(config.code_conf, "r", encoding="utf-8") as lstconf:
        headings.append(f"\n% lst listings config")
        for lines in lstconf.readlines():
            headings.append(lines.replace("\n", ""))

    items: str
    for items in [
            f"\n% paper info\n\\title{{{title}}}",
            f"\\author{{{config.author}}}",
            f"\date{{{config.date}}}"
        ]:
        headings.append(items)

    try:
        log.logger("I", "Writing headings to file ...")
        for items in headings:
            out_file.write(f"{items}\n")
    except (
        IOError,
        SystemError,
        BlockingIOError,
        PermissionError
    ) as Err:
        log.logger(
            "E", f"{Err}. Cannot write headings to file, aborting ..."
        )
        raise SystemExit

    return len(headings)+11 # 11 is the number of newlines created.
