__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


import re


def clean_cases(text):
    """
    Makes text all lowercase.
    :param text: the text to be converted to all lowercase.
    :type: str
    :return: lowercase text
    :type: str
    """
    return text.lower()


def split_camel_cased(text):
    """
    Split camelCased elements with a space.
    :param text: the text to be converted processed.
    :type: str
    :return: text with all camelCased elements split into different elements
    :type: str
    """
    return re.sub('(?!^)([A-Z][a-z]+)', r' \1', text)
