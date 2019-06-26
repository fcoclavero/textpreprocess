__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


from .common import SpellChecker
from ..settings import EN


class EnglishSpellCheckerSingleton(SpellChecker):
    """
    Utility class to manage a single SpellChecker instance for english.
    """
    __instance = None

    @staticmethod
    def getInstance():
        """
        Static access method for singleton pattern.
        :return: EnglishSpellCheckerSingleton
        """
        if EnglishSpellCheckerSingleton.__instance is None:
            EnglishSpellCheckerSingleton.__instance = EnglishSpellCheckerSingleton(
                allowed_punctuation_marks=EN['ALLOWED_PUNCTUATION_MARKS'],
                language=EN['PYSPELL_LANGUAGE']
            )
        return EnglishSpellCheckerSingleton.__instance



def fix_spelling(text):
    """
    Tries to correct the spelling of the given text.
    :param text: the text to spell-checked
    :type: string
    :return: spell-checked text
    :type: string
    """
    return EnglishSpellCheckerSingleton.getInstance().fix_text(text)