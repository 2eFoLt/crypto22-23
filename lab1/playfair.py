import alphabet

alpha = alphabet.get_alphabet().upper()
word = "РЕСПУБЛИКА"
text = "ТЕКСТДЛЯШИФРОВАНИЯВГ"


def strip(target, source):
    for i in target:
        source = source.replace(i, '')
    source = source.replace('Й', '').replace('Ъ', '')
    return source


def split_by(target, size):
    if len(target) % size == 0:
        return [list(target[i:i + size]) for i in range(0, len(target), size)]
    else:
        return None


def find_line(ch1, source):
    for i in source:
        if i.__contains__(ch1):
            return i
    return None


def are_in_line(pair, source):
    target = find_line(pair[0], source)
    if target.__contains__(pair[1]):
        return True
    return False


def are_in_vline(pair, source):
    target1, target2 = find_line(pair[0], source), find_line(pair[1], source)
    if target1.index(pair[0]) == target2.index(pair[1]):
        return True
    return False


def inline_cypher(pair, source):
    target = find_line(pair[0], source)
    res_pair = []
    for i in pair:
        if target.index(i) + 1 > len(target) - 1:
            res_pair.append(target[0])
        else:
            res_pair.append(target[target.index(i) + 1])
    return res_pair


def inline_decypher(pair, source):
    target = find_line(pair[0], source)
    res_pair = []
    for i in pair:
        if target.index(i) - 1 < 0:
            res_pair.append(target[len(target) - 1])
        else:
            res_pair.append(target[target.index(i) - 1])
    return res_pair


def vline_cypher(pair, source):
    lines = [find_line(pair[0], source), find_line(pair[1], source)]
    ch_pos = lines[0].index(pair[0])
    res_pair = []
    for i in lines:
        if source.index(i) + 1 > len(source) - 1:
            res_pair.append(source[0][ch_pos])
        else:
            res_pair.append(source[source.index(i) + 1][ch_pos])
    return res_pair


def vline_decypher(pair, source):
    lines = [find_line(pair[0], source), find_line(pair[1], source)]
    ch_pos = lines[0].index(pair[0])
    res_pair = []
    for i in lines:
        if source.index(i) - 1 < 0:
            res_pair.append(source[4][ch_pos])
        else:
            res_pair.append(source[source.index(i) - 1][ch_pos])
    return res_pair


def box_cypher(pair, source):
    target1, target2 = find_line(pair[0], source), find_line(pair[1], source)
    ch1_pos, ch2_pos = target1.index(pair[0]), target2.index(pair[1])
    return [target1[ch2_pos], target2[ch1_pos]]


def make_table():
    source = word + strip(word, alpha)
    return [list(source[i:i + 6]) for i in range(0, len(source), 6)]


def cypher_text(target, source):
    result = []
    text_splitted = split_by(target, 2)
    if text_splitted is not None:
        print(text_splitted)
    for j in text_splitted:
        if are_in_line(j, source):
            result.append(inline_cypher(j, source))
        elif are_in_vline(j, source):
            result.append(vline_cypher(j, source))
        else:
            result.append(box_cypher(j, source))
    return ''.join([''.join(i) for i in result])


def decypher_text(target, source):
    result = []
    text_splitted = split_by(target, 2)
    if text_splitted is not None:
        print(text_splitted)
    for j in text_splitted:
        if are_in_line(j, source):
            result.append(inline_decypher(j, source))
        elif are_in_vline(j, source):
            result.append(vline_decypher(j, source))
        else:
            result.append(box_cypher(j, source))
    return ''.join([''.join(i) for i in result])


t_source = make_table()
for p in t_source:
    print(p)
cypher_result = cypher_text(text, t_source)
decypher_result = decypher_text(cypher_result, t_source)
print(f"Source text: {text}")
print(f"Cypher result: {cypher_result}")
print(f"Decypher result: {decypher_result}")
