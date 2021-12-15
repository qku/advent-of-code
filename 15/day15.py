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


def lowest_risk_dijkstra(f, n_expand=1):
    risk = read_map(f)
    if n_expand > 1:
        risk = expand(risk, n_expand)

    max_i = risk.shape[0]

    unvisited = np.ones_like(risk).astype(bool)

    distance = np.full_like(risk, np.inf)
    distance[0, 0] = 0

    # mark initial node as current
    current = (0, 0)

    while unvisited[-1, -1]:
        #print(current)
        #print(distance[current])
        # loop through unvisited neighbors
        for n in neighbors(current, max_i=max_i):
            if unvisited[n]:
                # set new distance value if lower than previous
                distance[n] = np.minimum(distance[n], distance[current] + risk[n])

        # set current node to visited
        unvisited[current] = False
        if not unvisited.any():
            continue

        # status update
        n_unvisited = unvisited.sum()
        frac = 1 - (n_unvisited / unvisited.size)
        print(f'{frac:.2%}')

        # set node with the lowest distance to current
        unvisited_i = np.argwhere(unvisited)
        current = tuple(unvisited_i[distance[unvisited].argmin()])

    return distance[-1, -1]


if __name__ == '__main__':
    lowest = lowest_risk_dijkstra('input.txt')
    lowest_exp = lowest_risk_dijkstra('input.txt', n_expand=5)

    print(f'Lowest total risk: {lowest}')
    print(f'Lowest total risk after expansion: {lowest_exp}')
