table = []
for j in range(32):
    table.append([chr(1039 + i % 1071) if i > 1071 else chr(i) for i in range(1040+j, 1072+j)])


def cypher(text):
    print(''.join([table[table[0].index(text[i])][i % 32] for i in range(len(text))]))


def decypher(text):
    print(''.join([table[0][table[i % 32].index(text[i])] for i in range(len(text))]))


cypher("самаясильнаяцепьслабеесвоегосамогослабогозвенатчк".upper())
decypher("СБОГГЦОТДЦККВТЭЛБЬТФЩЪЗЩЖЮЭЙНЭКНГПУОДЖФКЦРМРЩНАЖЪ")
