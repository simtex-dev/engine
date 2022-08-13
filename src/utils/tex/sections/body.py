from re import findall

from typing import Any, Optional, TextIO, IO

from src.utils.config import Rules
from src.utils.logger import Logger


def title(
        line: str,
        command: str,
        def_rule: Optional[str] = None,
        params: Optional[str] = None,
        env: bool = False
    ) -> str:
    """Get the title from the line."""

    if env:
        attach: str = f"[{params}]\n" if params is not None else "\n"
        return f"\n\\begin{{{command}}}{attach}"

    stripped_line: str = (
            line
                .replace(def_rule if def_rule is not None else "", "")
                .replace("\n", "").strip()
        )
    return f"\n\\{command}{{{stripped_line}}}\n"


def body(
        log: Logger, filepath: str, rules: Rules, out_file: TextIO
    ) -> None:
    """Generate a LaTeX version of the given markdown file.

    Arguments:
    filepath: str -- the path of the file to convert (reference file).
    rules: object -- the rules to follow for parsing.
    out_file: textio -- where the output will be written.
    """

    file: IO[Any]
    with open(filepath, "r", encoding="utf-8") as file:
        text: list[str] = file.readlines()

    ref: int = -1

    log.logger("I", "Writing the body to the document ...")

    i: int; line: str
    for i, line in enumerate(text):
        if line in ["", "\n"]:
            continue

        if i <= ref:
            continue

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
                    maths: list[str] = []

                    if line.strip() == rules.paragraph_math: # for align
                        out_file.write("\\begin{align}\n")

                        eqs: str; j: int
                        for j, eqs in enumerate(text.copy()[i+1:]):
                            if eqs.strip() == rules.paragraph_math:
                                ref = j+i+1
                                break

                            if "&" not in eqs:
                                eqs = eqs.replace("=", "&=", 1)

                            eqs = eqs.replace("\n", "")
                            maths.append(f"{eqs}\\\\\n")

                        maths[-1] = maths[-1].replace("\\\\\n", "\n")
                        for eqs in maths:
                            out_file.write(f"\t{eqs}")

                        out_file.write("\\end{align}\n")
                    else: # for single line/equation
                        out_file.write(
                            (
                                "\\begin{equation}\n"
                                f"\t{line[2:-3]}\n"
                                "\\end{equation}\n"
                            )
                        )
                elif line.startswith(rules.code): # for code blocks
                    language: str = line[3:].replace("\n", "")
                    out_file.write(
                        title(
                            line,
                            "lstlisting",
                            params=f"language={language}",
                            env=True
                        )
                    )

                    code: str; n: int
                    for n, code in enumerate(text.copy()[i+1:]):
                        if code.strip() == rules.code:
                            out_file.write("\end{lstlisting}\n")
                            ref = n+i+1
                            break

                        out_file.write(code)
                else:
                    parts: list[str] = line.split(" ")
                    skip_line: bool = False

                    part: str
                    try:
                        new_line: str = line

                        for part in parts:
                            img_results: list[tuple[str, str]]
                            link_results: list[tuple[str, str]]

                            if (img_results := findall(rules.image, part)):
                                out_file.write(
                                    "\\begin{figure}[h]\n"
                                    "\t\\includegraphics[width=\\textwidth]"
                                    f"{{{img_results[0][1]}}}\n"
                                    f"\t\\caption{{{img_results[0][0]}}}\n"
                                    "\\end{figure}\n"
                                )
                                skip_line = True
                                break

                            if (link_results := findall(rules.links, part)):
                                link: tuple[str, str]
                                for link in link_results:
                                    new_line = new_line.replace(
                                            f"[{link[0]}]({link[1]})",
                                            f"\\href{{{link[0]}}}{{{link[1]}}}"
                                        )
                            elif (
                                    inline_codes := findall(
                                            rules.inline_code, part
                                        )
                                ):
                                codes: tuple[str]
                                for codes in inline_codes:
                                    new_line = new_line.replace(
                                            f"`{codes}`",
                                            f"\\texttt{{{codes}}}"
                                        )
                    finally:
                        if not skip_line:
                            new_line = (
                                    new_line
                                        .replace("_", r"\_")
                                        .replace("\n", "\n")
                                )
                            out_file.write(f"\n{new_line}\n")


def format_body(log: Logger, start: int, filepath: str) -> None:
    """Format the document body of the generated LaTeX file."""

    try:
        ref: TextIO
        with open(filepath, "r", encoding="utf-8") as ref:
            lines: list[str] = ref.readlines()
    except (FileNotFoundError, OSError, PermissionError, IOError):
        log.logger("E", "Cannot format the document.")
    else:
        log.logger("I", "Formatting the document ...")

        ignore: int = -1

        file: IO[Any]
        with open(filepath, "w", encoding="utf-8") as file:
            line: str
            for line in lines[:start]:
                file.write(line)

            file.write("\n\\begin{document}\n")

            i: int
            for i, line in enumerate(lines[start:]):
                print(i, ignore)
                if i < ignore:
                    continue

                if line.startswith(r"\begin{lstlisting}"):
                    for j, codes in enumerate(lines.copy()[i+start:]):
                        file.write(codes)
                        if codes.startswith(r"\end{lstlisting}"):
                            ignore = j+i+1
                            break

                    continue

                file.write(f"\t{line}")

            file.write("\\end{document}")
