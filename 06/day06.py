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


population = np.loadtxt('input.txt', delimiter=',', dtype=int)
# population = np.array([3, 4, 3, 1, 2], dtype=int)

for i in range(256):
    n = count_fish(population)
    print(f'Day {i:02d}: {n} fish')
    # print(population)
    population = simulate_day(population)

final_n = count_fish(population)
print(f'Final population: {final_n}')
