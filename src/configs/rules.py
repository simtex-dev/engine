from dataclasses import dataclass


@dataclass(frozen=True)
class Rules:
    """Dataclass for configuration of the parser, this includes
    the markers that the parser will look for as well as the patterns.

    Params:
        files -- the type of files that simtex will convert.
        code -- the marker of code blocks lstlistings.
        image -- marker of figure/image insert \includegraphic.
        links -- hyperlinks in line \hyperlink.
        section -- \section
        sectionn -- \section*
        subsection -- \subsection
        subsectionn -- \subsection*
        subsubsection -- \subsubsection
        subsubsectionn -- \subsubsectionn
        paragraph -- \paragraph
        paragraphn -- \paragraphn
        subparagraph -- \subparagraph
        subparagraphn -- \subparagraph*
        paragraph_math -- for equation/align environment.
        inline_math -- for inline math $$.
        inline_code -- for inline code -> \\texttt.
        bold -- \\textbf
        italics -- \\textit
        emph -- \emph
        strike -- \sout
        supscript -- \\textsuperscript
        subscript -- \\textsubscript
        uline -- \\underline
        quote -- ``<text>''
        bquote -- block quote using csquote.
        nonum -- for numberless paragraph math lines.
    """

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
