import numpy as np


def read_cave_file(_file):
    with open(_file) as f:
        paths = []
        max_x, min_x, max_y = 0, 1000, 0
        for path in f.readlines():
            points_str = path.split(' -> ')
            points = []
            for p in points_str:
                x, y = p.split(',')
                x = int(x)
                y = int(y)
                max_x = max(max_x, x)
                min_x = min(min_x, x)
                max_y = max(max_y, y)
                points.append([x, y])
            paths.append(points)

    cave = np.zeros((1+max_y, 1+max_x-min_x), dtype=int)
    for path in paths:
        start = path.pop(0)
        start[0] -= min_x
        while path:
            end = path.pop(0)
            end[0] -= min_x

            y = sorted([start[0], end[0]])
            x = sorted([start[1], end[1]])

            cave[x[0]:x[1]+1, y[0]:y[1]+1] = 1

            start = end
    return cave, 500 - min_x


def pad_cave(cave, start_x):
    pad_bottom = 2
    cave = np.pad(cave, [(0, pad_bottom), (0, 0)])

    pad_right = (start_x + cave.shape[0]) - cave.shape[1]
    pad_left = abs(start_x - cave.shape[0])
    cave = np.pad(cave, [(0, 0), (pad_left, pad_right)])
    cave[-1] = 1
    return cave, cave.shape[1] // 2


def let_sand_fall(cave, start_x):
    start_y = 0
    x, y = start_x, start_y
    while True:
        b_y = y + 1
        for i in [0, -1, 1]:
            b_x = x + i
            if b_x < 0 or b_y >= cave.shape[0]:
                cave[y, x] = 0
                return cave
            if cave[b_y, b_x] == 0:
                cave[b_y, b_x] = 2
                cave[y, x] = 0
                x, y = b_x, b_y
                break
        else:
            if x == start_x and y == start_y:
                cave[y, x] = 2
                return cave
            x, y = start_x, start_y


def print_cave(cave):
    for i in cave:
        line = str(i)
        line = line.replace(' ', '')
        line = line.replace('0', '⏹️')
        line = line.replace('1', '❇️')
        line = line.replace('2', '🧽')
        print(line)
    print()


if __name__ == '__main__':
    c, sand_x = read_cave_file('input.txt')
    c_sand = let_sand_fall(c, sand_x)
    print_cave(c_sand)
    n_sand = np.sum(c_sand == 2)
    print(f'Number of sand blocks: {n_sand}\n')

    c, sand_x = read_cave_file('input.txt')
    c_pad, sand_x = pad_cave(c, sand_x)
    c_sand = let_sand_fall(c_pad, sand_x)
    print_cave(c_sand)
    n_sand = np.sum(c_sand == 2)
    print(f'Number of sand blocks with rock bottom: {n_sand}')
