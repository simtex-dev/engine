from typing import TextIO


def mathsec(
        rule: str,
        line: str,
        source: list[str],
        start: int,
        out_file: TextIO,
    ) -> int:
    """Handles the math found in the input, this includes paragraph math
    inline math, and aligned paragraph math.

    Arguments:
        rule -- rule that needs to be followed in translation.
        line -- line that will be analyzed and translated.
        out_file -- where the translated line will be written.
        source -- where the other lines of equation would be found.
        start -- where the parser/translator would start.
        ignore -- for knowing what line(s) to skip.

    Returns:
        An integer that denotes what line to skip.
    """

    maths: list[str] = []

    if line.strip() == rule: # for align
        out_file.write("\n\\begin{align}\n")

        eqs: str; mline: int
        for mline, eqs in enumerate(source[start+1:]):
            if eqs.strip() == rule:
                end = mline+1+start
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
        end = start+1
        out_file.write(
            (
                "\n\\begin{equation}\n"
                f"\t{line[2:-3]}\n"
                "\\end{equation}\n"
            )
        )

    return end
