__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


from .common import clean
from ..case_cleaner import clean_cases
from ..symbol_cleaner import clean_invalid_symbols, clean_repeated_symbols, clean_newline
from ..spaces_cleaner import clean_spaces
from ..stopword_remover.es import remove_stopwords
from ..lemmatizer.es import lemmatize
from ..spell_checker.es import fix_spelling


def full_clean(text):
    """
    Cleans text with all available processes: lower casing, symbol cleaning, spaces cleaning, stop-word removal,
    spell checking and lemmatization.
    :param text: the text to be cleaned
    :type: string
    :return: the clean text
    :type: string
    """
    return clean(text, clean_cases, clean_newline, clean_invalid_symbols, clean_repeated_symbols, clean_spaces, remove_stopwords, fix_spelling, lemmatize)


def soft_clean(text):
    """
    Cleans text with the preprocessors that do not modify the syntax and semantics of the text: lower casing,
    spaces cleaning, symbol cleaning, and spell checking.
    :param text: the text to be cleaned
    :type: string
    :return: the clean text
    :type: string
    """
    return clean(text, clean_newline, clean_spaces, clean_invalid_symbols, clean_repeated_symbols, clean_cases, fix_spelling)
