from collections import Counter
import numpy as np


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
        p = polymer_step(p, pair_dict)

    counts = sorted(Counter(p).values())
    return counts[-1] - counts[0]


def get_pair_counter(p, pair_dict):
    pair_counter = np.zeros(len(pair_dict), dtype=np.uint64)
    for a, b in zip(p[:-1], p[1:]):
        i = list(pair_dict).index(a + b)
        pair_counter[i] += 1
    return pair_counter


def get_pc_update_info(pair_dict):
    pc_update_info = []
    for pair, new in pair_dict.items():
        left, right = pair[0], pair[1]

        i_new_pair_1 = list(pair_dict).index(left + new)
        i_new_pair_2 = list(pair_dict).index(new + right)
        pc_update_info.append([i_new_pair_1, i_new_pair_2])
    return pc_update_info


def polymer_step_pc(pair_counter, pc_update_info):
    new_pair_counter = np.zeros_like(pair_counter)
    for n_pairs, i_new_pairs in zip(pair_counter, pc_update_info):
        new_pair_counter[i_new_pairs] += n_pairs

    return new_pair_counter


def diff_after_n_steps_pc(f, n):
    p, pair_dict = read_input(f)
    pair_counter = get_pair_counter(p, pair_dict)
    pc_update_info = get_pc_update_info(pair_dict)

    for i in range(n):
        pair_counter = polymer_step_pc(pair_counter, pc_update_info)

    letter_dict = {letter: 0 for letter in pair_dict.values()}
    for n, pair in zip(pair_counter, pair_dict):
        a, b = pair[0], pair[1]
        letter_dict[a] += n
        letter_dict[b] += n
    letter_occ = sorted(letter_dict.values())
    return (letter_occ[-1] - letter_occ[0] + 1) / 2


n_1 = diff_after_n_steps('input.txt', 10)
print(f'Diff. after 10 steps: {n_1}')

n_2 = diff_after_n_steps_pc('input.txt', 40)
print(f'Diff. after 40 steps: {n_2}')
