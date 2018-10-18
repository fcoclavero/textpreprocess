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

Sample usage:

```python
from text_preprocess import full_clean, soft_clean

text = '   tis a bery :''{ñdirti text!  '

full_clean(text) # -> 'this very dirt text'

soft_clean(text) # -> 'this is a very dirty text'
```

Special thanks to [Vicente Oyanedel M.](https://github.com/vichoko) for work on the original Spanish version of this package.
