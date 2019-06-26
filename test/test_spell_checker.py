from compound_cleaners.en import full_clean as full_clean_en
from compound_cleaners.en import soft_clean as soft_clean_en


def test_spell_checker_en():
    text = '   thiss is a bery :''{ñdirti text!  '

    assert full_clean_en(text) == 'this very dirt text'
    assert soft_clean_en(text)  == 'this is a very dirty text'