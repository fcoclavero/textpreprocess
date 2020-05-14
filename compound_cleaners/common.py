from functools import reduce


def clean(text, *cleaners):
    """
    Cleans the given text using the provided cleaning functions.
    :param text: the text to be cleaned
    :type: str
    :return: the clean text
    :type: str
    """
    return reduce(lambda part, func: func(part), cleaners, text)