__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


import re


def clean_repeated_symbols(text):
    """
    Filters text, replacing symbols repeated more than twice (not allowed
    in most languages) with a single repetition of the symbol.
    :param text: the text to be filtered
    :type: string
    :return: the filtered text
    :type: string
    """
    pattern = re.compile(r"(.)\1{2,}", re.DOTALL)
    return pattern.sub(r"\1\1", text)


def clean_newline(text):
    """
    Filter newlines.
    :param text: the text to be filtered
    :type: string
    :return: the filtered text
    :type: string
    """
    return re.sub('\n', '', text)


def clean_ndot(text):
    """
    Filter for special symbol in a specific dataset.
    :param text: the text to be filtered
    :type: string
    :return: the filtered text
    :type: string
    """
    return re.sub(' N[.]', '', text)
