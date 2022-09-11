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

    if line.strip() == rule or line.strip() in [f"{rule}--", f"{rule} --"]: # for align
        if line.strip().endswith("--"):
            align_env: str = "align*"
        else:
            align_env = "align"

        out_file.write(f"\n\\begin{{{align_env}}}\n")

        eq: str; cur: int
        for cur, eq in enumerate(source[start+1:]):
            if eq.strip() == rule:
                end = cur+1+start
                break

            eq = eq.replace("\n", "").strip()
            if "&" not in eq:
                if "=" in eq and "\\text{" not in eq:
                    eq = eq.replace("=", "&=", 1)
                else:
                    eq = f"&{eq}"

            terminator: str
            for terminator in [r"--\\", "--", r"\\--"]:
                if eq.endswith(terminator):
                    eq = eq.removesuffix(terminator)
                    eq = f"{eq} \\nonumber"
                    break

            if eq.startswith((r"&\text", r"\text")):
                eq = f"{eq} \\nonumber"

            if not eq.endswith(r"\\"):
                eq = f"{eq} \\\\\n"
            else:
                eq = f"{eq} \n"

            maths.append(eq)

        try:
            maths[-1] = maths[-1].replace("\\\\\n", "\n")
        except IndexError:
            pass

        for eq in maths:
            out_file.write(f"\t{eq}")

        out_file.write(f"\\end{{{align_env}}}\n")
    else:
        end = start+1
        out_file.write(
            (
                "\n\\begin{equation}\n"
                f"\t{line.replace(rule, '')}\n"
                "\\end{equation}\n"
            )
        )

    return end
