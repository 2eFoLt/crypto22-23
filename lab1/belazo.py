from math import ceil

table = []
for j in range(32):
    table.append([chr(1039 + i % 1071) if i > 1071 else chr(i) for i in range(1040 + j, 1072 + j)])


def cypher(text, word):
    word_line = word * ceil(len(text) / len(word))
    print(''.join([table[table[0].index(text[i])][table[0].index(word_line[i])] for i in range(len(text))]))


def decypher(text, word):
    word_line = word * ceil(len(text) / len(word))
    print(''.join([''.join([k[0] for k in table if k.index(text[i]) == table[0].index(word_line[i])])
                   for i in range(len(text))]))


cypher("самаясильнаяцепьслабеесвоегосамогослабогозвенатчк".upper(), "АПОКРИФ")
decypher("СПЪКПЩЬЛЛЫКПЮЩПЛЯХРЙЩЕАРШХЛВСПЪШУЦЕЛППШУЦЫВФЫКВЯЮ", "АПОКРИФ")
