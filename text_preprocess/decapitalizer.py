def decapitalizer(text):
    """
    Deja el texto en minusculas.
    :param text: Texto a dejar en minusculas.
    :return: Texto resultante en minusculas.
    """
    return text.lower()


if __name__ == '__main__':
    print(decapitalizer("HOLA QUE TALCA"))
    print(decapitalizer("HoLa QuE Te PAsa"))