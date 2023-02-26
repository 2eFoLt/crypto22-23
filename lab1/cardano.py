def log(iterable):
    for k in iterable:
        print(k)
    print('\n')


def vertical_swap(source):
    return [i for i in reversed(source)]


def horizontal_swap(source):
    for j in range(len(source)):
        source[j] = list(reversed(source[j]))
    return source


def add_line(source, line):
    source_text = list(line)
    result_ = []
    for item in source:
        result_.append([source_text.pop(0) if j == 1 else j or 0 for j in item])
    log(result_)
    return result_


def update(source, mask_):
    result_ = []
    for item in range(len(source)):
        result_.append([source[item][subitem] or mask_[item][subitem] for subitem in range(len(source[0]))])
    return result_


mask = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
        ]
spaces = 11
test = list("helloo")
text = "шифр решетка является частным случаем шифра маршрутной перестановки".upper().replace(' ', '')

print(text[:15:])
result = add_line(mask, text)
mask = vertical_swap(mask)
result = update(result, [*mask])
text = text[15::]

print(text[:15:])
result = add_line(result, text)
mask = horizontal_swap([*mask])
result = update(result, [*mask])
text = text[15::]

print(text[:15:])
result = add_line(result, text)
mask = vertical_swap(mask)
result = update(result, [*mask])
text = text[15::]

print(text[:15:])
result = add_line(result, text)
