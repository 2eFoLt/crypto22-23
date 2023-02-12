import alphabet

alpha = alphabet.get_alphabet()
array = [['а', 'б', 'в', 'г', 'д', 'е'],
         ['ж', 'з', 'и', 'й', 'к', 'л'],
         ['м', 'н', 'о', 'п', 'р', 'с'],
         ['т', 'у', 'ф', 'х', 'ц', 'ч'],
         ['ш', 'щ', 'ъ', 'ы', 'ь', 'э'],
         ['ю', 'я', '']]


def cypher(text):
    for i in text:
        for j in array:
            if j.__contains__(i):
                print(str(array.index(j) + 1) + str(j.index(i) + 1))


def decypher(string_array):
    for i in string_array:
        print(array[int(i[0]) - 1][int(i[1]) - 1])


cypher('мама')
decypher(['31', '11', '31', '11'])
