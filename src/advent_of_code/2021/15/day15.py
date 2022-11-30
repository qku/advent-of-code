import numpy as np


def read_map(f):
    return np.genfromtxt(f, delimiter=1)


def expand(risk, n=5):
    # tile array right and down
    exp_risk = np.tile(risk, (n, n))

    # add 1 for every tile step to right and down
    n_orig = risk.shape[0]
    a = np.arange(n)
    b = np.zeros((n, n))
    for i in range(n):
        b[i] = a + i
        b[i, 0] = i
    inc = np.repeat(np.repeat(b, n_orig, axis=0), n_orig, axis=1)
    exp_risk += inc

    # wrap values back so that they are <= 9
    to_wrap = exp_risk > 9
    exp_risk[to_wrap] = (exp_risk[to_wrap] % 10) + 1

    return exp_risk


def neighbors(index, max_i):
    row, column = index
    pot_n = [(row, column + 1),
             (row, column - 1),
             (row + 1, column),
             (row - 1, column)]
    return [i for i in pot_n if max(i) < max_i and min(i) >= 0]


def lowest_risk_dijkstra(f, n_expand=1, use_heuristics=False):
    risk = read_map(f)
    if n_expand > 1:
        risk = expand(risk, n_expand)

    max_i = risk.shape[0]
    a = np.arange(max_i)
    b = np.zeros_like(risk)
    for i in range(max_i):
        b[i] = a + i
        b[i, 0] = i
    heuristic_distance = np.flip(b)

    distance = np.full_like(risk, np.inf)
    distance[0, 0] = 0

    # mark initial node as current
    current = (0, 0)
    open_set = [current]

    while True:
        # loop through unvisited neighbors
        for n in neighbors(current, max_i=max_i):
            # set new distance value if lower than previous
            new_distance = distance[current] + risk[n]
            if new_distance < distance[n]:
                distance[n] = new_distance
                if n not in open_set:
                    open_set.append(n)

        # set current node to visited
        open_set.remove(current)
        if not open_set:
            break

        # choose new current node according to distance
        if use_heuristics:
            distances_open_set = [distance[i] + heuristic_distance[i] for i in open_set]
        else:
            distances_open_set = [distance[i] for i in open_set]

        current = open_set[np.argmin(distances_open_set)]
        print(current)

    return distance[-1, -1]


if __name__ == '__main__':
    # lowest = lowest_risk_dijkstra('input.txt', use_heuristics=True)
    lowest_exp = lowest_risk_dijkstra('input.txt', n_expand=5, use_heuristics=False)

    # print(f'Lowest total risk: {lowest}')
    print(f'Lowest total risk after expansion: {lowest_exp}')
