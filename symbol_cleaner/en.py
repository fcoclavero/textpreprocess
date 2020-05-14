__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


import re, string

from functools import reduce


whitelist = string.ascii_letters + ' ,.!?'

contractions = [
    # specific
    (r"won\'t", "will not"),
    (r"can\'t", "can not"),
    # general
    (r"n\'t", " not"),
    (r"\'re", " are"),
    (r"\'s", " is"),
    (r"\'d", " would"),
    (r"\'ll", " will"),
    (r"\'t", " not"),
    (r"\'ve", " have"),
    (r"\'m", " am")
]


def clean_invalid_symbols(text):
    """
    Filters text, leaving only valid characters, digits and spaces.
    :param text: the text to be filtered
    :type: str
    :return: the filtered text
    :type: str
    """
    return re.sub(r'[^%s]' % whitelist, '', text)


def expand_contractions(text):
    """
    Filters text, expanding all contractions defined in the 'contractions' variable.
    :param text: the text to be filtered
    :type: str
    :return: the filtered text
    :type: str
    """
    return reduce(
        lambda partial_text, contraction: re.sub(contraction[0], contraction[1], partial_text),
        contractions,
        text
    )
