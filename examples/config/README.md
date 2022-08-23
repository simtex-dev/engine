# Config use

The program, as of writing, provides 12 parameters for the configuration of the LaTeX file to be generated, which can be modified via the config file (stored in `$HOME/.config/simtex/simtex.json`), or directly from the commandline options of the program.

## Rules

1. `FOR: str | list[str]` -- _defaults -> [`markdown`, `md`, `rst`, `txt`, `text`]_, markers/rules for specific file type.
2. `CODE_BLOCKS: str` -- _defaults -> ```_, for code blocks, using lstlisting environment.
3. `IMAGE: str` -- _defaults -> `![]()`_, for images, using figure environment. **Uses: regex. Note: do not replace `([^]]+)`**.
4. `LINKS: str` -- _defaults -> `[]()`_, for href environment. **Uses: regex. Note: do not replace `([^]]+)`**.
5. `SECTION: str` -- _defaults -> `#`_, for sections part.
6. `SUBSECTION: str` -- _defaults -> `##`_, for subsections part.
7. SUBSUBSECTION: str` -- _defaults -> `###`_, for subsubsections part.
8. `PARAGRAPH: str` -- _defaults -> `####`_, for paragraph part.
9. `SUBPARAGRAPH: str` -- _defaults -> `#####`_, for subparagraph part.
10. `INLINE_MATH: str` -- _defaults -> `$`_, for inline maths, uses equation environment.
11. `PARAGRAPH_MATH: str` -- _defaults -> `$$`_, for paragraph maths, using align environment. **Note: if there is no `&`, the program will insert `&` in the first `=`**.
12. `INLINE_CODE: str` -- _defaults -> ``_, for inline code, using `\\textttt`. ++
13. `BOLD: list[str]` -- _defaults -> [`**`, `**<text>**`]_, for bold text (uses `\textbf{<text>}`). The first item is for marker, and the second item is the patstern. ++
14. `ITALICS: list[str]` -- _defaults -> [`_`, `_<text>_`]_, for italized text. The first item is for marker, and the second item is the pattern. ++
15. `EMPH: list[str]` -- _defaults -> [`!*`, `!*<text>!*`]_, for emphasized text. The first item is for marker, and the second item is the pattern. ++
16. `STRIKE: list[str]` -- _defaults -> [`~~`, `~~<text>~~`]_. ++
17. `SUPSCRIPT: list[str]` -- _defaults -> [`^^`, `^^<text>^^`]_, for superscript. ++
18. `SUBSCRIPT: list[str]` -- _defaults -> [`-^`, `-^<text>-^`]_, for superscript. ++
19. `ULINE: list[str]` -- _defaults -> [`._`, `._<text>._`]_, for underlines. ++
20. `QUOTE: list[str]` -- _defaults -> `"`_, for inline quotes. **Note: the program does not accept single quotations**. ++
21. `BQUOTE: str` -- _defaults -> `>`_, for block quotes.

> ++ **Uses: regex. Note: do not replace `(.*?)`**

## Parameters: Document

1. `DOC_CLASS: str` -- _defaults -> `article`_, currently only supports article.
2. `DEF_FONT: str` -- _defaults -> `Latin Modern Roman` `(lmodern)`_ (provided by lmodern package), supports any font that has the package installed. Only package that is installed.
3. `FONT_SIZE: int` -- _defaults -> `12`_, font size of the general text in article, sections, title, and other text is excluded.
4. `MARGIN: int` -- _defaults -> `1`_, currenty only supports equal margin to all sides. **Unit: in.**
5. `PAPER_SIZE: str` -- _defaults -> `a4paper`_, supports other paper sizes, such as letter, and legal, refer to documentation of LaTeX for further information.
6. `INDENT_SIZE: int` -- _defaults -> `24`_, size of indentation. **Unit: pt**
7. `SLOPPY: bool` -- _defaults -> `true`_, whether to use `\sloppy`.
8. `CODE_FONT: str` -- _defaults -> `DejaVuSansMono`_, font to use in `lstlistings` environment and `\texttt` command.
9. `PACKAGES: list[str]` -- _defaults -> the basic needs that maybe used by general population_, this ranges from math tools, to some preferential options such as footnote symbols, as well as other symbols that maybe used.
10. `FOOTNOTE: str` -- _defaults -> `footnote`_, symbol of footnote to be used in footnote command.
11. `SECTION_SIZES: dict[str, int | str]` -- _defaults -> `"<DEF>"`_ (the oversized sections), sizes of the section.

    a. `main` == `\section`

    b. `sub` == `\subsection`

    c. `subsub` == `\subsubsection`

12. `COLOR_LINKS: bool` -- _default -> `true`_, whether to color the links,
13. `LINK_COLORS: str` -- _default -> `BLUE`_, color of links.
14. `AUTHOR: str` -- _defaults -> `John Doe`_.
15. `DATE: str` -- _defaults -> `<current time>`_ of conversion in format of (%B %d, %Y -- e.g. June, 27. 2055).
16. `MAKE_TITLE: bool` -- _defaults -> `true`_, whether to create the title or not.
17. `FILE_NAME: str` -- _defaults -> `a.te"_, filename that to be used if not specified in commandline options.
18. `OUTPUT_FOLDER: str` -- _defaults -> `./out`_, where the files/generated output will be saved.
19. `COMPILER: str` -- _defaults -> `pdflatex`_, the compiler the program will use to compile the source, currently supports `xetex`, `luatex`, and `pdflatex`, although virtually allows for anything given that the compiler is on `PATH` and is installed and is functional.
20. `ENCODE: str` -- _defaults -> `UTF8`_, encoding of the document, although not necessary to be changed.
