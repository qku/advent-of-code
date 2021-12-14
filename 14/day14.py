from collections import Counter


def read_input(f):
    with open(f) as file:
        lines = file.readlines()

    template = list(lines[0].strip())

    pair_dict = {}
    for line in lines[2:]:
        k = line[:2]
        v = line.strip()[-1]
        pair_dict[k] = v

    return template, pair_dict


def polymer_step(p, pair_dict):
    # find new elements
    new = []
    for a, b in zip(p[:-1], p[1:]):
        new.append(pair_dict[a + b])

    # intertwine lists
    last = p[-1]
    p = [i for pair in zip(p, new) for i in pair]
    p.append(last)
    return p


def diff_after_n_steps(f, n):
    p, pair_dict = read_input(f)

    for i in range(n):
        print(i)
        p = polymer_step(p, pair_dict)

    counts = sorted(Counter(p).values())
    return counts[-1] - counts[0]


n_1 = diff_after_n_steps('input.txt', 10)
print(f'Diff. after 10 steps: {n_1}')

n_2 = diff_after_n_steps('input.txt', 40)
print(f'Diff. after 40 steps: {n_2}')
