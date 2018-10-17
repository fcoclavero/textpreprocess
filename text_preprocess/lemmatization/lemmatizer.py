from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer


def wordnet_pos(tag):
    """
    Transforms nltk part-of-speech tag strings to wordnet part-of-speech tag string.
    :param tag: nltk part-of-speech tag string
    :type: string
    :return: the corresponding wordnet tag
    :type: wordnet part-of-speech tag string
    """
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


def transform(sentence):
    """
    Transforms a given text to its lemmatized form. Assumes clean text separated by spaces.
    :param sentence: the text to be lemmatized
    :type: string
    :return: lemmatized text
    :type: string
    """
    return ' '.join([WordNetLemmatizer().lemmatize(word, wordnet_pos(tag)) for word, tag in pos_tag(word_tokenize(sentence))])
