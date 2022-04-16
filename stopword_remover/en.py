__author__ = ["Francisco Clavero"]
__description__ = "Stopword remover functions for the `en` language."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

from nltk.corpus import stopwords

from .common import remove_stopwords_set


def remove_stopwords(sentence: str) -> str:
    """Transforms a given text to its lemmatized form.

    Assumes clean text separated by spaces.

    Arguments:
        sentence:
            the text from which stopwords will be removed.

    Returns:
        The lemmatized text.
    """
    return remove_stopwords_set(sentence, set(stopwords.words('english')))
