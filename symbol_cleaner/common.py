__author__ = ["Francisco Clavero"]
__description__ = "Common text cleaner functions that remove symbols."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

import re


def clean_repeated_symbols(text: str) -> str:
    """Filter text, replacing symbols repeated more than twice (not allowed in most
    languages) with a single repetition of the symbol.

    Arguments:
        text:
            The text to be filtered.

    Returns:
        The filtered text.
    """
    pattern = re.compile(r"(.)\1{2,}", re.DOTALL)
    return pattern.sub(r"\1\1", text)


def clean_newline(text: str) -> str:
    """Filter newlines.

    Arguments:
        text:
            The text to be filtered.

    Returns:
        The filtered text.
    """
    return re.sub("\n", "", text)


def clean_ndot(text: str) -> str:
    """Filter for special symbol in a specific dataset.

    Arguments:
        text:
            The text to be filtered.

    Returns:
        The filtered text.
    """
    return re.sub(" N[.]", "", text)
