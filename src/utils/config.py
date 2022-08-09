from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    """dataclass for configuration of the latex file."""
    doc_class: str
    doc_font: str
    font_size: int
    code_font: str
    cfont_scale: float
    code_conf: str
    packages: list[str]
    section_sizes: dict[str, int]
    links: bool
    link_color: str
    author: str
    date: str
    make_title: bool
    output_folder: str


@dataclass(frozen=True)
class Rules:
    """dataclass for configuration of the parser."""

    files: list[str]
    code: str
    image: str
    links: str
    section: str
    subsection: str
    subsubsection: str
    paragraph: str
    subparagraph: str
    inline_math: str
    paragraph_math: str