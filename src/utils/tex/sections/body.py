from re import findall

from typing import Any, Optional, TextIO, IO

from src.utils.config import Rules


def body(
        filepath: str, rules: Rules, out_file: TextIO
    ) -> None:
    """Generate a LaTeX version of the given markdown file.

    Arguments:
    filepath: str -- the path of the file to convert (reference file).
    rules: object -- the rules to follow for parsing.
    out_file: textio -- where the output will be written.
    """
    # TODO: figure out to efficiently write the body into the file

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
                    .replace(
                        def_rule if def_rule is not None else "", ""
                    )
                    .replace("\n", "").strip()
            )
        return f"\n\\{command}{{{stripped_line}}}\n"

    file: IO[Any]
    with open(filepath, "r", encoding="utf-8") as file:
        text: list[str] = file.readlines()

    text_2: list[str] = text.copy()
    ref: int = -1

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
                if line.startswith(rules.paragraph_math):
                    out_file.write(
                        (
                            "\n\\begin{equation}\n"
                            f"\t{line[2:-3]}\n"
                            "\\end{equation}\n"
                        )
                    )
                elif line.startswith(rules.code):
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
                    for n, code in enumerate(text_2[i+1:]):
                        if code.strip() == rules.code:
                            out_file.write("\end{lstlisting}\n")
                            ref = n+i+1
                            break

                        out_file.write(code)
                else:
                    parts: list[str] = line.split()

                    part: str
                    for part in parts:
                        img_results: list[tuple[str, str]]
                        link_results: list[tuple[str, str]]

                        if (img_results := findall(rules.image, part)):
                            out_file.write(
                                (
                                    "\n\\begin{figure}\n"
                                    "\t\\includegraphics[width=\\textwidth]"
                                    f"{{{img_results[0][1]}}}\n"
                                    f"\t\\caption{img_results[0][0]}\n"
                                    "\\end{figure}\n"
                                )
                            )
                        elif (link_results := findall(rules.links, part)):
                            links: tuple[str, str] = link_results[0]
                            new_line: str = line.replace(
                                    f"[{links[0]}]({links[1]})",
                                    f"\\href{{{links[0]}}}{{{links[1]}}}"
                                )
                            out_file.write(f"\n{new_line}\n")
                        else:
                            out_file.write(f"\n{line}")
                            break
