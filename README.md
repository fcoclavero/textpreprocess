# text-preprocess

Python package for natural language pre-processing with nltk and Hunspell.

Includes:

1. Standarizing cases
2. Standarizing symbols
3. Removing extra whitespaces
4. Stopword removal
5. Simple spelling corrections
6. Lemmatization

Avalable utilities:

* `clean_cases`
* `clean_symbols`
* `clean_spaces`
* `remove_stopwords`
* `fix_spelling`
* `SpellChecker`
* `lemmatize`
* `clean`
* `soft_clean`
* `full_clean`

Supported languages:

1. Spanish
2. English

## Submodules

Spell checking functions rely on dictionary files, placed by default on the `dictionaries` directory. [This collection](https://github.com/wooorm/dictionaries) of dictionaries was added as a git submodule for convenience.

Lemmatization in Spanish relies on lemma dictionary files, placed by default on the `lemmas` directory. [This collection](https://github.com/fcoclavero/lemmas) was added as a git submodule for convenience. Feel free to propose your own!

To clone all submodules, use the following commands.

```bash
git submodule init
git submodule update
```

Further reference can be found [here](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

## Sample usage

```python
from text_preprocess import full_clean, soft_clean

text = '   thiss is a bery :''{ñdirti text!  '

full_clean(text) # -> 'this very dirt text'

soft_clean(text) # -> 'this is a very dirty text'
```

Special thanks to [Vicente Oyanedel M.](https://github.com/vichoko) for work on the first version of this package.
