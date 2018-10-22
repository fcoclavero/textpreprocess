__author__ = ["Francisco Clavero", "Vicente Oyanedel M."]
__email__ = ["fcoclavero32@gmail.com", "vicenteoyanedel@gmail.com"]
__status__ = "Prototype"


from nltk import word_tokenize
from nltk.corpus import stopwords


stop_words = set(stopwords.words('spanish'))


def remove_stopwords(sentence):
    """
    Transforms a given text to its lemmatized form. Assumes clean text separated by spaces.
    :param sentence: the text to be lemmatized
    :type: string
    :return: lemmatized text
    :type: string
    """
    return ' '.join([w for w in word_tokenize(sentence) if not w in stop_words])
