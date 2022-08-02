from argparse import ArgumentParser



def cli() -> None:
    """commandline interface for the program."""

    description: str = (
            "Generate a LaTeX file from your notes with few commands!"
        )
    parser: object = ArgumentParser(
            prog="simtex",
            usage="simtex [OPTIONS]",
            description=description
        )

    parser.add_argument(
        "-m", "--mardown",
        help="Convert your markdown files to LaTeX.",
        action="store_true"
    )
    parser.add_argument(
        "-t", "--text",
        help="Convert your text files to LaTeX.",
        action="store_true"
    )
    parser.add_argument(
        "-b", "--build",
        help="Build the generated LaTeX file.",
        action="store_true"
    )
    parser.add_argument(
        "-B", "--build-nview",
        help="Build the generated LaTeX file and view the output.",
        action="store_true"
    )
    parser.add_argument(
        "-o", "--output",
        help="Use different name for the output file.",
        action="store"
    )
    parser.add_argument(
        "-T", "--title",
        help="Set the title of the document.",
        action="store",
    )
    parser.add_argument(
        "-a", "--author",
        help="Set the author name of the document.",
        action="store"
    )
    parser.add_argument(
        "-d", "--date",
        help="Set the date of the document.",
        action="store"
    )
    parser.add_argument(
        "-f", "--font",
        help="Use different font package.",
        action="store"
    )
    parser.add_argument(
        "-s", "--font-size",
        help="Use different font size.",
        action="store"
    )
    parser.add_argument(
        "-p", "--paper-size",
        help="Use different paper size.",
        action="store"
    )

