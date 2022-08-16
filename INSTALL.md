# Installation

Since the current version of simtex, is under alpha (v0.1.0a), there is no package and install script yet. Clone the repository:

```
git clone -b devel https://github.com/iaacornus/simtex
```

Install the dependencies, currently, the python dependency used is only `rich==12.4.4` which can be installed via `pip`. If you plan to use `-b` and `-B` command, you need a tex compiler, by default the program uses `PdfLaTeX`, which can be installed with `texlive` or other LaTeX distribution from your distro.

Then create the config directory: `mkdir $HOME/.config/simtex && cp ./simtex/examples/config/code_conf.txt ./simtex/examples/config/simtex.json -t $HOME/.config/simtex/`.

And place the source code in your `$PYTHONPATH`, since the command that is used is `python -m src.cli [COMMANDS] [OPTIONS]`, therefore, the source code must be in `$PYTHONPATH`. Then finally, you can add an alias to your `$HOME/.bashrc` or shell config file, with `simtex="python -m src.cli`.
