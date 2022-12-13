from functools import cmp_to_key


def compare(_left, _right):
    # print(f'Compare {_left} to {_right}')
    if type(_left) == list or type(_right) == list:
        if type(_right) != list:
            _right = [_right]
        elif type(_left) != list:
            _left = [_left]

        __left = _left.copy()
        __right = _right.copy()
        while __left and __right:
            _res = compare(__left.pop(0), __right.pop(0))
            if _res != 0:
                return _res
        if __left and not __right:
            return 1
        elif __right and not __left:
            return -1
        else:
            return 0

    else:
        if _left > _right:
            return 1
        elif _left < _right:
            return -1
        else:
            return 0


if __name__ == '__main__':
    file = 'input.txt'
    pair_index = 1
    right_order = []
    with open(file) as f:
        while True:
            try:
                left = eval(f.readline())
                right = eval(f.readline())
            except SyntaxError:
                break
            _ = f.readline()
            res = compare(left, right)
            if res == -1:
                right_order.append(pair_index)
            pair_index += 1

    print(f'Sum of pair index in right order: {sum(right_order)}')

    packages = []
    with open(file) as f:
        while True:
            try:
                for _ in range(2):
                    packages.append(eval(f.readline()))
                f.readline()
            except SyntaxError:
                break
    div_a, div_b = [[2]], [[6]]
    packages.append(div_a)
    packages.append(div_b)

    print(packages)
    packages = sorted(packages, key=cmp_to_key(compare))
    print(packages)
    decoder_key = (1 + packages.index(div_a)) * (1 + packages.index(div_b))
    print(f'Decoder key: {decoder_key}')
