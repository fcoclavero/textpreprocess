__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


import re


def clean_spaces(text):
    """
    Removes any consecutive white spaces in the text, as well as preceding and trailing whitespaces.
    :param text: the text to be filtered
    :type: str
    :return: the filtered text
    :type: str
    """
    return re.sub(' +', ' ', text).strip() # strip removes characters from beginning and end, with whitespace as default
