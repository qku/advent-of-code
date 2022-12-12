import numpy as np
import matplotlib.pyplot as plt


def read_map(file):
    _m = np.genfromtxt(file, delimiter=1, dtype=object)
    _start = tuple(list(np.argwhere(_m == b'S')[0]))
    _target = tuple(list(np.argwhere(_m == b'E')[0]))
    _m[_start] = b'a'
    _m[_target] = b'z'
    _m = np.vectorize(ord)(_m)
    _m -= _m.min()
    return _m, _start, _target


def accessible_neighbors(index, _m):
    row, column = index
    pot_n = [(row, column + 1),
             (row, column - 1),
             (row + 1, column),
             (row - 1, column)]
    in_bound = []
    for i in pot_n:
        try:
            _m[i]
        except IndexError:
            pass
        else:
            in_bound.append(i)
    return [i for i in in_bound if _m[i] - _m[index] <= 1]


def dijkstra(_m, _start, _target):
    distance = np.full_like(_m, np.inf)
    distance[_start] = 0

    current = _start
    open_set = [current]

    while True:
        new_d = distance[current] + 1
        for n in accessible_neighbors(current, _m):
            if new_d < distance[n]:
                distance[n] = new_d
                if n not in open_set:
                    open_set.append(n)

        open_set.remove(current)
        if current == _target or not open_set:
            return distance[_target]

        distances_open_set = [distance[i] for i in open_set]
        current = open_set[np.argmin(distances_open_set)]


if __name__ == '__main__':
    m, start, target = read_map('input.txt')

    # fig, ax = plt.subplots()
    # ax.imshow(m)
    # ax.plot(start[1], start[0], 'x')
    # ax.plot(target[1], target[0], 'x')
    # plt.show()

    min_distance = dijkstra(m, start, target)
    print(f'Min. distance: {min_distance}')

    min_distances = []
    for start in zip(*np.where(m == 0)):
        min_distances.append(dijkstra(m, start, target))
    print(f'Min. distance of all: {min(min_distances)}')
