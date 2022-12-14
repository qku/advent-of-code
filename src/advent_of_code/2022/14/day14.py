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
    return cave, min_x


def let_sand_fall(cave, min_x):
    start_x = 500 - min_x
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
            x, y = start_x, start_y


def print_cave(cave):
    for i in cave:
        line = str(i)
        line = line.replace(' ', '')
        line = line.replace('0', '⏹️')
        line = line.replace('1', '❇️')
        line = line.replace('2', '🧽')
        print(line)


if __name__ == '__main__':
    c, m = read_cave_file('test_input.txt')
    c_sand = let_sand_fall(c, m)
    print_cave(c_sand)
    n_sand = np.sum(c_sand == 2)
    print(f'Number of sand blocks: {n_sand}')
