from typing import TextIO


def mathsec(
        line: str,
        rule: str,
        out_file: TextIO,
        sources: list[str],
        start: int,
        end: int
    ) -> int:
    """Handles the math found in the input, this includes paragraph math
    inline math, and aligned paragraph math.

    Arguments:
    line: str -- line that will be analyzed and translated.
    rules: Rules -- rules that needs to be followed in translation.
    out_file: TextIO -- where the translated line will be written.
    sources: list[str] -- where the other lines of equation would be found.
    start: int -- where the parser/translator would start.
    end: int -- for knowing what line(s) to skip.

    Returns an integer that denotes what line to skip.
    """

    maths: list[str] = []

    if line.strip() == rule: # for align
        out_file.write("\\begin{align}\n")

        eqs: str; j: int
        for j, eqs in enumerate(sources[start+1:]):
            if eqs.strip() == rule:
                end = j+start+1
                break

            if "&" not in eqs:
                eqs = eqs.replace("=", "&=", 1)

            eqs = eqs.replace("\n", "")
            maths.append(f"{eqs}\\\\\n")

        maths[-1] = maths[-1].replace("\\\\\n", "\n")
        for eqs in maths:
            out_file.write(f"\t{eqs}")

        out_file.write("\\end{align}\n")
    else:
        out_file.write(
            (
                "\\begin{equation}\n"
                f"\t{line[2:-3]}\n"
                "\\end{equation}\n"
            )
        )

    return end
