from argparse import ArgumentParser



def cli() -> None:
    """Commandline interface for the program."""

    description: str = (
            "Generate a LaTeX file from your notes with few commands!"
        )
    parser: ArgumentParser = ArgumentParser(
            prog="simtex",
            usage="simtex [OPTIONS]",
            description=description
        )

    parser.add_argument(
        "-f", "--file",
        type=str,
        help="File to be converted into LaTeX.",
        action="store"
    )
    parser.add_argument(
        "-c", "--convert",
        type=bool,
        help="Convert the input to LaTeX.",
        action="store_true"
    )
    parser.add_argument(
        "-b", "--build",
        type=bool,
        help="Build the generated LaTeX file.",
        action="store_true"
    )
    parser.add_argument(
        "-B", "--build-nview",
        type=bool,
        help="Build the generated LaTeX file and view the output.",
        action="store_true"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Use different name for the output file.",
        action="store"
    )
    parser.add_argument(
        "-T", "--title",
        type=str,
        help="Set the title of the document.",
        action="store",
    )
    parser.add_argument(
        "-a", "--author",
        type=str,
        help="Set the author name of the document.",
        action="store"
    )
    parser.add_argument(
        "-d", "--date",
        type=str,
        help="Set the date of the document.",
        action="store"
    )
    parser.add_argument(
        "-F", "--font",
        type=str,
        help="Use different font package.",
        action="store"
    )
    parser.add_argument(
        "-s", "--font-size",
        type=int,
        help="Use different font size.",
        action="store"
    )
    parser.add_argument(
        "-p", "--paper-size",
        type=str,
        help="Use different paper size.",
        action="store"
    )

