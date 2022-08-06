# Config use

The program, as of writing, provides 12 parameters for the configuration of the LaTeX file to be generated, which can be modified via the config file (stored in `$HOME/.config/simtex/simtex.json`), or directly from the commandline options of the program.

## Parameters

1. `DOC_CLASS: str` -- _defaults -> article_, currently only supports article.
2. `DEF_FONT: str` -- _defaults -> Latin Modern Roman_ (provided by lmodern package), supports any font that has the package installed. Only package that is installed.
3. `FONT_SIZE: int` -- _defaults -> 12_, font size of the general text in article, sections, title, and other text is excluded.
4. `MARGIN: int` -- _defaults -> 1_, currenty only supports equal margin to all sides. **Unit: inches.**
5. `PAPER_SIZE: str` -- _defaults -> a4paper_, supports other paper sizes, such as letter, and legal, refer to documentation of LaTeX for further information.
6. `MAKE_TITLE: bool` -- _defaults -> true_, whether to create the title or not.
7. `PACKAGES: arr[str]` -- _defaults to the basic needs that maybe used by general population_, this ranges from math tools, to some preferential options such as footnote symbols, as well as other symbols that maybe used.
8. `SECTION_SIZES: dict[str, int]` -- _defaults -> 12_, sizes of the section.

    a. `main` == `\section`

    b. `sub` == `\subsection`

    c. `subsub` == `\subsubsection`
9. `AUTHOR: str` -- _defaults -> "John Doe"_.
10. `DATE: str` -- _defaults -> current time_ of conversion in format of (%B %d, %Y -- e.g. June, 27. 2055).
11. `COLOR_LINKS: bool` -- _default -> true_, whether to color the links,
12. `LINK_COLORS: str` -- _default -> BLUE_, color of links.
