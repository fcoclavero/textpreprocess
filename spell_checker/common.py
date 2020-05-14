__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


import re

from nltk import word_tokenize

from spellchecker import SpellChecker as PySpellChecker


class SpellChecker:
    """
    Class for managing spell checking using pyspellchecker. Implemented as a class, as multiple SpellChecker instances
    might be used to maintain different dictionaries simultaneously.
    """

    def __init__(self, language, allowed_punctuation_marks):
        """
        Constructor method. Declares and creates a new Hunspell object.
        """
        self.language = language
        self.allowed_punctuation_marks = allowed_punctuation_marks
        self.spell = None
        self.refresh_dict()


    def refresh_dict(self):
        """
        Create a new SpellChecker object from the specified dictionary file.
        """
        self.spell = PySpellChecker(language=self.language, distance=1)


    def is_punctuation_mark(self, word):
        """
        Checks if the given word corresponds to one of the allowed punctuation marks.
        :param word: a string with a single word
        :type: str
        :return: boolean indicating if the given word is an allowed punctuation mark
        :type: bool
        """
        return bool(re.match(r'[%s]' % self.allowed_punctuation_marks, word))


    def is_correctly_spelled(self, word):
        """
        Checks if the given word is correctly spelled.
        :param word: a string with a single word
        :type: str
        :return: boolean indicating if the spelling of the word is correct
        :type: bool
        """
        return len(self.spell.spell.known([word])) # if word correctly spelled, known will be a list containing `word`


    def suggest(self, word):
        """
        Suggest similar and correctly spelled alternatives for the given string.
        :param word: a string with a single word
        :type: str
        :return: a list of suggestions
        :type: List[str]
        """
        return self.spell.candidates(word)


    def fix(self, word):
        """
        Fixes the spelling of the given word.
        :param word: a string with a single word
        :type: str
        :return: the same string if it is a punctuation mark, otherwise the top pyspellchecker suggestion.
        """
        return word if self.is_punctuation_mark(word) else self.spell.correction(word)


    def fix_text(self, text):
        """
        Fixes the spelling of a multi-worded phrase.
        :param text: the phrase string
        :type: str
        :return: the same phrase, with the spelling of each word fixed.
        """
        fixed_text = ' '.join([self.fix(word) for word in word_tokenize(text)])
        return re.sub(r' ([%s])' % self.allowed_punctuation_marks, r'\1', fixed_text) # remove spaces preceding punctuation
