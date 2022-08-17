# simtex

![](https://api.codiga.io/project/34276/score/svg) ![](https://github.com/iaacornus/simtex/actions/workflows/pytest.yaml/badge.svg)

simtex (simplified LaTeX) allows you to convert your markdown or text lectures into LaTeX file with one command, configured with simple `.json` file.

> Note: This program does not exist to replace the LaTeX system, this do exist to simplify the process of turning your already existing markdown/text file into PDF with LaTeX.

# Program Options

```
usage: simtex [OPTIONS]

Generate a LaTeX file from your notes with few commands!

options:
  -h, --help            show this help message and exit
  -c, --convert         Convert the input to LaTeX.
  -b, --build           Build the generated LaTeX file.
  -B, --buildnview      Build the generated LaTeX file and view the output.
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
  -F FONT, --font FONT  Use different font package.
  -s FONTSIZE, --fontsize FONTSIZE
                        Use different font size.
  -p PAPERSIZE, --papersize PAPERSIZE
                        Use different paper size.
  -I INDENT, --indent INDENT
                        Indent size to be used.
  -m MARGIN, --margin MARGIN
                        Margin size to be used.
```

# Examples

You can view the output of the program [here](./examples/1/hello.pdf) using the command:

![](./imgs/sample.png)

```
simtex -c -i="./examples/1/hello.md" -T="Hello Simtex!" -of="./examples/1" -f="hello.tex" -a="iaacornus" -d="August 15, 2552"
```

To convert a LaTeX file, and rename the default author defined in `$CONF_PATH/simtex.json`, add `-a="iaacornus (or your name)`, and with the date, `-d="August 15, 2552`. See the [documentation of arguments and configuration file](./examples/config/README.md).

# Installation

See [INSTALL.md](INSTALL.md) for details.
