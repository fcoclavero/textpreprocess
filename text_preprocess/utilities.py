from functools import reduce

from .lemmatization.lemmatizer import transform
from .stop_words.stopwords_remover import clean as swclean, clean_by_pos
from .symbol_cleaner import alphanumeric_filter
from .spaces_cleaner import clean_spaces
from .decapitalizer import decapitalizer
from .dirt_cleaner import remove_n_dot
from .spell_check.spell_check import SpellCheck


class Preprocess:
    def __init__(self):
        self.h = SpellCheck()

    @staticmethod
    def __limpiar(texto, *correctores):
        return reduce(lambda part, func: func(part), correctores, texto)

    @staticmethod
    def full_clean(text):
        """
        @DeprecationWarning
        Aplica todos los preprocesadores.
        """
        return Preprocess.__limpiar(text, remove_n_dot, clean_spaces, alphanumeric_filter, decapitalizer, Preprocess().fix_spelling, swclean, transform)

    @staticmethod
    def full_clean_pos(text):
        """
        @DeprecationWarning
        Aplica todos los preprocesadores, se filtra por POS-tagging en vez de StopWords.
        """
        return Preprocess.__limpiar(text, remove_n_dot, clean_spaces, alphanumeric_filter, decapitalizer,
                                    Preprocess().fix_spelling, clean_by_pos, transform)

    @staticmethod
    def soft_clean(text):
        """
        Aplica los procesadores que no modifican la sintaxis y semantica del texto.
        """
        return Preprocess.__limpiar(text, remove_n_dot, clean_spaces, alphanumeric_filter, decapitalizer,
                                    Preprocess().fix_spelling)

    def lemmatize(self, text):
        """
        Lematiza el texto.
        """
        return transform(text)

    def stopword_filter(self, text, default=True):
        """
        Filtra las stopwords del texto.
        """
        return swclean(text) if default else clean_by_pos(text)

    def fix_spelling(self, text):
        """
        Intenta arreglar la ortografía del texto.
        """

        return self.h.correct_text(text)