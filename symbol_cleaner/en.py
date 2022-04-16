__author__ = ["Francisco Clavero"]
__description__ = "Text cleaner functions that remove symbols for the `en` language."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

import re
import string

from functools import reduce
from typing import List, Tuple


WHITELIST: str = string.ascii_letters + " ,.!?"
"""Symbols that won't be filtered."""

CONTRACTIONS: List[Tuple[str, str]] = [
    # specific
    (r"won\'t", "will not"),
    (r"can\'t", "can not"),
    # general
    (r"n\'t", " not"),
    (r"\'re", " are"),
    (r"\'s", " is"),
    (r"\'d", " would"),
    (r"\'ll", " will"),
    (r"\'t", " not"),
    (r"\'ve", " have"),
    (r"\'m", " am"),
]
"""List of tuples containing the allowed contractions and their expansion."""


def clean_invalid_symbols(text: str) -> str:
    """Filters text, leaving only valid characters, digits and spaces.

    Arguments:

    Arguments:
        text:
            The text to be filtered.

    Returns:
        The filtered text.
    """
    return re.sub(r"[^%s]" % WHITELIST, "", text)


def expand_contractions(text: str) -> str:
    """Filters text, expanding all contractions defined in the 'CONTRACTIONS' variable.

    Arguments:
        text:
            The text to be filtered.

    Returns:
        The filtered text.
    """
    return reduce(
        lambda partial_text, contraction: re.sub(
            contraction[0], contraction[1], partial_text
        ),
        CONTRACTIONS,
        text,
    )
