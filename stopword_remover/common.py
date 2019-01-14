__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


from nltk import word_tokenize


def remove_stopwords_set(sentence, stop_words):
    """
    Transforms a given text to its lemmatized form. Assumes clean text separated by spaces.
    :param sentence: the text from which stopwords will be removed
    :type: string
    :param stop_words: a set with stop words for the same language as the sentence
    :type: string
    :return: lemmatized text
    :type: string
    """
    return ' '.join([w for w in word_tokenize(sentence) if not w in stop_words])
