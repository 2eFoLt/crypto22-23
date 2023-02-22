import alphabet
import numpy as np
from math import ceil


def convert(matrix):
    res = [i.getT().getA() for i in matrix]
    digitized = [list(i[0]) for i in res]
    output = []
    for i in digitized:
        output.append([round(j) for j in i])
    return output


def encode(text, key, size):
    d_text_matrix = []
    d_text = [alphabet.get_pos(i) for i in text]
    text_size = len(d_text)
    for i in range(0, text_size, size):
        d_text_matrix.append([d_text[i+j] for j in range(size)])
    return [list(np.dot(key, i)) for i in d_text_matrix]


def decode(encrypted_matrix, key):
    inverted_matrix = np.asmatrix(key).getI()
    result = convert([np.dot(inverted_matrix, np.asmatrix(i).getT()) for i in encrypted_matrix])
    return result


text1 = "забава"
res1 = encode(text1, [[1, 4, 8], [3, 7, 2], [6, 9, 5]], 3)
res2 = decode(res1, [[1, 4, 8], [3, 7, 2], [6, 9, 5]])
converted = ""
for k in res2:
    converted += ''.join([alphabet.get_char(j) for j in k])
print(f"Encode result: {res1}\nDecode result: {res2}\nConversion of decode result: {converted}")



