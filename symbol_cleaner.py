__author__ = ["Francisco Clavero", "Vicente Oyanedel M."]
__email__ = ["fcoclavero32@gmail.com", "vicenteoyanedel@gmail.com"]
__status__ = "Prototype"


import re, string


whitelist = string.ascii_letters + string.digits + ' ' # for spanish: + 'ñáéíóúüÑÁÉÍÓÚÜ'


def clean_symbols(text):
    """
    Filters text, leaving only valid characters, digits and spaces.
    :param text: the text to be filtered
    :type: string
    :return: the filtered text
    :type: string
    """
    return re.sub(r'[^%s]' % whitelist, '', text)
