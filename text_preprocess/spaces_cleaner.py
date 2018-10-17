def unify_spaces(text):
    """
    Deja solo espacios unitarios, quitando los espacios repetidos.
    :param text: Texto a unificar sus espacios.
    :return: Texto con solo espacios unicos.
    """
    while "  " in text:
        text = text.replace("  ", " ")
    return text


def clean_spaces(text):
    """
    Deja espacios unitarios y elimina espacios del comienzo y final.
    :param text: Texto a formatear sus espacios.
    :return: Texto sin espacios al comienzo y final, y con espacios unitarios.
    """
    text = unify_spaces(text)
    text = text.strip()  # remove spaces from beggining and end
    return text


if __name__ == '__main__':
    print(clean_spaces("  hola que  tal    como      estas         tu     ajaj ajjaja       ajaj                       aaaaaaaaaaaaa     "))
