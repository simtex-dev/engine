from typing import TextIO, Any, IO

from src.config import Config
from src.utils.logger import Logger


def format_body(
        log: Logger, config: Config, start: int, out_file: str
    ) -> None:
    """Format the document body of the generated LaTeX file."""

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

            i: int
            for i, line in enumerate(ref_tex[start:]):
                if i < ignore:
                    continue

                if line.startswith(r"\begin{lstlisting}"):
                    for j, codes in enumerate(ref_tex.copy()[i+start:]):
                        file.write(codes)
                        if codes.startswith(r"\end{lstlisting}"):
                            ignore = j+i+1
                            break

                    continue
                file.write(f"\t{line}")
            file.write("\\end{document}")
    except (FileNotFoundError, OSError, PermissionError, IOError) as Err:
        log.logger(
            "E", f"{Err}. Cannot format the document, aborting ..."
        )
