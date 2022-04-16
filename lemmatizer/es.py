__author__ = ["Francisco Clavero"]
__description__ = "Functions to lemmatize text for the `es` language."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

import json

from typing import Dict

from nltk import word_tokenize

from ..settings import ES


LEMMAS: Dict[str, str] = json.load(open(ES["LEMMAS_PATH"], "r", encoding="latin-1"))
"""Spanish lemmas dictionary."""


def lemma(word: str) -> str:
    """Transforms a given word to its lemmatized form, checking the lemma dictionary.

    If the word is not included in the dictionary, the same word is returned.

    Arguments:
        word:
            String containing a single word.

    Returns:
        The word's lemma.
    """
    return LEMMAS[word] if word in LEMMAS else word


def lemmatize(sentence: str) -> str:
    """Transforms a given text to its lemmatized form.

    Assumes clean text separated by spaces.

    Arguments:
        sentence:
            The text to be lemmatized.

    Returns:
        The lemmatized text.
    """
    return " ".join([lemma(word) for word in word_tokenize(sentence)])
