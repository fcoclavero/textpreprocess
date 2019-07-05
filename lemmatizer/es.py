__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


import json

from nltk import word_tokenize

from settings import ES


# Load spanish lemmas dictionary
lemmas = json.load(open(ES['LEMMAS_PATH'], 'r', encoding='latin-1'))


def lemma(word):
    """
    Transforms a given word to its lemmatized form, checking a lemma dictionary. If the word is
    not included in the dictionary, the same word is returned.
    :param word: string containing a single word
    :type: string
    :return: the word's lemma
    :type: string
    """
    return lemmas[word] if word in lemmas else word


def lemmatize(sentence):
    """
    Transforms a given text to its lemmatized form. Assumes clean text separated by spaces.
    :param sentence: the text to be lemmatized
    :type: string
    :return: lemmatized text
    :type: string
    """
    return ' '.join([lemma(word) for word in word_tokenize(sentence)])
