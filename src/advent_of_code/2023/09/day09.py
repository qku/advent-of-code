import numpy as np

def read_input(input_file: str) -> list[np.ndarray]:
    sequences = []
    with open(input_file) as f:
        for line in f.readlines():
            sequences.append(
                np.array([int(i) for i in line.split()])
            )
    return sequences


def part_1(input_file: str) -> int:
    tot_s = 0
    for seq in read_input(input_file):
        s = 0
        while not np.all(seq == 0):
            s += seq[-1]
            seq = np.diff(seq)
        tot_s += s
    return tot_s


def part_2(input_file: str) -> int:
    tot_s = 0
    for seq in read_input(input_file):
        s = 0
        a = 1
        while not np.all(seq == 0):
            s += a * seq[0]
            a *= -1
            seq = np.diff(seq)
        tot_s += s
    return tot_s


if __name__ == '__main__':
    solution_part_1 = part_1('input.txt')
    print(f'Solution to part 1: {solution_part_1}')

    solution_part_2 = part_2('input.txt')
    print(f'Solution to part 2: {solution_part_2}')
