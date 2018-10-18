__author__ = ["Francisco Clavero", "Vicente Oyanedel M."]
__email__ = ["fcoclavero32@gmail.com", "vicenteoyanedel@gmail.com"]
__status__ = "Prototype"


from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer


# Equivalences between the first character of an nltk part-of-speech tag and wordnet POS tag.
nltk_wordnet_pos_dict = {
    'J': wordnet.ADJ,
    'N': wordnet.NOUN,
    'V': wordnet.VERB,
    'R': wordnet.ADV
}


def wordnet_pos(tag):
    """
    Transforms nltk part-of-speech tag strings to wordnet part-of-speech tag string.
    :param tag: nltk part-of-speech tag string
    :type: string
    :return: the corresponding wordnet tag
    :type: wordnet part-of-speech tag string
    """
    return getattr(nltk_wordnet_pos_dict, tag[0], nltk_wordnet_pos_dict['N']) # 'N' is the wordnet default


def lemmatize(sentence):
    """
    Transforms a given text to its lemmatized form. Assumes clean text separated by spaces.
    :param sentence: the text to be lemmatized
    :type: string
    :return: lemmatized text
    :type: string
    """
    return ' '.join([WordNetLemmatizer().lemmatize(word, wordnet_pos(tag)) for word, tag in pos_tag(word_tokenize(sentence))])
