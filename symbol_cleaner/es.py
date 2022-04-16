__author__ = ["Francisco Clavero"]
__description__ = "Text cleaner functions that remove symbols for the `es` language."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

import re
import string


WHITELIST = string.ascii_letters + "ñáéíóúüÑÁÉÍÓÚÜ" + " ,.!¡?¿"
"""Symbols that won't be filtered."""


def clean_invalid_symbols(text: str) -> str:
    """Filters text, leaving only valid characters, digits and spaces.

    Arguments:
        text:
            The text to be filtered.

    Returns:
        The filtered text.
    """
    return re.sub(r"[^%s]" % WHITELIST, "", text)
