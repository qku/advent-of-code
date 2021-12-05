import numpy as np
import io


def read_vent_file(f_name):
    """ Read file and return 4-column array. """
    with open(f_name) as f:
        clean_lines = [line.replace(' -> ', ',') for line in f]
        data = np.genfromtxt(clean_lines, delimiter=',', dtype=int)
    return data


def get_horizontal_lines(lines):
    horizontal = (lines[:, 1] == lines[:, 3])
    return lines[horizontal]


def get_vertical_lines(lines):
    vertical = (lines[:, 0] == lines[:, 2])
    return lines[vertical]


def get_diagonal_lines(lines):
    horizontal = (lines[:, 1] == lines[:, 3])
    vertical = (lines[:, 0] == lines[:, 2])
    return lines[~ (horizontal | vertical)]


def draw_diagonal(line):
    extension = np.abs(line[0] - line[2])
    x_top_left = min(line[0], line[2])
    y_top_left = min(line[1], line[3])

    segment = np.diagflat(np.ones(extension))


def draw_map(lines, map_size=1000, consider_diagonal=False):
    m = np.zeros((map_size, map_size), dtype=int)
    for i in get_horizontal_lines(lines):
        x1 = min(i[0], i[2])
        x2 = max(i[0], i[2])
        y = i[1]
        m[y, x1:x2+1] += 1

    for i in get_vertical_lines(lines):
        x = i[0]
        y1 = min(i[1], i[3])
        y2 = max(i[1], i[3])
        m[y1:y2+1, x] += 1

    if consider_diagonal:
        for i in get_diagonal_lines(lines):
            extension = np.abs(i[0] - i[2]) + 1
            x = min(i[0], i[2])
            y = min(i[1], i[3])

            do_flip = (i[0] > i[2]) != (i[1] > i[3])

            segment = np.diagflat(np.ones(extension, dtype=int))

            if do_flip:
                segment = np.fliplr(segment)

            m[y:y+extension, x:x+extension] += segment

    return m


def evaluate_map(m, threshold=2):
    return np.count_nonzero(m >= threshold)


def print_map(m):
    bio = io.BytesIO()
    np.savetxt(bio, m, delimiter='', fmt='%1i')
    print_string = bio.getvalue().decode('utf-8')
    print_string = print_string.replace('0', '.')
    print(print_string)


all_lines = read_vent_file('input.txt')
vent_map = draw_map(all_lines)
answer = evaluate_map(vent_map)
print(f'# of points where at least two lines overlap: {answer}')

vent_map_diagonal = draw_map(all_lines, consider_diagonal=True)
answer_diagonal = evaluate_map(vent_map_diagonal)
print(f'... if considering diagonals: {answer_diagonal}')
