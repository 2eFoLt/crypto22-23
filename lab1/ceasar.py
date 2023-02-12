import alphabet

alpha = alphabet.get_alphabet()


def encrypt(text, i_shift):
    result1 = ''.join([alpha[(alpha.index(i) + i_shift) % len(alpha)] for i in text])
    print(result1)


def decrypt(text, i_shift):
    result1 = ''.join([alpha[(alpha.index(i) - i_shift) % len(alpha)] for i in text])
    print(result1)


# text_object = open('текст.txt', 'r')
# line = text_object.readline()
# print(line)
encrypt('яэяэ'.replace('ё', 'е'), 1)
decrypt('аюаю', 1)
