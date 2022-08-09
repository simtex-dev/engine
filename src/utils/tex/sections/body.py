from re import findall

from typing import Any, TextIO


def body(filepath: str, rules: tuple[Any]) -> None:
    """Generate a LaTeX version of the given markdown file.

    Arguments:
    filepath: str -- the path of the file to convert (reference file).
    """

    file: TextIO
    with open(filepath, "r", encoding="utf-8") as file:
        text: list[str] = file.readlines()

    PARTS: dict[str, list[str]] = {
            "sections": [],
            "subsections": [],
            "subsubsections": [],
            "paragraphs": [],
            "subparagraphs": [],
            "images": [],
            "links": [],
            "code_blocks": {}
        }

    text_2: list[str] = text.copy()
    for i, line in enumerate(text):
        if line in ["", "\n"]:
            continue

        match line.split()[0].strip():
            case rules.section:
                PARTS["sections"].append(line)
            case rules.subsection:
                PARTS["subsections"].append(line)
            case rules.subsubsection:
                PARTS["subsubsections"].append(line)
            case rules.paragraph:
                PARTS["paragraphs"].append(line)
            case rules.subparagraph:
                PARTS["subparagraphs"].append(line)
            case _:
                if line.startswith(rules.code):
                    for n, code in enumerate(text_2[i+1:]):
                        if code.strip() == rules.code:
                            PARTS["code_blocks"][
                                    f"code_{len(PARTS['code_blocks'])}"
                                ] = text[i+1:i+n+1]
                            break

                parts: list[str] = line.split()
                for part in parts:
                    img_results: list[tuple[str]]
                    if (
                            img_results := findall(
                                    rules.image, part
                                )
                        ):
                        PARTS["images"].append(img_results)
                    elif (
                            link_results := findall(
                                    rules.links, part
                                )
                        ):
                        PARTS["images"].append(link_results)
