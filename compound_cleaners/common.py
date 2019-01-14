from functools import reduce


def clean(text, *cleaners):
    """
    Cleans the given text using the provided cleaning functions.
    :param text: the text to be cleaned
    :type: string
    :return: the clean text
    :type: string
    """
    return reduce(lambda part, func: func(part), cleaners, text)