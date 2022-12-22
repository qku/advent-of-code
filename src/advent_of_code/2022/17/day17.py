from itertools import cycle
import numpy as np
import matplotlib.pyplot as plt


def read_input(file):
    with open(file) as f:
        content = f.readline().strip()
    directions = []
    for i in content:
        if i == '<':
            directions.append(-1)
        elif i == '>':
            directions.append(1)
        else:
            raise AssertionError
    return directions


def print_cave(_cave):
    for i in _cave:
        line = str(i)
        line = line.replace('1', '⏹')
        line = line.replace('0', '.')
        print(line)
    print()


def measure_height(_cave):
    assert np.all(0 <= _cave) and np.all(1 >= _cave)
    floors_to_crop = 0
    while _cave[floors_to_crop].sum() == 2:
        floors_to_crop += 1
    return _cave.shape[0] - floors_to_crop - 1


def find_pattern(_increase):
    crop = 0
    while crop < _increase.size:
        cropped = _increase[crop:]
        n = 5
        while n <= cropped.size // 2:
            candidate = cropped[:n]

            repetitions = 1
            while n * (repetitions + 1) <= cropped.size:
                check = cropped[n * repetitions:n * (repetitions + 1)]
                if np.all(check == candidate):
                    print(f'Found candidate that repeats {repetitions}x of length {n} after cropping {crop} lines.')
                else:
                    break
                repetitions += 1
            else:
                print(f'Found fully repeating pattern of length {n} after cropping {crop} lines.')
                return crop, candidate
            n += 1
        crop += 1


if __name__ == '__main__':
    jet_pattern = read_input('input.txt')
    jet_pattern = cycle(jet_pattern)

    rocks = [
        np.array([[1, 1, 1, 1]]),
        np.array([[0, 1, 0],
                  [1, 1, 1],
                  [0, 1, 0]]),
        np.array([[0, 0, 1],
                  [0, 0, 1],
                  [1, 1, 1]]),
        np.array([[1],
                  [1],
                  [1],
                  [1]]),
        np.array([[1, 1],
                 [1, 1]])
    ]
    rocks = cycle(rocks)

    # create just cave floor
    cave = np.ones((1, 9), dtype=int)

    pile_heights = []
    n_rocks = 9001
    for _ in range(n_rocks):
        # print(_ / n)
        rock = next(rocks)
        height, width = rock.shape

        floors_to_append = height + 3
        extension = np.zeros((floors_to_append, 9), dtype=int)
        extension[:, 0] = 1
        extension[:, -1] = 1
        cave = np.concatenate([extension, cave])

        right, down = 3, 0
        while True:
            potential_right = right + next(jet_pattern)
            overlap = cave[down:down + height, potential_right:potential_right + width] + rock
            if np.all(overlap < 2):
                right = potential_right

            potential_down = down + 1
            overlap = cave[potential_down:potential_down + height, right:right + width] + rock
            if np.all(overlap < 2):
                down = potential_down
            else:
                break
        cave[down:down + height, right:right + width] += rock

        top_index = np.argmax(cave.sum(axis=1) > 2)
        cave = cave[top_index:]
        pile_heights.append(measure_height(cave))

    rock_pile_height = measure_height(cave)
    print(f'Pile after {n_rocks} rocks is {rock_pile_height} high.')
    # plt.plot(pile_heights)
    # plt.show()

    increase = np.diff(pile_heights)
    lines_to_crop, pattern = find_pattern(increase)

    n_rocks_extreme = 1000000000000
    crop_pile = pile_heights[lines_to_crop]
    n_remaining = n_rocks_extreme - lines_to_crop
    full_reps = n_remaining // pattern.size
    partial_rep = n_remaining % pattern.size

    extreme_pile_height = crop_pile + full_reps * pattern.sum() + pattern[:partial_rep-1].sum()
    print(f'Pile after {n_rocks} rocks is {extreme_pile_height} high.')
