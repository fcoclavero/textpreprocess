from datetime import datetime


def test_english():
    from compound_cleaners.en import full_clean
    from compound_cleaners.en import soft_clean

    start = datetime.now()

    text = '   thiss is a bery :''{ñdirti text!  '

    text_full_clean = full_clean(text)
    text_soft_clean = soft_clean(text)

    assert text_full_clean == 'dirty text !'
    assert text_soft_clean == 'this is a very dirty text!'

    print('Processing complete in %s' % (datetime.now() - start))
    print('Original text: %s' % text)
    print('Full clean: %s' % text_full_clean)
    print('Soft clean: %s' % text_soft_clean)


def test_spanish():
    from compound_cleaners.es import full_clean
    from compound_cleaners.es import soft_clean

    start = datetime.now()

    text = '   AraucanÃ­a, la manera presora con la cual estan atacando al pueblo mapuche.el desempleo  '

    text_full_clean = full_clean(text)
    text_soft_clean = soft_clean(text)

    assert text_full_clean == 'araucano , manera presora estan atacar poblar mapuche.el desempleo'
    assert text_soft_clean == 'araucana, la manera presora con la cual estan atacando al pueblo mapuche.el desempleo'

    print('Processing complete in %s' % (datetime.now() - start))
    print('Original text: %s' % text)
    print('Full clean: %s' % text_full_clean)
    print('Soft clean: %s' % text_soft_clean)