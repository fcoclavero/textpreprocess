__author__ = ["Francisco Clavero"]
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


import re
import string


whitelist = string.ascii_letters + 'ñáéíóúüÑÁÉÍÓÚÜ' + ' ,.!¡?¿'


def clean_invalid_symbols(text):
    """
    Filters text, leaving only valid characters, digits and spaces.
    :param text: the text to be filtered
    :type: str
    :return: the filtered text
    :type: str
    """
    return re.sub(r'[^%s]' % whitelist, '', text)
