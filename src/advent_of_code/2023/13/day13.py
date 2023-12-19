import numpy as np

def read_input(input_file: str) -> list[np.ndarray]:
    patterns = []
    with open(input_file) as f:
        pattern = []
        for line in f:
            line = line.strip()
            if line:
                pattern.append([0 if i == '.' else 1 for i in line])
            else:
                patterns.append(np.array(pattern))
                pattern = []
        patterns.append(np.array(pattern))
    return patterns

def find_horizontal_split(pattern: np.ndarray, smudged: bool = False) -> int:
    split = 1
    rows = pattern.shape[0]
    while split < rows:
        if split > rows - split:
            up = pattern[-2*(rows - split):split]
            dw = pattern[split:]
        else:
            up = pattern[:split]
            dw = pattern[split:2*split]
        if not smudged and np.all(up == dw[::-1]):
            return split
        elif smudged and np.sum(up == dw[::-1]) == up.size - 1:
            return split
        split += 1
    return -1

def part_1(input_file: str) -> int:
    patterns = read_input(input_file)
    summary = 0
    for pattern in patterns:
        horizontal_split = find_horizontal_split(pattern)
        if horizontal_split > 0:
            summary += 100 * horizontal_split
        else:
            summary += find_horizontal_split(pattern.T)
    return summary


def part_2(input_file: str) -> int:
    patterns = read_input(input_file)
    summary = 0
    for pattern in patterns:
        horizontal_split = find_horizontal_split(pattern, smudged=True)
        if horizontal_split > 0:
            summary += 100 * horizontal_split
        else:
            summary += find_horizontal_split(pattern.T, smudged=True)
    return summary


if __name__ == '__main__':
    solution_part_1 = part_1('input.txt')
    print(f'Solution to part 1: {solution_part_1}')

    solution_part_2 = part_2('input.txt')
    print(f'Solution to part 2: {solution_part_2}')
