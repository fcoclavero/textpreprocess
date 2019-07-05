import os


EN = {
    'ALLOWED_PUNCTUATION_MARKS': '.,!?;',
    'PYSPELL_LANGUAGE': 'en'
}
ES = {
    'ALLOWED_PUNCTUATION_MARKS': '.,!?;',
    'PYSPELL_LANGUAGE': 'es',
    'LEMMAS_PATH': os.path.join(os.path.dirname(__file__), 'lemmas', 'es.json')
}