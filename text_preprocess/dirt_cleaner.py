def remove_n_dot(text):
    if text[-3:].lower == " n.":
        return text[:-3]
    else:
        if " n." in text.lower():
            return text.replace(" n.", "").replace(" N.", "")
        else:
            return text
    