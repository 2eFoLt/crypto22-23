body = [['c', '4', '6', '2', 'a', '5', 'b', '9', 'e', '8', 'd', '7', '0', '3', 'f', '1'],
        ['6', '8', '2', '3', '9', 'a', '5', 'c', '1', 'e', '4', '7', 'b', 'd', '0', 'f'],
        ['b', '3', '5', '8', '2', 'f', 'a', 'd', 'e', '1', '7', '4', 'c', '9', '6', '0'],
        ['c', '8', '2', '1', 'd', '4', 'f', '6', '7', '0', 'a', '5', '3', 'e', '9', 'b'],
        ['7', 'f', '5', 'a', '8', '1', '6', 'd', '0', '9', '3', 'e', 'b', '4', '2', 'c'],
        ['5', 'd', 'f', '6', '9', '2', 'c', 'a', 'b', '7', '8', '1', '4', '3', 'e', '0'],
        ['8', 'e', '2', '5', '6', '9', '1', 'c', 'f', '4', 'b', '0', 'd', 'a', '3', '7'],
        ['1', '7', 'e', 'd', '0', '5', '8', '3', '4', 'f', 'a', '6', '9', 'c', 'b', '2']
        ]

key = "da1c966ee627d35f37b9061230850695ff05cccc44eac1e1855c32a25902c356"
mask32 = 2 ** 32 - 1  # 11111...111 x32


def keys(int256):
    int256 = to_int(int256)
    container = []
    for i in reversed(range(8)):
        container.append((int256 >> (32 * i)) & mask32)
    container += container * 2 + list(reversed(container))
    return container


def to_int(x):
    if isinstance(x, int):
        return x
    return int(x, 16)


def t(int32):
    y = 0
    for i in reversed(range(8)):
        j = (int32 >> 4 * i) & 0xf
        y <<= 4
        y ^= int(body[i][j], 16)
    return y


def shift11(int32):
    return ((int32 << 11) ^ (int32 >> (32 - 11))) & mask32


def g(i32, k32):  # Фейстель?
    i32, k32 = to_int(i32), to_int(k32)
    return shift11(t(i32 + k32) % 2 ** 32)


def split_by_32(int64):
    int64 = to_int(int64)
    left = int64 >> 32
    right = int64 & mask32
    return left, right


def join_32(left, right):
    left = to_int(left)
    right = to_int(right)
    return (left << 32) ^ right


def magma_encrypt(plaintext, source_key):
    container = keys(source_key)
    (left, right) = split_by_32(plaintext)
    for i in range(31):
        (left, right) = (right, left ^ g(right, container[i]))
    return join_32(left ^ g(right, hex(container[-1])), right)


print(hex(magma_encrypt("fedcba9876543210", "ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff")))
