import numpy as np


def read_map(f):
    return np.genfromtxt(f, delimiter=1)


def neighbors(index, max_i):
    row, column = index
    pot_n = [(row, column + 1),
             (row, column - 1),
             (row + 1, column),
             (row - 1, column)]
    return [i for i in pot_n if max(i) < max_i and min(i) >= 0]


def lowest_risk_dijkstra(f):
    risk = read_map(f)
    max_i = risk.shape[0]

    unvisited = np.ones_like(risk).astype(bool)

    distance = np.full_like(risk, np.inf)
    distance[0, 0] = 0

    # mark initial node as current
    current = (0, 0)

    while unvisited[-1, -1]:
        print(current)
        print(distance[current])
        # loop through unvisited neighbors
        for n in neighbors(current, max_i=max_i):
            if unvisited[n]:
                # set new distance value if lower than previous
                distance[n] = np.minimum(distance[n], distance[current] + risk[n])

        # set current node to visited
        unvisited[current] = False
        if not unvisited.any():
            continue

        # set node with the lowest distance to current
        unvisited_i = np.argwhere(unvisited)
        current = tuple(unvisited_i[distance[unvisited].argmin()])

    return distance[-1, -1]


lowest = lowest_risk_dijkstra('input.txt')
print(f'Lowest total risk: {lowest}')
