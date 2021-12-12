import numpy as np


def get_cave_map(f):
    return np.loadtxt(f, delimiter='-', dtype='str')


def find_next(last, cm):
    n = []
    for a, b in cm:
        if a == last:
            n.append(b)
        elif b == last:
            n.append(a)
    return n


def small_twice(path):
    for i in path:
        if i[0].islower() and path.count(i) > 1:
            return True
    return False


def extend_path(paths_to_here, cm, allow_twice=False):
    extended_paths = []
    for i in paths_to_here:
        last = i[-1]
        if last == 'end':
            continue
        next_caves = find_next(last, cm)
        extended = []
        for k in next_caves:
            if k[0].islower() and k in i:
                if k in ['start', 'end']:
                    continue
                elif not small_twice(i) and allow_twice:
                    # one cave is allowed to be visited twice
                    pass
                else:
                    # do not visit small caves twice
                    continue
            extended_paths.append(i + [k])
    return extended_paths


def find_all_paths(f, allow_twice=False):
    cm = get_cave_map(f)
    paths_to_extend = [['start']]
    finished_paths = []
    while paths_to_extend:
        new_paths = extend_path(paths_to_extend, cm, allow_twice=allow_twice)
        finished_paths += [i for i in new_paths if i[-1] == 'end']
        paths_to_extend = [i for i in new_paths if i[-1] != 'end']
    return len(finished_paths)


n_1 = find_all_paths('input.txt')
print(f'Number of paths through cave: {n_1}')

n_2 = find_all_paths('input.txt', allow_twice=True)
print(f'if visiting twice is sometimes allowed: {n_2}')
