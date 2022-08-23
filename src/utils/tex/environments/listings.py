from typing import TextIO

from src.config import Rules


def listings(
        rules: Rules,
        line: str,
        start: int,
        source: list[str],
        out_file: TextIO
    ) -> int:
    """For formatting of code blocks.

    Args:
        line -- line that will be analyzed and translated.
        rules -- rules that needs to be followed in translation.
        start -- where the parser/translator would start.
        out_file -- where the translated line will be written.
    """

    language: str = line[3:].replace("\n", "")
    out_file.write(
        "\n\\begin{lstlisting}"
        f"[language={language.title()}]\n"
    )

    code: str; cline: int
    for cline, code in enumerate(source[start+1:]):
        if code.strip() == rules.code:
            out_file.write("\end{lstlisting}\n")
            return cline+start+1

        out_file.write(code)
