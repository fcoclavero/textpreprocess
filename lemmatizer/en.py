__author__ = ["Francisco Clavero"]
__description__ = "Functions to lemmatize text for the `en` language."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

from typing import Dict

from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer


NLTK_WORDNET_POS: Dict[str, str] = {
    "J": wordnet.ADJ,
    "N": wordnet.NOUN,
    "V": wordnet.VERB,
    "R": wordnet.ADV,
}
"""Equivalences between the first character of an `nltk` part-of-speech tag and
`wordnet` POS tags.
"""


def wordnet_pos(tag: str) -> str:
    """Transform a `nltk` part-of-speech tag string to a `wordnet` part-of-speech tag
    string.

    Arguments:
        tag:
            An `nltk` part-of-speech tag string.

    Returns:
        The corresponding `wordnet` part-of-speech tag string.
    """
    return getattr(
        NLTK_WORDNET_POS, tag[0], NLTK_WORDNET_POS["N"]
    )  # 'N' is the wordnet default


def lemmatize(sentence: str) -> str:
    """Transforms a given text to its lemmatized form.

    Assumes clean text separated by spaces.

    Arguments:
        sentence:
            The text to be lemmatized.

    Returns:
        The lemmatized text.
    """
    return " ".join(
        [
            WordNetLemmatizer().lemmatize(word, wordnet_pos(tag))
            for word, tag in pos_tag(word_tokenize(sentence))
        ]
    )
