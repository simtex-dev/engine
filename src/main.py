from src.cli import Cli


def main() -> None:
    """Main program that calls the argument parser."""

    cli_: Cli = Cli()
    cli_.cli()


if __name__ == "__main__":
    main()
