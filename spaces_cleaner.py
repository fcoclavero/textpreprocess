__author__ = ["Francisco Clavero", "Vicente Oyanedel M."]
__email__ = ["fcoclavero32@gmail.com", "vicenteoyanedel@gmail.com"]
__status__ = "Prototype"


import re


def clean_spaces(text):
    """
    Removes any consecutive white spaces in the text, as well as preceding and trailing whitespaces.
    :param text: the text to be filtered
    :type: string
    :return: the filtered text
    :type: string
    """
    return re.sub(' +', ' ', text).strip() # strip removes characters from beginning and end, with whitespace as default
