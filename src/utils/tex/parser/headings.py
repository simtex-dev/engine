from datetime import datetime
from typing import IO, Any, TextIO

from src.configs.config import Config
from src.utils.logger import Logger


def headings(
        log: Logger,
        config: Config,
        title: str,
        out_file: TextIO
    ) -> int:
    """Create the headings of the LaTeX file.

    Args:
        log -- for logging.
        config -- configuration of the document metadata, which includes,
            formatting, packages to use among others, refer to simtex.json.
        title -- title of the document.
        out_file -- where the translated line will be written.

    Returns:
        The number of lines used by the headings.
    """

    CONST: int = 12
    sections: dict[str, str] = {
            "main": (
                    "\n%\ size config of sections"
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
            (
                "\documentclass"
                f"[{config.font_size}pt,"
                f" {config.encode}]"
                f"{{{config.doc_class}}}\n"
            ),
            (
                "% font\n"
                "\\usepackage"
                f"{{{config.doc_font}}}"
                "\n\n% packages"
            )
        ]

    if config.date == "<NOW>":
        config.__setattr__("date", datetime.now().strftime("%B %d, %Y"))

    pkgs_: str | list[str]
    for pkgs_ in config.packages:
        if isinstance(pkgs_, list):
            try:
                if pkgs_[0] == "geometry":
                    param: str = (
                            pkgs_[1]
                                .replace(
                                    "<MARGIN>",
                                    f"{config.margin}in"
                                )
                                .replace(
                                    "<PAPER_SIZE>",
                                    config.paper_size
                                )
                        )
                elif pkgs_[0] == "hyperref":
                    param = pkgs_[1].replace(
                            "<LINK_COLORS>",
                            config.link_color
                        )
                else:
                    param = pkgs_[1]

                pkg = f"[{param}]{{{pkgs_[0]}}}"
            except IndexError:
                log.logger(
                    "e", f"Error detected in package: {pkgs_}, skipping ..."
                )
                continue
        else:
            pkg = f"{{{pkgs_}}}"

        headings.append(f"\\usepackage{pkg}")

    headings.append(
        (
            "\\usepackage"
            f"[scaled={config.cfont_scale}]"
            f"{{{config.code_font}}}"
        )
    )

    sec_sizes: str | int; sec_val: str
    for sec_sizes, sec_val in zip(
            config.section_sizes.values(), sections.values()
        ):
        if str(sec_sizes) == "<DEF>":
            CONST -= 1
        else:
            headings.append(
                sec_val.replace(
                    "<SECTION_SIZES>",
                    str(sec_sizes)
                )
            )

    headings.extend(
        [
            (
                "\n% basic config"
                "\n\setlength"
                "\parindent"
                f"{{{config.indent_size}pt}}"
            ),
            (
                f"\\renewcommand{{\\thefootnote}}"
                f"{{\\fnsymbol{{{config.footnote}}}}}"
            )
        ]
    )

    if config.sloppy:
        headings.append(r"\sloppy")

    try:
        lstconf: IO[Any]
        with open(config.code_conf, "r", encoding="utf-8") as lstconf:
            headings.append("\n%\ lst listings config")
            for lines in lstconf.readlines():
                headings.append(lines.replace("\n", ""))
    except (FileNotFoundError, PermissionError) as Err:
        log.logger(
            "e", f"{Err}. Cannot read code config file, skipping ..."
        )

    headings.extend(
        [
            (
                "\n% paper info\n"
                f"\\title{{{title}}}"
            ),
            f"\\author{{{config.author}}}",
            f"\date{{{config.date}}}"
        ]
    )

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

    return len(headings)+CONST # 11 is the number of newlines created.
