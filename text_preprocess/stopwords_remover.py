import json

from text_preprocess.symbol_cleaner import symbol_cleaner
from text_preprocess.spaces_cleaner import clean_spaces
from text_preprocess.decapitalizer import case_cleaner
from pattern.es import parsetree

stopwords_file_name = "text_preprocess/stop_words/stopwords-es-aggregated.json"
def concat_stopwords():
    """
    Se llama una vez para generar un archivo unico de stopwords en JSON.
    :return: None
    """
    stopword_files = ["stopwords-iso.txt", "stopwords-json.txt", "stopwords-matcms.txt", "stopwords-ranks.txt", ]
    stopwords = set()

    # # first parse
    # filename = stopword_files[0]
    # aux_list = []
    # with open(filename, 'r') as fp:
    #     lines = fp.readlines()
    #     for line in lines:
    #         line = line.replace("\n", "")
    #         if line not in stopwords:
    #             aux_list.append(line)
    # stopwords.update(aux_list)

    # second parse
    filename = stopword_files[1]
    with open(filename, 'r') as fp:
        d = json.load(fp)
        stopwords.update(d)

    # third parse
    filename = stopword_files[2]
    aux_list = []
    with open(filename, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            line = line.replace("\n", "")
            if line not in stopwords:
                aux_list.append(line)
    stopwords.update(aux_list)

    # cuarto parse
    filename = stopword_files[3]
    aux_list = []
    with open(filename, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            line = line.replace("\n", "")
            if line not in stopwords:
                aux_list.append(line)
    stopwords.update(aux_list)

    with open(stopwords_file_name, 'w') as fp:
        a = json.dumps(list(stopwords), ensure_ascii=False)
        fp.write(a)
    print(stopwords)


def clean(text):
    """
    Elimina stopwords del texto.

    Asume que el texto está en español, en minusculas, separado por espacios unitarios, sin simbolos y en ascii.
    :param text:
    :return:
    """

    text = case_cleaner(
        symbol_cleaner(
            clean_spaces(
                    text)))
    with open(stopwords_file_name) as fp:
        raw_sws = json.load(fp)

    stopwords = []
    for stopword in raw_sws:
        stopwords.append(
                case_cleaner(
                    symbol_cleaner(
                        clean_spaces(
                                stopword))))
    out_str_list = []
    for word in text.split(" "):

        if word not in stopwords:
            out_str_list.append(word)
    return ' '.join(out_str_list)

def clean_by_pos(text):
    new_text = []
    text = parsetree(text)
    for sentence in text:
            for word_n_tag in sentence.word:
             
                word = word_n_tag.string
                tag = word_n_tag.part_of_speech
                #print(word + tag)
                word = symbol_cleaner(word)
                if 'NN' in tag or 'VB' in tag or 'RB' in tag or 'JJ' in tag:
                    new_text.append(word)
            new_text.append(".")
    return " ".join(new_text)

#concat_stopwords()
