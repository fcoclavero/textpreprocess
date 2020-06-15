__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


from ..case_cleaner import clean_cases
from ..case_cleaner import split_camel_cased
from ..lemmatizer.es import lemmatize
from ..spaces_cleaner import clean_spaces
from ..spell_checker.es import fix_spelling
from ..stopword_remover.es import remove_stopwords
from ..symbol_cleaner.common import clean_newline
from ..symbol_cleaner.common import clean_repeated_symbols
from ..symbol_cleaner.es import clean_invalid_symbols
from .common import clean


def full_clean(text):
    """
    Cleans text with all available processes: lower casing, symbol cleaning, spaces cleaning, stop-word removal,
    spell checking and lemmatization.
    :param text: the text to be cleaned
    :type: str
    :return: the clean text
    :type: str
    """
    return clean(text, clean_newline, split_camel_cased, clean_cases, clean_invalid_symbols, clean_repeated_symbols, clean_spaces, fix_spelling, remove_stopwords, lemmatize)


def soft_clean(text):
    """
    Cleans text with the preprocessors that do not modify the syntax and semantics of the text: lower casing,
    spaces cleaning, symbol cleaning, and spell checking.
    :param text: the text to be cleaned
    :type: str
    :return: the clean text
    :type: str
    """
    return clean(text, clean_newline, split_camel_cased, clean_cases, clean_invalid_symbols, clean_repeated_symbols, clean_spaces, fix_spelling)
