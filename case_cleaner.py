__author__ = ["Francisco Clavero"]
__description__ = "Text cleaner functions that deal with casing."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

import re


def clean_cases(text: str) -> str:
    """Makes text all lowercase.

    Arguments:
        text:
            The text to be converted to all lowercase.

    Returns:
        The lowercase text.
    """
    return text.lower()


def split_camel_cased(text: str) -> str:
    """Split camelCased elements with a space.

    Arguments:
        text:
            The text to be converted processed.

    Returns:
        The text with all camelCased elements split into different elements.
    """
    return re.sub("(?!^)([A-Z][a-z]+)", r" \1", text)
