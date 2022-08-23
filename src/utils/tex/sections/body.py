from re import sub
from typing import Callable, TextIO

from src.config import Rules
from src.utils.tex.environments.mathsec import mathsec
from src.utils.tex.environments.common_envs import commons
from src.utils.tex.environments.quotes import quotation
from src.utils.logger import Logger


def body(
        log: Logger, rules: Rules, in_file: str, out_file: TextIO
    ) -> list[str]:
    """Generate a LaTeX version of the given markdown file.

    Args:
        log -- for logging.
        rules -- rules that needs to be followed in translation.
        in_file -- path of the file to be converted to LaTeX.
        out_file -- where the translated line will be written.

    Returns:
        A list of files found in the input file.
    """

    line: str
    striptitle: Callable[
            [str, str], str
        ] = lambda line, def_rule: (
            line
                .replace(def_rule, "")
                .replace("\n", "")
                .strip()
        )
    title: Callable[
            [str, str, str], str
        ] = lambda line, command, def_rule: (
            f"\n\\{command}{{{striptitle(line, def_rule)}}}\n"
        )

    files: list[str] = []

    ref_file: TextIO
    with open(in_file, "r", encoding="utf-8") as ref_file:
        ref_tex: list[str] = ref_file.readlines()

    end: int = -1

    log.logger("I", "Writing the body to the document ...")

    cur: int # current index
    for cur, line in enumerate(ref_tex):
        if line in ["", "\n"] or cur <= end:
            continue

        # replace numerous \n, if there is any, with one \n
        line = sub(r"\n{2, 10}", "\n", line).strip()

        match line.split()[0].strip():
            case rules.section:
                out_file.write(
                    title(line, "section", rules.section)
                )
            case rules.subsection:
                out_file.write(
                    title(line, "subsection", rules.subsection)
                )
            case rules.subsubsection:
                out_file.write(
                    title(line, "subsubsection", rules.subsubsection)
                )
            case rules.paragraph:
                out_file.write(
                    title(line, "paragraph", rules.paragraph)
                )
            case rules.subparagraph:
                out_file.write(
                    title(line, "subparagraph", rules.subparagraph)
                )
            case _:
                if line.startswith(rules.paragraph_math): # math mode
                    end = mathsec(
                            line,
                            rules.paragraph_math,
                            out_file,
                            ref_tex,
                            cur,
                            end
                        )
                elif line.startswith(rules.bquote):
                    out_file.write("\n\\begin{displayquote}\n")
                    end = quotation(
                            log,
                            line,
                            rules,
                            ref_tex,
                            cur,
                            out_file
                        )
                    out_file.write("\\end{displayquote}\n")
                elif line.startswith(rules.code): # for code blocks
                    language: str = line[3:].replace("\n", "")
                    out_file.write(
                        "\n\\begin{lstlisting}"
                        f"[language={language.title()}]\n"
                    )

                    code: str; n: int
                    for n, code in enumerate(ref_tex[cur+1:]):
                        if code.strip() == rules.code:
                            out_file.write("\end{lstlisting}\n")
                            end = n+cur+1
                            break

                        out_file.write(code)
                else:
                    commons(
                        line,
                        line.split(),
                        rules,
                        files,
                        out_file
                    )

    return files
