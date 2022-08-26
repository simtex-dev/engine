# simtex

![](https://api.codiga.io/project/34276/score/svg)
![](https://github.com/iaacornus/simtex/actions/workflows/pytest.yaml/badge.svg)

simtex (simplified LaTeX) allows you to convert your markdown or text lectures
into LaTeX file with one command, configured with simple `.json` file.

> Note: This program does not exist to replace the LaTeX system, this do exist
to simplify the process of turning your already existing markdown/text file
into PDF with LaTeX.

# Program Options

```
usage: simtex [OPTIONS]

Convert your mardown or text lectures into LaTeX/pdf with one command.!

options:
  -h, --help            show this help message and exit
  -c, --convert         Convert the input to LaTeX.
  -b, --build           Build the generated LaTeX file.
  -B, --buildnview      Build the generated LaTeX file and view the output.
  -F FONT, --font FONT  Use different font package.
  -s FONTSIZE, --fontsize FONTSIZE
                        Use different font size.
  -p PAPERSIZE, --papersize PAPERSIZE
                        Use different paper size.
  -I INDENT, --indent INDENT
                        Indent size to be used.
  -m MARGIN, --margin MARGIN
                        Margin size to be used.
  -e ENCODING, --encoding ENCODING
                        Use a different encoding for document.
  -i INPUT, --input INPUT
                        File to be converted into LaTeX.
  -T TITLE, --title TITLE
                        Set the title of the document.
  -f FILENAME, --filename FILENAME
                        Use different name for the output file.
  -of OUTPUTFOLDER, --outputfolder OUTPUTFOLDER
                        Change the output folder for the output file.
  -a AUTHOR, --author AUTHOR
                        Set the author name of the document.
  -d DATE, --date DATE  Set the date of the document.
  -C COMPILER, --compiler COMPILER
                        Use a different LaTeX compiler.
  -ft, --filenametitle  Use the filename as title.
  -v, --verbose         Hide stdout of other processes.
```

# Features

The program allows the user to convert simple file such as markdown or text
file of its assignment/lecture into PDF using LaTeX. This program does not
intend to compete with pandoc, which essential does the same, but on a higher
level, however, produces a very complex transcription of the input, another
reason why this program is created, to create a simple LaTeX transcript of the
input. Currently, the program has features that can satisfy conversion of basic
inputs:

1. Supports the most basic commands, such as **bold**, _italics_,
**_emphasize_**, `inline code`, quotes, as well as hyperlinks.
2. Environments, the program supports a multiline math environment using
`align`, single line math equation using `equation` environment, as well as
code blocks using `lstlisting` with syntax highlighting.
3. Figures.
4. Sections, subsections upto subparagraphs.
5. Basic document metadata and properties that can be provided in a
configuration file for default value, this includes, author, date, font, among
others, view the [short documentation](./examples/config/README.md) for full
list.
6. Simple [config file](./examples/config/simtex.json) using JSON, which
defines the rules that should be followed on how the program should parse the
input, as well as how to format the document.

Refer to the [PDF](./examples/1/hello.pdf) for more details.

# Examples

You can view the output of the program [here](./examples/1/hello.pdf) which was
generated using the command:

```
simtex -c -i="./examples/1/hello.md" -T="Hello Simtex!" -of="./examples/1" -f="hello.tex" -a="iaacornus" -d="August 15, 2552"
```

> View [`./examples/1/hello.md`](./examples/1/example.md)

> View output: [.examples/1/hello.pdf](./examples/1/hello.pdf)

To convert a LaTeX file, and rename the default author defined in
`$CONF_PATH/simtex.json`, add `-a="iaacornus (or your name)`, and with the
date, `-d="August 15, 2552`.
See the [documentation of arguments and configuration file](./examples/config/README.md).

# Installation

See [INSTALL.md](INSTALL.md) for details.

# Contribution

1. All contributions are enforced to abide by the [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md)
2. Opening and reporting issues is regarded as value contribution in this project and is welcomed.
3. In regards to coding contribution, refer to [CONTRIBUTING](CONTRIBUTING.md)

# Roadmap

1. Support for enumerate/lists.
2. Support Windows
3. Add templates
