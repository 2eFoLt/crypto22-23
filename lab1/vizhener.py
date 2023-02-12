table = []
for j in range(32):
    table.append([chr(1039 + i % 1071) if i > 1071 else chr(i) for i in range(1040+j, 1072+j)])


def get_pos(l1):
    return table[0].index(l1)


def find_intersection(l1, l2):
    return table[get_pos(l2)][get_pos(l1)]


def find_source(l1, prod):
    return ''.join([i[0] for i in table if i.index(prod) == table[0].index(l1)])


def letter_cypher(text, letter):
    word_line = letter + text
    print(''.join([find_intersection(word_line[i], text[i]) for i in range(len(text))]))


def letter_decypher(text, letter):
    result = []
    for i in range(len(text)):
        letter = ''.join(find_source(letter, text[i]))
        result.append(letter)
    print(''.join(result))


def text_cypher(text, letter):
    result = []
    for i in range(len(text)):
        letter = find_intersection(letter, text[i])
        result.append(letter)
    print(''.join(result))


def text_decypher(text, letter):
    result = []
    for i in range(len(text)):
        result.append(find_source(letter, text[i]))
        letter = text[i]
    print(''.join(result))


letter_cypher("самаясильнаяцепьслабеесвоегосамогослабогозвенатчк".upper(), "э".upper())
letter_decypher("ОСММЯРЩУЗЙНЯХЫФЛНЬЛБЖКЦУРУИСЯСМЪССЯЬЛБПССХЙЗТНТЙБ", "э".upper())
text_cypher("самаясильнаяцепьслабеесвоегосамогослабогозвенатчк".upper(), "э".upper())
text_decypher("ООЪЪЩКТЭЩЖЖЕЫАПЛЬЗЗИНТГЕУШЫЙЪЪЖФЧЕЦББВРУБИКПЬЬОЕП", "э".upper())
