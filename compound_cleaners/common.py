__author__ = ["Francisco Clavero"]
__description__ = "Common complex cleaners."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"


from functools import reduce
from typing import Callable


def clean(text: str, *cleaners: Callable[[str], str]) -> str:
    """Cleans the given text using the provided cleaning functions.

    Arguments:
        text:
            The text string to be cleaned.
        cleaners:
            The simple cleaner functions to be applied in sequence over the input text.

    Returns:
        The clean text.
    """
    return reduce(lambda part, func: func(part), cleaners, text)
