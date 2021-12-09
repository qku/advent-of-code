import numpy as np


def load_map(f):
    return np.genfromtxt(f, delimiter=1, dtype=int)


def pad_map(m):
    return np.pad(m, 1, constant_values=9)


def find_minimum_values(h_map, return_index=False):
    minima = []
    minima_index = []
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
                minima_index.append((row, column))

    if return_index:
        return minima_index
    else:
        return np.array(minima, dtype=int)


def total_risk_value(minima):
    return (minima + 1).sum()


def neighbors(index):
    row, column = index
    up = (row - 1, column)
    down = (row + 1, column)
    left = (row, column - 1)
    right = (row, column + 1)
    return [up, down, left, right]


def flood_fill(node, a):
    for i in neighbors(node):
        if a[i] == 0:
            a[i] = 1
            flood_fill(i, a)
    return a


def determine_basin_size(h_map, minimum_index):
    # map identifying the basin
    #  0 -> not checked yet
    #  1 -> part of basin
    # -1 -> not part of basin

    basin = np.zeros_like(h_map, dtype=int)
    basin[minimum_index] = 1
    basin[h_map == 9] = -1

    basin = flood_fill(minimum_index, basin)
    return (basin > 0).sum()


def product_of_three_largest_basins(h_map):
    minima = find_minimum_values(h_map, return_index=True)
    basin_sizes = [determine_basin_size(h_map, i) for i in minima]
    three_largest = np.sort(basin_sizes)[-3:]
    return np.prod(three_largest)


heightmap = load_map('input.txt')
heightmap_padded = pad_map(heightmap)
minimum_values = find_minimum_values(heightmap_padded)
print(f'Total risk value: {total_risk_value(minimum_values)}')
print(f'Product of three largest basins: {product_of_three_largest_basins(heightmap_padded)}')
