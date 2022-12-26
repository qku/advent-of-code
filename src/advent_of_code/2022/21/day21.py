def read_file(file):
    with open(file) as f:
        _d = {}
        for i in f.readlines():
            _k, _v = i.split(':')
            try:
                _v = int(_v)
            except ValueError:
                _v = tuple(_v.split())
            _d[_k] = _v
    return _d


def update_monkey_dict(_d):
    for k in _d:
        v = _d[k]
        if type(v) == int:
            continue
        else:
            try:
                o1, o2 = _d[v[0]], _d[v[2]]
            except KeyError:
                continue
            if type(o1) == int and type(o2) == int:
                match v[1]:
                    case '+':
                        _d[k] = o1 + o2
                    case '-':
                        _d[k] = o1 - o2
                    case '/':
                        _d[k] = o1 // o2
                    case '*':
                        _d[k] = o1 * o2


def reverse_calc(_d, _monkey_to_match, _number_to_match):
    while _monkey_to_match != 'humn':
        print(d[_monkey_to_match], _number_to_match)
        o1, op, o2 = d[_monkey_to_match]
        if o1 == 'humn':
            number = d[o2]
            _monkey_to_match = 'humn'
        elif o2 == 'humn':
            number = d[o1]
            _monkey_to_match = 'humn'
        elif type(d[o1]) == int:
            number = d[o1]
            _monkey_to_match = o2
        else:
            number = d[o2]
            _monkey_to_match = o1
        print(number, _monkey_to_match)
        if op in '+*':
            if op == '+':
                _number_to_match = _number_to_match - number
            else:
                _number_to_match = _number_to_match // number
        elif op in '-/':
            if op == '-':
                if number == d[o2]:
                    _number_to_match = _number_to_match + number
                else:
                    _number_to_match = number - _number_to_match
            else:
                if number == d[o2]:
                    _number_to_match = number * _number_to_match
                else:
                    _number_to_match = number // _number_to_match
        print(_number_to_match)
        print()
    return _number_to_match


if __name__ == '__main__':
    d = read_file('input.txt')
    while type(d['root']) != int:
        update_monkey_dict(d)

    root_monkey = d['root']
    print(f'Root monkey yells: {root_monkey}')

    # part II
    d = read_file('input.txt')
    root_match_a, root_match_b = d['root'][0], d['root'][2]
    del d['root']
    del d['humn']

    d_old = {}
    # while type(d[root_match_a]) != int and type(d[root_match_b]) != int:
    while d_old != d:
        d_old = d.copy()
        update_monkey_dict(d)

    if type(d[root_match_a]) != int:
        monkey_to_match = root_match_a
        number_to_match = d[root_match_b]
    else:
        monkey_to_match = root_match_b
        number_to_match = d[root_match_a]

    number_to_match = reverse_calc(d, monkey_to_match, number_to_match)
    print(f'humn must yell: {number_to_match}')

    # check
    d['humn'] = number_to_match
    while d_old != d:
        d_old = d.copy()
        update_monkey_dict(d)

    print(d[root_match_a], d[root_match_b])
