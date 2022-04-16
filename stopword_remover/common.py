__author__ = ["Francisco Clavero"]
__description__ = "Common stopword remover functions."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

from typing import Collection

from nltk import word_tokenize


def remove_stopwords_set(sentence: str, stop_words: Collection[str]) -> str:
    """Transforms a given text to its lemmatized form.

    Assumes clean text separated by spaces.

    Arguments:
        sentence:
            The text from which stopwords will be removed.
        stop_words:
            A collection of stop words for the same language as the sentence.

    Returns:
        The lemmatized text.
    """
    return " ".join([w for w in word_tokenize(sentence) if w not in stop_words])
