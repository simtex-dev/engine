# Config use

The program, as of writing, provides 12 parameters for the configuration of the LaTeX file to be generated, which can be modified via the config file (stored in `$HOME/.config/simtex/simtex.json), or directly from the commandline options of the program.

## Parameters

1. "DOC_CLASS": defaults -> article, currently only supports article. Only accepts str and option that is supported by LaTeX.
2. "DEF_FONT": defaults -> Latin Modern Roman (provided my lmodern package), supports any font that has the package installed. Only accepts str with the name of package that is installed.
3. "FONT_SIZE": defaults -> 12, font size of the general text in article, sections, title, and other text is excluded. Only accepts int, not units.
4. "MARGIN": defaults -> 1 inches, currenty only supports equal margin to all sides. Only accepts str with unit "in", and no spaces.
5. "PAPER_SIZE": defaults -> a4paper, supports other paper sizes, such as letter, and legal, refer to documentation of LaTeX for further information. Only accepts str.
6. "MAKE_TITLE": defaults -> true, whether to create the title or not. Only accepts bool.
7. "PACKAGES": defaults to the basic needs that maybe used by general population, this ranges from math tools, to some preferential options such as footnote symbols, as well as other symbols that maybe used. Only accepts array with items of str only.
8. "SECTION_SIZES": defaults -> 12, sizes of the section. Only accepts dictionary with key as string, and value as integer.
9. "AUTHOR". Only accepts str.
10. "DATE": defaults -> current time of conversion in format of (%B %d, %Y -- e.g. June, 27. 2055). Only accepts str.
11. COLOR_LINKS: default -> true, whether to color the links, Only accepts bool.
12. "LINK_COLORS": default -> blue, color of links. Only accepts str.
