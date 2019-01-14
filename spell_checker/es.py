__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


import re

from .common import SpellChecker
from ..settings import ES


class SpanishSpellCheckerSingleton(SpellChecker):
    """
    Utility class to manage a single SpellChecker instance for spanish.
    """
    __instance = None

    @staticmethod
    def getInstance():
        """
        Static access method for singleton pattern.
        :return: SpanishSpellCheckerSingleton
        """
        if SpanishSpellCheckerSingleton.__instance is None:
            SpanishSpellCheckerSingleton.__instance = SpanishSpellCheckerSingleton(
                allowed_punctuation_marks=ES.ALLOWED_PUNCTUATION_MARKS, 
                dictionary_directory=ES.DICTIONARY_DIRECTORY
            )
        return SpanishSpellCheckerSingleton.__instance



def fix_spelling(text):
    """
    Tries to correct the spelling of the given text.
    :param text: the text to spell-checked
    :type: string
    :return: spell-checked text
    :type: string
    """
    return SpanishSpellCheckerSingleton.getInstance().fix_text(text)