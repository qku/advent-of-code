import numpy as np


def adjacent(a, b):
    d = np.abs(a - b)
    d.sort()
    if np.all(d == np.array([0, 0, 1])):
        # print(d)
        return True
    else:
        return False


cubes = np.genfromtxt('input.txt', delimiter=',', dtype=int)

n = cubes.shape[0]
open_surfaces = np.full(n, 6)

for i in range(n):
    print(i, n)
    for k in range(n):
        if adjacent(cubes[i], cubes[k]):
            open_surfaces[k] -= 1

total_surface = open_surfaces.sum()
print(f'Lava droplet surface: {total_surface}')
