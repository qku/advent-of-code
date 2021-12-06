import numpy as np


def simulate_day(p):
    # identify who is ready
    ready_to_spawn = (p == 0)

    # decrease counter for rest
    p -= 1

    # reset those that are ready
    p[ready_to_spawn] = 6

    # add new fish
    new = np.full(ready_to_spawn.sum(), 8, dtype=int)
    p = np.append(p, new)
    return p


def count_fish(p):
    return p.size


def simulate_n_days(p, n_days):
    for i in range(n_days):
        n = count_fish(p)
        print(f'Day {i:02d}: {n} fish')
        p = simulate_day(p)
    final_n = count_fish(p)
    print(f'Final population: {final_n}')
    return final_n


population = np.loadtxt('input.txt', delimiter=',', dtype=int)
# population = np.array([3, 4, 3, 1, 2], dtype=int)

simulate_n_days(population, 80)
