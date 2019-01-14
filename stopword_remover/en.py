__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


from nltk.corpus import stopwords

from .common import remove_stopwords_set


def remove_stopwords(sentence):
    """
    Transforms a given text to its lemmatized form. Assumes clean text separated by spaces.
    :param sentence: the text from which stopwords will be removed
    :type: string
    :return: lemmatized text
    :type: string
    """
    return remove_stopwords_set(sentence, set(stopwords.words('english')))
