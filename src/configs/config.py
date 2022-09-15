from dataclasses import dataclass


@dataclass
class Config:
    """Dataclass for configuration of the document
    file, its metadata and the program itself.

    Params:
        doc_class -- the type of the document.
        doc_font -- main document font.
        font_size -- size of the main font.
        margin -- margin of all sides in the document.
        paper_size -- size of the paper.
        indent_size -- size of indent.
        sloppy -- whether to use sloppy.
        code_font -- font to be used in listings.
        cfont_scale -- scaling of the code font.
        packages -- packages to include in imports.
        footnote -- symbol to be used for footnote.
        section_sizes -- size of the sections.
        links -- whether to parse links.
        link_color -- color of hyperlinks.
        author -- default author of the document.
        date -- date to be used in document.
        make_title -- whether to invoke \maketitle.
        output_folder -- name of the folders where the output would
            be placed.
        compiler -- compiler to be used for compilation of the
            output .tex file.
        encode -- encoding of the document.
        replace -- whether to replace UTF8 and other symbols with
            their respective LaTeX commands.
        twocols -- whether to use two column.
        assume_yes -- whether to set assume yes by default.
        hline -- whether to put \hline every end of the row.
        hline_ec -- number of \hline that will be included every
            end of the row.
        collinec -- column line end count -- the number of column border
            that will be included.
        thead_for -- formatting of the table headings.
    """

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
    packages: list[str | list[str]]
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
    autocorrect: bool
    autocorrect_lang: str
