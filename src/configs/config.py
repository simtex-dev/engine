from dataclasses import dataclass


@dataclass
class Config:
    """Dataclass for configuration of the latex file."""

    doc_class: str
    doc_font: str
    font_size: int
    margin: int
    paper_size: str
    indent_size: int
    sloppy: bool
    code_font: str
    cfont_scale: float
    code_conf: str
    packages: list[str]
    footnote: str
    section_sizes: dict[str, int | str]
    links: bool
    link_color: str
    author: str
    date: str
    make_title: bool
    output_folder: str
    compiler: str
    encode: str
    replace: bool
    twocols: bool
    assume_yes: bool
    hline: bool
    hline_ec: int
    collinec: int
    thead_for: str
