__author__ = ["Francisco Clavero"]
__description__ = "Text cleaner functions that deal with spacing."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

import re


def clean_spaces(text: str) -> str:
    """Removes any consecutive white spaces in the text, as well as preceding and
    trailing whitespaces.

    Arguments:
        text:
            The text to be filtered.

    Returns:
        The filtered text.
    """
    return re.sub(
        " +", " ", text
    ).strip()  # `strip` removes characters from start & end, with whitespace as default
