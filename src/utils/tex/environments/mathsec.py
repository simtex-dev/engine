from typing import TextIO


def mathsec(
        line: str,
        rule: str,
        out_file: TextIO,
        sources: list[str],
        i: int,
        ref: int
    ) -> int:
    maths: list[str] = []

    if line.strip() == rule: # for align
        out_file.write("\\begin{align}\n")

        eqs: str; j: int
        for j, eqs in enumerate(sources[i+1:]):
            if eqs.strip() == rule:
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
    else:
        out_file.write(
            (
                "\\begin{equation}\n"
                f"\t{line[2:-3]}\n"
                "\\end{equation}\n"
            )
        )

    return ref
