import string

def alphanumeric_filter(text):
    """
    Filtra el texto dejando solo letras en español, digitos y espacios.
    :param text:
    :return:
    """
    whitelist = string.ascii_letters + string.digits + ' ' # for spanish: + ' ñáéíóúüÑÁÉÍÓÚÜ'
    ret = ''.join(c for c in text if c in whitelist)
    return ret


if __name__ == '__main__':
    print(alphanumeric_filter(" si te gustan la canciones de amor? Shalala__ te, gustan esos raros. # h%ola/\peiñados `n``uévos!!"))

