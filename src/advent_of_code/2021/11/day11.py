import numpy as np


def read_start_config(f):
    return np.genfromtxt(f, delimiter=1, dtype=float)


def neighbors(index, max_i=9):
    """ Find (also diagonal) neighbor indices. """
    row, column = index
    n = []
    for i in [-1, 0, 1]:
        for k in [-1, 0, 1]:
            if i == k == 0:
                continue
            n_row = row + i
            n_column = column + k
            if min(n_row, n_column) >= 0 and max(n_row, n_column) <= max_i:
                n.append((n_row, n_column))
    return n


def do_step(a):
    flashes = 0

    # increase energy level of all by one
    a += 1

    while np.any(a > 9):
        for ix, iy in np.argwhere(a > 9):
            # prevent octopus from flashing again
            a[ix, iy] = np.nan
            flashes += 1
            for k in neighbors((ix, iy)):
                # increase energy level of all neighbors by one
                try:
                    a[k] += 1
                # if out of bounds, do nothing
                except IndexError:
                    continue

    # reset flashed fish
    a[np.isnan(a)] = 0
    return flashes


def do_n_steps(f, n):
    config = read_start_config(f)
    flashes = 0
    for i in range(n):
        flashes += do_step(config)
    return flashes


def first_simultaneous(f):
    config = read_start_config(f)
    n = 0
    flashes = 0
    while flashes != 100:
        n += 1
        flashes = do_step(config)
    return n


n_flashes = do_n_steps('input.txt', 100)
n_sim = first_simultaneous('input.txt')
print(f'Flashes after 100 steps: {n_flashes}')
print(f'First simultaneous flash in step: {n_sim}')
