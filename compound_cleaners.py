__author__ = ["Francisco Clavero", "Vicente Oyanedel M."]
__email__ = ["fcoclavero32@gmail.com", "vicenteoyanedel@gmail.com"]
__status__ = "Prototype"


from functools import reduce

from text_preprocess.case_cleaner import clean_cases
from text_preprocess.symbol_cleaner import clean_symbols, clean_ndot
from text_preprocess.spaces_cleaner import clean_spaces
from text_preprocess.stopwords_remover import remove_stopwords
from text_preprocess.lemmatizer import lemmatize
from text_preprocess.spell_checker import fix_spelling


def clean(text, *cleaners):
    """
    Cleans the given text using the provided cleaning functions.
    :param text: the text to be cleaned
    :type: string
    :return: the clean text
    :type: string
    """
    return reduce(lambda part, func: func(part), cleaners, text)


def full_clean(text):
    """
    Cleans text with all available processes: lower casing, symbol cleaning, spaces cleaning, stop-word removal,
    spell checking and lemmatization.
    :param text: the text to be cleaned
    :type: string
    :return: the clean text
    :type: string
    """
    return clean(text, clean_ndot, clean_cases, clean_symbols, clean_spaces, remove_stopwords, fix_spelling, lemmatize, clean_spaces)


def soft_clean(text):
    """
    Cleans text with the preprocessors that do not modify the syntax and semantics of the text: lower casing,
    spaces cleaning, symbol cleaning, and spell checking.
    :param text: the text to be cleaned
    :type: string
    :return: the clean text
    :type: string
    """
    return clean(text, clean_ndot, clean_spaces, clean_symbols, clean_cases, fix_spelling, clean_spaces)
