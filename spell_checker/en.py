__author__ = ["Francisco Clavero"]
__description__ = "Text cleaner functions that check correct spelling for `en`."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

from ..settings import EN
from .common import SpellChecker


class EnglishSpellCheckerSingleton(SpellChecker):
    """Utility class to manage a single `SpellChecker` instance for english."""

    __instance: "EnglishSpellCheckerSingleton" = None
    """The singleton instance."""

    @staticmethod
    def get_instance() -> "EnglishSpellCheckerSingleton":
        """Static access method for singleton pattern."""
        if EnglishSpellCheckerSingleton.__instance is None:
            EnglishSpellCheckerSingleton.__instance = EnglishSpellCheckerSingleton(
                language=EN["PYSPELL_LANGUAGE"],
                allowed_punctuation_marks=EN["ALLOWED_PUNCTUATION_MARKS"],
            )
        return EnglishSpellCheckerSingleton.__instance


def fix_spelling(text: str) -> str:
    """Tries to correct the spelling of the given text.

    Arguments:
        text:
            The text to be spell-checked.

    Returns:
        The spell-checked text.
    """
    return EnglishSpellCheckerSingleton.get_instance().fix_text(text)
