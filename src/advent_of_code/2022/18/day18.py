import numpy as np


def adjacent(a, b):
    d = np.abs(a - b)
    d.sort()
    if np.all(d == np.array([0, 0, 1])):
        # print(d)
        return True
    else:
        return False


def naive_surface(_cubes):
    n = _cubes.shape[0]
    open_surfaces = np.full(n, 6)

    for _i in range(n):
        print(_i, n)
        for k in range(n):
            if adjacent(cubes[_i], cubes[k]):
                open_surfaces[k] -= 1

    return open_surfaces.sum()


def neighbors(a, max_size):
    _x, _y, _z = a
    _n = [
        (_x + 1, _y, _z),
        (_x - 1, _y, _z),
        (_x, _y + 1, _z),
        (_x, _y - 1, _z),
        (_x, _y, _z + 1),
        (_x, _y, _z - 1)
    ]
    _n_true = []
    for _i in _n:
        for _k in _i:
            if 0 <= _k < max_size:
                continue
            else:
                break
        else:
            _n_true.append(_i)
    return _n_true


def gas_expansion(origin, _grid):
    max_size = _grid.shape[0]
    surface = 0
    visited = set()
    q = {origin}
    while q:
        current = q.pop()
        for _n in neighbors(current, max_size):
            v = _grid[_n]
            if _n in visited:
                continue
            if v == 0:
                q.add(_n)
            elif v == 1:
                surface += 1
        visited.add(current)
    return surface


def edge_surface(_cubes):
    surface = np.any(_cubes == 0, axis=1).sum()
    return surface


if __name__ == '__main__':
    cubes = np.genfromtxt('input.txt', delimiter=',', dtype=int)

    # part I (very inefficient)
    # total_surface = naive_surface(cubes)
    # print(f'Lava droplet surface: {total_surface}')

    # part II
    max_xyz = cubes.max() + 2
    grid = np.zeros((max_xyz, max_xyz, max_xyz), dtype=int)
    for i in cubes:
        grid[i[0], i[1], i[2]] = 1

    exterior_surface = gas_expansion((0, 0, 0), grid) + edge_surface(cubes)
    print(f'Total exterior surface: {exterior_surface}')
