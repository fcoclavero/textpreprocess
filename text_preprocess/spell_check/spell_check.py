from hunspell import Hunspell
import re

punctuation = ".,!?;"
hunspell_data_dir='/home/fcoclavero/Dropbox/Workspace/Python/Tesis/experiments/dictionaries/dictionaries/en-US/'

class SpellCheck:
    def __init__(self):
        self.refresh_dict()

    def suggest(self, word):
        return self.h.suggest(word)
        
    def correct_word(self, word):
        if word in punctuation:
            return word
        suggetions = self.h.suggest(word)
        if suggetions and not self.contains(word):
            return suggetions[0]
        return word
        
    def contains(self, word):
        return self.h.spell(word)

    def correct_text(self, text):
        result_str = []
        tokens = re.findall(r"[\w']+|[.,!?;]", text)
        list_of_words = [self.correct_word(word) for word in tokens]
        for wd in list_of_words:
            if wd not in punctuation:
                result_str.append(" ")
            result_str.append(wd)
        try:
            if result_str[0] is " ":
                return "".join(result_str[1:])
        except IndexError:
            pass
        return "".join(result_str)
        
    def add_word(self, word, refresh=True):
        if not self.contains(word):
            with open(hunspell_data_dir + 'index.dic', 'a') as fp:
                fp.write(word + "\n")
            if refresh:
                self.refresh_dict()

    def remove_word(self, word, refresh=True):
            with open(hunspell_data_dir + 'index.dic', 'r', encoding='utf8') as fp:
                lines = fp.readlines()
            with open(hunspell_data_dir + 'index.dic', 'w', encoding='utf8') as fp:
                for line in lines:
                    if line!=word+"\n":
                        fp.write(line)
            if refresh:
                self.refresh_dict()
    
    def refresh_dict(self):
        self.h = Hunspell('index', hunspell_data_dir=hunspell_data_dir)

   