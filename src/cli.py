from argparse import ArgumentParser
from subprocess import CalledProcessError, Popen
from typing import Any, Callable

from src.config import Config, Rules
from src.utils.config_fetch import ConfParse
from src.convert import convert
from src.mutils.functions import build_file
from src.mutils.functions import update_conf
from src.utils.logger import Logger
from src.misc.stdout import Signs


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
            action="store",
            required=True
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

    def cli(self) -> None:
        """Commandline interface of the program."""

        self.create_parser() # create the arguments
        # update the config for overrides
        update_conf(self.log, self.config, self.args)

        converter: Callable[..., Any] = lambda: convert(
                self.log,
                self.rules,
                self.config,
                self.args.title,
                self.args.input
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
                try:
                    Popen(["xgd-open", self.args.filename])
                except FileNotFoundError:
                    self.log.logger(
                        "e", "No PDF view found, cannot view file."
                    )
            else:
                print(f"{Signs.FAIL} Unknown option.")
        except KeyboardInterrupt:
            self.log.logger("E", "Process aborted, aborting ...")
        except CalledProcessError:
            self.log.logger("E", "Cannot call the process, aborting ...")
