# Config use

The program provides a configuration that can be easily modified by the user
for the configuration of the LaTeX file to be generated, which can be modified
via the config file (stored in `$HOME/.config/simtex/simtex.json`), or
directly from the commandline options of the program.

## Rules

1. `FOR: str | list[str] -> ["markdown", "md", "rst", "txt",
"text"]`, markers/rules for specific file type.
2. `CODE_BLOCKS: str -> ```_, for code blocks, using lstlisting
environment.
3. `IMAGE: str -> "![]()"`, for images, using figure environment. ++
4. `LINKS: str -> "[]()"`, for href environment. ++
5. `SECTION: str -> "#"`, for sections part.
6. `SUBSECTION: str -> "##"`, for subsections part.
7. `SUBSUBSECTION: str -> "###"`, for subsubsections part.
8. `PARAGRAPH: str -> "####"`, for paragraph part.
9. `SUBPARAGRAPH: str -> "#####"`, for subparagraph part.
10. `INLINE_MATH: str -> "$"`, for inline maths, uses equation environment.
11. `PARAGRAPH_MATH: str -> "$$"`, for paragraph maths, using align
environment. **Note: if there is no `&`, the program will insert `&` in the first `=`**.
12. `INLINE_CODE: str -> `\`, for inline code, using `\\textttt`. ++
13. `BOLD: list[str] -> ["**", "**<text>**"]`, for bold text
(uses `\textbf{<text>}`). The first item is for marker, and the second item is the patstern. ++
14. `ITALICS: list[str] -> ["_", "_<text>_"]`, for italized text.
The first item is for marker, and the second item is the pattern. ++
15. `EMPH: list[str] -> ["!*", "!*<text>!*"]`, for emphasized text.
The first item is for marker, and the second item is the pattern. ++
16. `STRIKE: list[str] -> ["~~", "~~<text>~~"]`. ++
17. `SUPSCRIPT: list[str] -> ["^^", "^^<text>^^"]`, for superscript in text mode. ++
18. `SUBSCRIPT: list[str] -> ["-^", "-^<text>-^"]_, for superscript. ++
19. `ULINE: list[str] -> ["._", "._<text>._"]`, for underlines. ++
20. `QUOTE: list[str] -> "`, for inline quotes.
**Note: the program does not accept single quotations**. ++
21. `BQUOTE: str -> ">"`, for block quotes.
22. `NONUM: str -> "*"`, for toggling nonumber in section in documents.

> ++ **Uses: regex. Note: do not replace `(.*?)`**

## Parameters: Document

1. `DOC_CLASS: str -> "article"`, currently only supports article.
2. `DEF_FONT: str -> "Latin Modern Roman (lmodern)"` (provided by
`lmodern` package), supports any font that has the package installed. Only package that is installed.
3. `FONT_SIZE: int -> 12`, font size of the general text in
article, sections, title, and other text is excluded.
4. `MARGIN: int -> 1`, currenty only supports equal margin to
all sides. **Unit: in.**
5. `PAPER_SIZE: str -> "a4paper"`, supports other paper sizes,
such as letter, and legal, refer to documentation of LaTeX for further information.
6. `INDENT_SIZE: int -> 24`, size of indentation. **Unit: pt**
7. `SLOPPY: bool -> true`, whether to use `\sloppy`.
8. `CODE_FONT: str -> "DejaVuSansMono"`, font to use in
`lstlistings` environment and `\texttt` command.
9. `PACKAGES: list[str]` the basic needs that maybe used by
general population_, this ranges from math tools, to some preferential options such as footnote symbols, as well as other symbols that maybe used.
10. `FOOTNOTE: str -> "footnote"`, symbol of footnote to be used
in footnote command.
11. `SECTION_SIZES: dict[str, int | str] -> "<DEF>"`_ (the
oversized sections), sizes of the section.

    a. `main` == `\section`

    b. `sub` == `\subsection`

    c. `subsub` == `\subsubsection`

12. `COLOR_LINKS: bool -> true`, whether to color the links,
13. `LINK_COLORS: str -> "BLUE"`, color of links.
14. `AUTHOR: str -> "John Doe"`.
15. `DATE: str -> <NOW>` of conversion in format of
(`%B %d, %Y` -- e.g. June, 27. 2055).
16. `MAKE_TITLE: bool -> true`, whether to create the title or not.
specified in commandline options.
18. `OUTPUT_FOLDER: str -> <input file folder>/out`, where the files/generated
output will be saved.
19. `COMPILER: str -> "pdflatex"`, the compiler the program will
use to compile the source, currently supports `xetex`, `luatex`, and `pdflatex`,
although virtually allows for anything given that the compiler is on `$PATH` and
is installed and is functional.
20. `ENCODE: str -> "UTF8"`, encoding of the document, although
not necessary to be changed.
21. `REPLACE: bool -> false`, whether to replace UTF8 or any other ascii
string that points to a particular command.
23. `TWOCOLS: bool -> false`, whether to turn the document to a two columns.
24. `ASSUME_YES: bool -> false`, to assume yes in every prompt.
25. `HLINE: bool -> true`, whether to add `\hline` after end of every row.
26. `HLINE_ENDING_COUNT: int -> 1`, the number of `\hline` in the final row.
27. `COLUMNLINE_COUNT: int -> 1`, the number of column border in the outer most column.
28. `TABLE_HEAD_FORMAT: str -> "bold"`, the formatting of table headings.
