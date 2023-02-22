alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"


def get_decimal_alphabet(b):
    string_s = []
    for i in range(len(b)):
        string_s.append(alphabet.index(b[i]))
    return string_s


def get_alphabet():
    return alphabet


def get_pos(c):
    return alphabet.index(c) + 1


def get_char(n):
    return alphabet[n-1]
