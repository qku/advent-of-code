def read_file(file):
    with open(file) as f:
        _n = [int(_i) for _i in f.readlines()]
    return _n


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        raise AssertionError


def mix(_ids, _numbers):
    _length = len(_numbers)
    for _id in range(_length):
        # print([_numbers[i] for i in _ids])
        i = _ids.index(_id)
        _ids.pop(i)

        _n = _numbers[_id]
        if abs(_n) >= _length:
            moves = abs(_n) % _length + abs(_n) // _length
            moves *= sign(_n)
        else:
            moves = _n

        new_index = i + moves
        if new_index >= (_length - 1):
            new_index = new_index % (_length - 1)
        elif abs(new_index) >= (_length - 1):
            new_index = - (abs(new_index) % (_length - 1))
        _ids.insert(new_index, _id)
    return _ids


def get_coordinates(_numbers):
    _length = len(_numbers)
    zero_index = _numbers.index(0)
    _numbers = _numbers[zero_index:] + _numbers[:zero_index]
    coordinates = []
    for i in [1000, 2000, 3000]:
        i = i % _length
        n = _numbers[i]
        print(n)
        coordinates.append(n)
    return sum(coordinates)


if __name__ == '__main__':
    numbers = read_file('input.txt')
    length = len(numbers)

    # part I
    ids = list(range(length))
    ids = mix(ids, numbers)
    numbers_mixed = [numbers[i] for i in ids]
    print(numbers_mixed)
    coordinate_sum = get_coordinates(numbers_mixed)
    print(f'Sum of coordinates: {coordinate_sum}')

    # part II
    decryption_key = 811589153
    numbers = [i * decryption_key for i in numbers]
    ids = list(range(length))
    for _ in range(10):
        print(_)
        print(ids)
        numbers_mixed = [numbers[i] for i in ids]
        print(numbers_mixed)
        ids = mix(ids, numbers)

    numbers_mixed = [numbers[i] for i in ids]
    print(numbers_mixed)

    coordinate_sum = get_coordinates(numbers_mixed)
    print(f'Sum of coordinates: {coordinate_sum}')

