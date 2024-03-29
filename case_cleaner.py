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


def camel_to_snake_case(camel_cased_string: str) -> str:
    """Convert the format of the given string from CamelCase to snake_case.

    Arguments:
        camel_cased_string:
            The string in CamelCase format.

    Returns:
        The same string, but in snake_case format.

    """
    return re.sub(r"(?<!^)(?=[A-Z])", "_", camel_cased_string).lower()


def kebab_to_snake_case(text: str) -> str:
    """Convert a kebab-cased-text to snake_case.

    Arguments:
        text:
            The text to be converted to snake case. Must be valid kebab case.

    Returns:
        The text in kebab case form.
    """
    return text.replace("-", "_")


def split_camel_cased(text: str) -> str:
    """Split camelCased elements with a space.

    Arguments:
        text:
            The text to be processed.

    Returns:
        The text with all camelCased elements split into different elements.
    """
    return re.sub("(?!^)([A-Z][a-z]+)", r" \1", text)
