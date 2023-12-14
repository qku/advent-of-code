def is_valid(springs: str, groups: tuple[int, ...]) -> bool:
    lengths = tuple([len(i) for i in springs.split('.') if i != ''])
    return lengths == groups

def tree(springs: str, groups: tuple[int, ...]) -> int:
    first_unknown = springs.find('?')
    if first_unknown < 0:
        valid = is_valid(springs, groups)
        return valid
    n = 0
    for c in ['#', '.']:
        new_springs = springs[:first_unknown] + c + springs[first_unknown+1:]
        n += tree(new_springs, groups)
    return n

def part_1(input_file: str) -> int:
    tot = 0
    with open(input_file) as f:
        for line in f.readlines():
            [springs, groups] = line.split()
            groups = tuple([int(i) for i in groups.strip().split(',')])
            n = tree(springs, groups)
            tot += n
    return tot

def part_2(input_file: str) -> int:
    return 0


if __name__ == '__main__':
    solution_part_1 = part_1('input.txt')
    print(f'Solution to part 1: {solution_part_1}')

    solution_part_2 = part_2('input.txt')
    print(f'Solution to part 2: {solution_part_2}')
