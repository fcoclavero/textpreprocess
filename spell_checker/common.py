__author__ = ["Francisco Clavero"]
__description__ = "Spellchecker class to interface with `pyspellchecker`."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

import re

from typing import List

from nltk import word_tokenize
from spellchecker import SpellChecker as PySpellChecker


class SpellChecker:
    """Class for managing spell checking using `pyspellchecker`.

    Implemented as a class, as multiple `SpellChecker` instances might be used to
    maintain different dictionaries simultaneously.
    """

    def __init__(self, language: str, allowed_punctuation_marks: str) -> None:
        """Constructor method. Declares and creates a new `PySpellChecker` object.

        Arguments:
            language:
                The language for the `PySpellChecker` object.
            allowed_punctuation_marks:
                String with the allowed punctuation marks.
        """
        self.language = language
        self.allowed_punctuation_marks = allowed_punctuation_marks
        self.spell = None
        self.refresh_dict()

    def refresh_dict(self) -> None:
        """Create a new `SpellChecker` object from the specified dictionary file."""
        self.spell = PySpellChecker(language=self.language, distance=1)

    def is_punctuation_mark(self, word: str) -> bool:
        """Checks if the given word corresponds to one of the allowed punctuation marks.

        Arguments:
            word:
                A string with a single word.

        Returns:
            Boolean indicating if the given word is an allowed punctuation mark.
        """
        return bool(re.match(r"[%s]" % self.allowed_punctuation_marks, word))

    def is_correctly_spelled(self, word: str) -> bool:
        """Checks if the given word is correctly spelled.

        Arguments:
            word:
                A string with a single word.

        Returns:
            A boolean indicating if the spelling of the word is correct.
        """
        return bool(
            self.spell.known([word])
        )  # if word correctly spelled, known will be a list containing `word`

    def suggest(self, word: str) -> List[str]:
        """Suggest similar and correctly spelled alternatives for the given string.

        Arguments:
            word:
                A string with a single word.

        Returns:
            A list of correctly spelled suggestions.
        """
        return self.spell.candidates(word)

    def fix(self, word: str) -> str:
        """Fixes the spelling of the given word.

        Arguments:
            word:
                A string with a single word.

        Returns:
            The same input string if it is a punctuation mark, otherwise the top
            `pyspellchecker` suggestion.
        """
        return word if self.is_punctuation_mark(word) else self.spell.correction(word)

    def fix_text(self, text: str) -> str:
        """Fixes the spelling of a multi-worded phrase.

        Arguments:
            text:
                The phrase string.

        Returns:
            The same phrase, with the spelling of each word fixed.
        """
        fixed_text = " ".join([self.fix(word) for word in word_tokenize(text)])
        return re.sub(
            r" ([%s])" % self.allowed_punctuation_marks, r"\1", fixed_text
        )  # remove spaces preceding punctuation
