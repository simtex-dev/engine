from dataclasses import dataclass


@dataclass(frozen=True)
class Rules:
    """Dataclass for configuration of the parser."""

    files: list[str]
    code: str
    image: str
    links: str
    section: str
    sectionn: str
    subsection: str
    subsectionn: str
    subsubsection: str
    subsubsectionn: str
    paragraph: str
    paragraphn: str
    subparagraph: str
    subparagraphn: str
    paragraph_math: str
    inline_math: list[str]
    inline_code: list[str]
    bold: list[str]
    italics: list[str]
    emph: list[str]
    strike: list[str]
    supscript: list[str]
    subscript: list[str]
    uline: list[str]
    quote: list[str]
    bquote: str
    nonum: str
