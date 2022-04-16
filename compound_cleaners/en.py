__author__ = ["Francisco Clavero"]
__description__ = "Complex cleaners for the `en` language."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

from ..case_cleaner import clean_cases, split_camel_cased
from ..lemmatizer.en import lemmatize
from ..spaces_cleaner import clean_spaces
from ..spell_checker.en import fix_spelling
from ..stopword_remover.en import remove_stopwords
from ..symbol_cleaner.common import clean_newline, clean_repeated_symbols
from ..symbol_cleaner.en import clean_invalid_symbols, expand_contractions
from .common import clean


def full_clean(text: str) -> str:
    """Cleans text with all available processes.

    Current processing:
        - Lower casing
        - Symbol cleaning
        - Spaces cleaning
        - Stop-word removal
        - Spell checking
        - Lemmatization

    Arguments:
        text:
            The text to be cleaned

    Returns:
        The clean text.
    """
    return clean(
        text,
        clean_newline,
        split_camel_cased,
        clean_cases,
        expand_contractions,
        clean_invalid_symbols,
        clean_repeated_symbols,
        clean_spaces,
        fix_spelling,
        remove_stopwords,
        lemmatize,
    )


def soft_clean(text: str) -> str:
    """Cleans text with the preprocessors that do not modify the syntax and semantics
    of the text.

    Processing:
        - Lower casing
        - Spaces cleaning
        - Symbol cleaning
        - Spell checking

    Arguments:
        text:
            The text to be cleaned

    Returns:
        The clean text.
    """
    return clean(
        text,
        clean_newline,
        split_camel_cased,
        clean_cases,
        clean_invalid_symbols,
        clean_repeated_symbols,
        clean_spaces,
        fix_spelling,
    )
