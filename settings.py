__author__ = ["Francisco Clavero"]
__description__ = "Settings and constants for text cleaners."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

import os

from typing import Dict


EN: Dict[str, str] = {"ALLOWED_PUNCTUATION_MARKS": ".,!?;", "PYSPELL_LANGUAGE": "en"}
"""Settings for the `en` language."""

ES: Dict[str, str] = {
    "ALLOWED_PUNCTUATION_MARKS": ".,!?;",
    "PYSPELL_LANGUAGE": "es",
    "LEMMAS_PATH": os.path.join(os.path.dirname(__file__), "lemmas", "es.json"),
}
"""Settings for the `es` language."""
