import numpy as np

# file = 'test_input.txt'
file = 'input.txt'
trees = np.genfromtxt(file, delimiter=1, dtype=int)

vis = np.zeros_like(trees)
vis[0, :] = 1
vis[-1, :] = 1
vis[:, 0] = 1
vis[:, -1] = 1

rows, columns = trees.shape
for i in range(1, rows-1):
    for k in range(1, columns-1):
        tree = trees[i, k]
        if (tree > trees[i+1:, k]).all() or (tree > trees[:i, k]).all() or (tree > trees[i, k+1:]).all() or (tree > trees[i, :k]).all():
            vis[i, k] = 1

print(vis.sum())

scores = np.ones_like(trees)
for i in range(rows):
    for k in range(columns):
        tree = trees[i, k]

        down = trees[i+1:, k]
        up = trees[:i, k][::-1]
        right = trees[i, k+1:]
        left = trees[i, :k][::-1]

        for m in [down, up, right, left]:
            if m.size == 0:
                # on edge
                scores[i, k] = 0
                break
            elif (tree > m).all():
                # can see all the way
                scores[i, k] *= m.size
            else:
                scores[i, k] *= (1 + np.argmax(m >= tree))

print(scores.max())
