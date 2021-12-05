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


def draw_map(lines, map_size=1000):
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

    return m


def evaluate_map(m, threshold=2):
    return np.count_nonzero(m >= threshold)


def print_map(m):
    bio = io.BytesIO()
    np.savetxt(bio, m, delimiter='', fmt='%1i')
    print_string = bio.getvalue().decode('utf-8')
    print(print_string)


all_lines = read_vent_file('input.txt')
vent_map = draw_map(all_lines)
answer = evaluate_map(vent_map)
print(f'# of points where at least two lines overlap: {answer}')

