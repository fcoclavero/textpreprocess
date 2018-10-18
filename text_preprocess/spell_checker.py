__author__ = ["Francisco Clavero", "Vicente Oyanedel"]
__email__ = ["fcoclavero32@gmail.com", "vicenteoyanedel@gmail.com"]
__status__ = "Prototype"


import re

from hunspell import Hunspell
from nltk import word_tokenize


allowed_punctuation_marks = '.,!?;'
hunspell_data_dir = '/home/fcoclavero/Dropbox/Workspace/Python/Tesis/experiments/text_preprocess/dictionaries/dictionaries/en-US/'


class SpellChecker:
    """
    Class for managing spell checking using Hunspell. Implemented as a class, as multiple instances of a SpellChecker
    might be used to maintain different dictionaries simultaneously (for example adding custom words).
    """

    def __init__(self):
        """
        Constructor method. Declares and creates a new Hunspell object.
        """
        self.hunspell = None
        self.refresh_dict()


    def refresh_dict(self):
        """
        Create a new Hunspell object from the specified dictionary file.
        """
        self.hunspell = Hunspell('index', hunspell_data_dir=hunspell_data_dir)


    @staticmethod
    def is_punctuation_mark(word):
        """
        Checks if the given word corresponds to one of the allowed punctuation marks.
        :param word: a string with a single word
        :type: string
        :return: boolean indicating if the given word is an allowed punctuation mark
        :type: boolean
        """
        return bool(re.match(r'[%s]' % allowed_punctuation_marks, word))


    def is_correctly_spelled(self, word):
        """
        Checks if the given word is correctly spelled.
        :param word: a string with a single word
        :type: string
        :return: boolean indicating if the spelling of the word is correct
        :type: boolean
        """
        return self.hunspell.spell(word)


    def suggest(self, word):
        """
        Suggest similar and correctly spelled alternatives for the given string.
        :param word: a string with a single word
        :type: string
        :return: a list of suggestions
        :type: list<string>
        """
        return self.hunspell.suggest(word)


    def fix(self, word):
        """
        Fixes the spelling of the given word.
        :param word: a string with a single word
        :type: string
        :return: the same word if correctly spelled or a punctuation mark, otherwise the top Hunspell suggestion.
        """
        return word if self.is_punctuation_mark(word) or self.is_correctly_spelled(word) else self.suggest(word)[0]


    def fix_text(self, text):
        """
        Fixes the spelling of a multi-worded phrase.
        :param text: the phrase string
        :type: string
        :return: the same phrase, with the spelling of each word fixed.
        """
        fixed_text = ' '.join([self.fix(word) for word in word_tokenize(text)])
        return re.sub(r' ([%s])' % allowed_punctuation_marks, r'\1', fixed_text) # remove spaces preceding punctuation


checker = SpellChecker()


def fix_spelling(text):
    """
    Tries to correct the spelling of the given text.
    :param text: the text to spell-checked
    :type: string
    :return: spell-checked text
    :type: string
    """
    return checker.fix_text(text)