import alphabet

alpha = alphabet.get_alphabet()


def cypher(source):  # 0 - 32
    text = ''.join([alpha[31 - alpha.index(i)] for i in source])
    print(text)


def decypher(source):  # 0 - 32
    text = ''.join([alpha[31 - alpha.index(i)] for i in source])
    print(text)


cypher('абвг')
decypher('яюэь')
