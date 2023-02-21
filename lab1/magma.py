import secrets
# key = secrets.token_hex(32)


class Table:
    body = [['c', '4', '6', '2', 'a', '5', 'b', '9', 'e', '8', 'd', '7', '0', '3', 'f', '1'],
            ['6', '8', '2', '3', '9', 'a', '5', 'c', '1', 'e', '4', '7', 'b', 'd', '0', 'f'],
            ['b', '3', '5', '8', '2', 'f', 'a', 'd', 'e', '1', '7', '4', 'c', '9', '6', '0'],
            ['c', '8', '2', '1', 'd', '4', 'f', '6', '7', '0', 'a', '5', '3', 'e', '9', 'b'],
            ['7', 'f', '5', 'a', '8', '1', '6', 'd', '0', '9', '3', 'e', 'b', '4', '2', 'c'],
            ['5', 'd', 'f', '6', '9', '2', 'c', 'a', 'b', '7', '8', '1', '4', '3', 'e', '0'],
            ['8', 'e', '2', '5', '6', '9', '1', 'c', 'f', '4', 'b', '0', 'd', 'a', '3', '7'],
            ['1', '7', 'e', 'd', '0', '5', '8', '3', '4', 'f', 'a', '6', '9', 'c', 'b', '2']
            ]

    def get(self, number, value):
        number = int(number)
        if not value.isdigit():
            value = int(value, 16)
        else:
            value = int(value)
        return self.body[number][value]


table = Table()
key = "da1c966ee627d35f37b9061230850695ff05cccc44eac1e1855c32a25902c356"
keys = ['0x' + key[i:i+8] for i in range(0, len(key), 8)]
print(keys)


def t(piece_0x):
    return ''.join([table.get(8 - 1 - i, piece_0x[i]) for i in range(8)])


def add32(vec_a, vec_b):
    res = []
    for i in range(0, vec_a.__sizeof__()//4, 4):
        prod1, prod2 = hex(vec_a)[2::][i:i+4], vec_b[2::][i:i+4]
        res.append(hex(int(prod1, 16) ^ int(prod2, 16))[2::])
    return ''.join(res)


def g(left_0x, right_0x):
    print("wtf")


g(0x87654321, 0xfedcba98)  # == 0xfdcbc20c
# def g(piece_0x):
