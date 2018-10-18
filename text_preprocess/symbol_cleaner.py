import re, string


whitelist = string.ascii_letters + string.digits + ' ' # for spanish: + 'ñáéíóúüÑÁÉÍÓÚÜ'


def symbol_cleaner(text):
    """
    Filters text, leaving only valid characters, digits and spaces.
    :param text: the text to be filtered
    :type: string
    :return: the filtered text
    :type: string
    """
    return re.sub(r'[^%s]' % whitelist, '', text)
