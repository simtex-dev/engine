# `simtex`

![](https://api.codiga.io/project/34276/score/svg)
![](https://github.com/iaacornus/simtex/actions/workflows/pytest.yaml/badge.svg)

`simtex` (simplified LaTeX) allows you to convert your mardown or files
 into PDF using LaTeX with one command, configured with simple `.json` file.

> `simtex` is a program that works based on rules of the user that is
defined in `simtex.json`, which the program uses to the files and converts
it in LaTeX based on the rules defined by the user.

`simtex` also allows for interop between markdown and LaTeX, especially in cases
where markdown is not enough to format the document, that part could be written
in LaTeX while the others would be converted by `simtex`!

> Note: This program does not intend to replace the LaTeX system, but to
simplify the process of turning your already existing markdown/text file
into PDF with LaTeX.

> Note: The program currently only supports basic markdown syntax and
features, and not HTML tags.

# Program Options

```
❯ simtex --help
usage: simtex [OPTIONS] [INPUT] FILE [ARGUMENTS]

Convert your markdown or text files into LaTeX/pdf with one command! Interop
with LaTeX and markdown is also allowed by simtex!

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
                        Use a different encoding for the document.
  -tc, --twocolumns     Use two columns in the document.
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
  -v, --verbose         Show the stdout of processes.
  -y, --assumeyes       Assume yes to every prompt.
  -A, --autocorrect     Apply autocorrection in wrong spellings.
  -R, --replace         Automatically replace math symbols defined.
  --version             Print the version number of the application.
```

# Convertion features

The program allows the user to convert simple file such as markdown or text
file into PDF using LaTeX. This program does not intend to compete with pandoc,
which essentially does the same but on higher level. Currently, the program
has features that can satisfy conversion of basic inputs:

1. Supports the most basic commands, such as **bold**, _italics_,
**_emphasize_**, `inline code`, quotes, as well as [hyperlinks](hyperlinks).
2. Environments, the program supports a multiline math environment using
`align`, single line math equation using `equation` environment, as well as
code blocks using `lstlisting` with syntax highlighting.
3. Figures with captions.
4. Sections, subsections upto subparagraphs.
5. Basic document metadata and properties that can be provided in a
configuration file for default value, this includes, author, date, font, among
others, view the [short documentation](./examples/config/README.md) for full
list.
6. Simple [config file](./examples/config/simtex.json) using JSON, which
defines the rules that should be followed on how the program should parse the
input, as well as how to format the document.

Refer to the [PDF](./examples/1/out/hello.pdf) for more details.

# Examples

You can view the output of the program [here](./examples/1/out/hello.pdf) which was
generated using the command:

```
simtex -c -i="./examples/1/hello.md" -T="Hello Simtex!" -f="hello.tex" -a="iaacornus" -d="August 15, 2552"
```

> View [`./examples/1/hello.md`](./examples/1/example.md)

> View output: [.examples/1/hello.pdf](./examples/1/out/hello.pdf)

To convert a LaTeX file, and rename the default author defined in
`$CONF_PATH/simtex.json`, add `-a="iaacornus (or your name)`, and with the
date, `-d="August 15, 2552` to provide other date instead of the present. The
program will output the `tex` file, as well as `pdf`, if `-b` was used, in `./out`
inside the folder of the input if there is no output folder given. See the
[documentation of arguments and configuration file](./examples/config/README.md).

# Program features

1. Convert a whole directory of files into LaTeX. `simtex` allows conversion of
bunch of files in all at once.
2. 'simtex' supports different compilers.
3. Interoperation between LaTeX and raw files. `simtex` is a program
that works based on the rules defined by user in `simtex.json`, which it uses
to convert the document given by the user.
4. Autocorrect (**beta**) of spelling mistakes in the document.
5. Automatic replacement (**beta**) of unicode characters and ASCII symbols that represent mathematical symbol or anything that is defined by user to their respective LaTeX command or the defined command by the user.

# Installation

Starting `v0.3.2-beta`, there is a released frozen code which can be easily downloaded
and executed directly with `./simtex [OPTIONS]`:

```
./simtex --help
```

> All of the dependency needed is packaged with in this build.

Another method to install the project is with `pip`. Since the package is
published on [PyPI](https://pypi.org/project/simtex/) since v0.2.0-alpha:

```
pip install --user simtex
```

Other options, specifically `-b` and `-B` requires `pdflatex` and any default 
pdf viewer for the latter. The LaTeX compiler can be provided by any of TeX
distributions that can be installed, but `texlive` with its full package is 
recommended since it is tested. `texlive` is available in most distribution
and can be installed with its package manager:

```
# fedora
sudo dnf install texlive-scheme-full

# arch linux
sudo pacman -S texlive-most

# debian
sudo apt install texlive
```

For other installation method, see [INSTALL.md](INSTALL.md) for details.

# Contribution

Refer to [CONTRIBUTING](CONTRIBUTING.md).

1. All contributions are required to abide by the [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md)
2. Opening and reporting issues is welcomed and considered as valuable contribution in this project.

# Roadmap

The first prioritized features (not sorted) are listed below:

- [ ] Support for enumerate/lists.
- [ ] Support Windows
- [ ] Add templates
- [ ] Include GUI
- [ ] Improve table support
