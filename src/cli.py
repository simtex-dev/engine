from argparse import ArgumentParser
from subprocess import CalledProcessError, Popen
from typing import Any, Callable

from src.utils.config_fetch import ConfParse
from src.utils.logger import Logger
from src.misc.stdout import Signs
from src.convert import convert
from src.utils.config import Config, Rules
from src.mutils.functions import build_file


class Cli:
    """Commandline interface of the program."""

    def __init__(self) -> None:
        self.log: Logger = Logger()
        conf_parse: ConfParse = ConfParse(self.log)
        self.config: Config = conf_parse.conf()
        self.rules: Rules = conf_parse.rules()

        description: str = (
                "Convert your mardown or text lectures"
                " into LaTeX/pdf with one command.!"
            )
        self.parser: ArgumentParser = ArgumentParser(
                prog="simtex",
                usage="simtex [OPTIONS]",
                description=description
            )

    def create_parser(self) -> None:
        """Create the parser."""

        self.parser.add_argument( # commands
            "-c", "--convert",
            help="Convert the input to LaTeX.",
            action="store_true"
        )
        self.parser.add_argument(
            "-b", "--build",
            help="Build the generated LaTeX file.",
            action="store_true"
        )
        self.parser.add_argument(
            "-B", "--buildnview",
            help="Build the generated LaTeX file and view the output.",
            action="store_true"
        ) # starts here are the options
        self.parser.add_argument(
            "-i", "--input",
            help="File to be converted into LaTeX.",
            action="store"
        )
        self.parser.add_argument(
            "-T", "--title",
            help="Set the title of the document.",
            action="store",
        )
        self.parser.add_argument(
            "-f", "--filename",
            help="Use different name for the output file.",
            action="store"
        )
        self.parser.add_argument(
            "-of", "--outputfolder",
            help="Change the output folder for the output file.",
            action="store"
        )
        self.parser.add_argument(
            "-a", "--author",
            help="Set the author name of the document.",
            action="store"
        )
        self.parser.add_argument(
            "-d", "--date",
            help="Set the date of the document.",
            action="store"
        )
        self.parser.add_argument(
            "-F", "--font",
            help="Use different font package.",
            action="store"
        )
        self.parser.add_argument(
            "-s", "--fontsize",
            help="Use different font size.",
            action="store"
        )
        self.parser.add_argument(
            "-p", "--papersize",
            help="Use different paper size.",
            action="store"
        )
        self.parser.add_argument(
            "-I", "--indent",
            help="Indent size to be used.",
            action="store"
        )
        self.parser.add_argument(
            "-m", "--margin",
            help="Margin size to be used.",
            action="store"
        )

        self.args = self.parser.parse_args()

    def update_conf(self) -> None:
        """Update the overrides of the program."""

        PARAMETERS: dict[str, Any] = {
            "filename": self.args.filename,
            "output_folder": self.args.outputfolder,
            "author": self.args.author,
            "date": self.args.date,
            "doc_font": self.args.font,
            "font_size": self.args.fontsize,
            "paper_size": self.args.papersize,
            "margin": self.args.margin,
            "indent_size": self.args.indent,
            "doc_font": self.args.font
        }

        key_: str; param: Any
        for key_, param in PARAMETERS.items(): # for overrides
            if param is not None:
                self.log.logger(
                    "E", f"{self.config.__getattribute__(key_)} -> {param}"
                )
                self.config.__setattr__(key_, param)

    def cli(self) -> None:
        """Commandline interface of the program."""

        self.create_parser() # create the arguments
        self.update_conf() # update the config for overrides

        converter: Callable[..., None] = lambda: convert(
                self.log,
                self.rules,
                self.config,
                self.args.title,
                self.args.filename
            )

        try:
            if self.args.convert:
                converter()
            elif self.args.build:
                converter()
                build_file(
                    self.log,
                    self.config.output_folder,
                    self.config.filename
                )
            elif self.args.buildnview:
                converter()
                build_file(
                    self.log,
                    self.config.output_folder,
                    self.config.filename
                )
                Popen(["xgd-open", self.args.filename])
            else:
                print(f"{Signs.FAIL} Unknown option.")
        except KeyboardInterrupt:
            self.log.logger("E", "Process aborted, aborting ...")
        except CalledProcessError:
            self.log.logger("E", "Cannot call the process, aborting ...")


if __name__ == "__main__":
    cli: Cli = Cli()
    cli.cli()
