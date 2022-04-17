__author__ = ["Francisco Clavero"]
__description__ = "Text cleaner functions that check correct spelling for `es`."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

from ..settings import ES
from .common import SpellChecker


class SpanishSpellCheckerSingleton(SpellChecker):
    """Utility class to manage a single `SpellChecker` instance for spanish."""

    __instance: "SpanishSpellCheckerSingleton" = None
    """The singleton instance."""

    @staticmethod
    def get_instance() -> "SpanishSpellCheckerSingleton":
        """Static access method for singleton pattern."""
        if SpanishSpellCheckerSingleton.__instance is None:
            SpanishSpellCheckerSingleton.__instance = SpanishSpellCheckerSingleton(
                language=ES["PYSPELL_LANGUAGE"],
                allowed_punctuation_marks=ES["ALLOWED_PUNCTUATION_MARKS"],
            )
        return SpanishSpellCheckerSingleton.__instance


def fix_spelling(text: str) -> str:
    """Tries to correct the spelling of the given text.

    Arguments:
        text:
            The text to be spell-checked.

    Returns:
        The spell-checked text.
    """
    return SpanishSpellCheckerSingleton.get_instance().fix_text(text)
