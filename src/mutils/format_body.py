from typing import TextIO, Any, IO

from src.config import Config
from src.utils.logger import Logger


def format_body(
        log: Logger, config: Config, start: int, out_file: str
    ) -> None:
    """Format the document body of the generated LaTeX file.

    Args:
        log -- for logging.
        config -- configuration of the document metadata, which includes,
            formatting, packages to use among others, refer to simtex.json.
        start -- where the formatter will start, since the formatter
            simply just emphasize the order and the belongings of each
            environment using tabs.
        out_file -- where the output will be written.
    """

    try:
        ref: TextIO
        with open(out_file, "r", encoding="utf-8") as ref:
            ref_tex: list[str] = ref.readlines()

        log.logger("I", "Formatting the document ...")

        ignore: int = -1

        file: IO[Any]
        with open(out_file, "w", encoding="utf-8") as file:
            line: str
            for line in ref_tex[:start]:
                file.write(line)

            file.write("\n\\begin{document}\n")

            if config.make_title:
                file.write("\t\maketitle\n")

            cur: int
            for cur, line in enumerate(ref_tex[start:]):
                if cur < ignore:
                    continue

                if line.startswith(r"\begin{lstlisting}"):
                    for cline, codes in enumerate(ref_tex.copy()[cur+start:]):
                        file.write(codes)
                        if codes.startswith(r"\end{lstlisting}"):
                            ignore = cline+cur+1
                            break

                    continue
                file.write(f"\t{line}")
            file.write("\n\\end{document}")
    except (FileNotFoundError, OSError, PermissionError, IOError) as Err:
        log.logger(
            "E", f"{Err}. Cannot format the document, aborting ..."
        )
