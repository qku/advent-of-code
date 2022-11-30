import numpy as np


def initial_population(f):
    p = np.loadtxt(f, delimiter=',', dtype=np.uint64)
    compact_p = np.zeros(9, dtype=np.uint64)

    for i in np.unique(p):
        n = (p == i).sum()
        compact_p[i] = n

    return compact_p


def simulate_day(p):
    # identify how many new to spawn
    ready_to_spawn = p[0]

    # do an iteration (move 8 to 7 etc.)
    # and by rolling 0 -> 8 spawn new fish
    p = np.roll(p, -1)

    # re-add the fish who just had offspring
    p[6] += ready_to_spawn

    return p


def count_fish(p):
    return p.sum()


def simulate_n_days(p, n_days):
    for i in range(n_days):
        n = count_fish(p)
        print(f'Day {i:02d}: {n} fish')
        p = simulate_day(p)
    final_n = count_fish(p)
    print(f'Final population: {final_n}')
    return final_n


population = initial_population('input.txt')
simulate_n_days(population, 256)
