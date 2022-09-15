from autocorrect import Speller # type: ignore


def fix_spell(line: str, autocorrect_lang: str) -> str:
    """Fixes the spelling of the incorrect words in given line.

    Args:
        line -- line that will be analyzed and translated.
        autocorrect_lang -- language of autocorrect to use.

    Returns:
        The line with corrected spelling.
    """

    spell = Speller(lang=autocorrect_lang)

    return f"\n{spell(line)}\n"
