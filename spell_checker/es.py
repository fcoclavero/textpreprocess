__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


from .common import SpellChecker
from ..settings import ES


class SpanishSpellCheckerSingleton(SpellChecker):
    """
    Utility class to manage a single SpellChecker instance for spanish.
    """
    __instance = None

    @staticmethod
    def get_instance():
        """
        Static access method for singleton pattern.
        :return: SpanishSpellCheckerSingleton
        """
        if SpanishSpellCheckerSingleton.__instance is None:
            SpanishSpellCheckerSingleton.__instance = SpanishSpellCheckerSingleton(
                language=ES['PYSPELL_LANGUAGE'],
                allowed_punctuation_marks=ES['ALLOWED_PUNCTUATION_MARKS']
            )
        return SpanishSpellCheckerSingleton.__instance



def fix_spelling(text):
    """
    Tries to correct the spelling of the given text.
    :param text: the text to spell-checked
    :type: str
    :return: spell-checked text
    :type: str
    """
    return SpanishSpellCheckerSingleton.get_instance().fix_text(text)