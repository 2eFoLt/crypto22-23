from math import ceil


def get_multi(x, q):
    return ceil(x/q), q


def prepare(source_string):
    container_ = [source_string[k:k + j] for k in range(0, len(source_string), j)]
    for q in range(len(container_[0]) - len(container_[-1])):
        container_[-1] += ' '
    for k in range(1, len(container_), 2):
        container_[k] = container_[k][::-1]
    container_ = [''.join([container_[k][m] for k in range(i)]) for m in range(j)]
    return container_


def get_order(source_word):
    sorted_w = ''.join(sorted(source_word))
    order_ = [sorted_w.index(k) + 1 for k in source_word]
    inst_set = set()
    result_ = []
    for k in order_:
        if k not in inst_set:
            inst_set.add(k)
            result_.append(k)
        else:
            result_.append(k + 1)
    return result_


def sort_in_order(source_array, source_order):
    return [source_array[source_order.index(k)] for k in range(1, j + 1)]


def restore_from_order(source_array, source_order):
    return [source_array[k-1] for k in source_order]


def dewind(source_array):
    sw = 0
    result_ = ""
    for q in range(len(source_array[0])):
        if sw == 0:
            piece = ''.join([source_array[q_][q] for q_ in range(len(source_array))])
            sw += 1
        else:
            piece = ''.join(source_array[_q][q] for _q in reversed(range(len(source_array))))
            sw -= 1
        result_ += piece
    return result_


word = "аккерман"
source = "эта капуста зеленая зпт все равно что зеленая капустатчк".upper().replace(' ', '')
i, j = get_multi(len(source), len(word))
prepared_container = prepare(source)
order = get_order(word)
result = ''.join(sort_in_order(prepared_container, order)).replace(' ', '')
print(f"Cypher result: {result}")
container = [result[k:k + i] for k in range(0, len(result), i)]
container = restore_from_order(container, order)
print(f"Decypher result: {dewind(container)}")
