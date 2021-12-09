import numpy as np


def load_map(f):
    return np.genfromtxt(f, delimiter=1, dtype=int)


def pad_map(m):
    return np.pad(m, 1, constant_values=9)


def find_minimum_values(h_map):
    minima = []
    rows, columns = h_map.shape
    for row in range(1, rows - 1):
        for column in range(1, columns - 1):
            val = h_map[row, column]

            up = h_map[row - 1, column]
            down = h_map[row + 1, column]
            left = h_map[row, column - 1]
            right = h_map[row, column + 1]

            if val < min(up, down, left, right):
                minima.append(val)

    return np.array(minima, dtype=int)


def total_risk_value(minima):
    return (minima + 1).sum()


heightmap = load_map('input.txt')
heightmap_padded = pad_map(heightmap)
minimum_values = find_minimum_values(heightmap_padded)
print(f'Total risk value: {total_risk_value(minimum_values)}')
