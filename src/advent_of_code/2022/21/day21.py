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


if __name__ == '__main__':
    d = read_file('input.txt')
    print(d)

    while type(d['root']) != int:
        for k in d:

            v = d[k]
            if type(v) == int:
                continue
            else:
                o1, o2 = d[v[0]], d[v[2]]
                if type(o1) == int and type(o2) == int:
                    match v[1]:
                        case '+': d[k] = o1 + o2
                        case '-': d[k] = o1 - o2
                        case '/': d[k] = o1 // o2
                        case '*': d[k] = o1 * o2
                    print(d)

    root_monkey = d['root']
    print(f'Root monkey yells: {root_monkey}')
