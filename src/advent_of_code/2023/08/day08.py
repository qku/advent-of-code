from math import lcm


def read_input(input_file: str) -> tuple[list[int], dict[str, tuple[str, str]]]:
    with open(input_file) as f:
        directions = list(f.readline().strip())
        directions = [0 if i == 'L' else 1 for i in directions]

        f.readline()
        desert_map: dict[str, tuple[str, str]] = {}
        for i in f.readlines():
            splits = i.split('=')
            source = splits[0].strip()
            destinations = splits[1].strip().strip('()').split(',')
            left = destinations[0].strip()
            right = destinations[1].strip()
            desert_map[source] = (left, right)
    return directions, desert_map


def part_1(input_file: str) -> int:
    directions, desert_map = read_input(input_file)
    location = 'AAA'
    steps = 0
    while True:
        for d in directions:
            location = desert_map[location][d]
            steps += 1
            if location == 'ZZZ':
                return steps


def find_periodicity(
        directions: list[int],
        desert_map: dict[str, tuple[str, str]],
        location: str
) -> int:
    steps = 0
    while True:
        for d in directions:
            location = desert_map[location][d]
            steps += 1
            if location.endswith('Z'):
                return steps


def part_2(input_file: str) -> int:
    directions, desert_map = read_input(input_file)
    locations = [i for i in desert_map if i.endswith('A')]
    p = [find_periodicity(directions, desert_map, l) for l in locations]
    return lcm(*tuple(p))


if __name__ == '__main__':
    solution_part_1 = part_1('input.txt')
    print(f'Solution to part 1: {solution_part_1}')

    solution_part_2 = part_2('input.txt')
    print(f'Solution to part 2: {solution_part_2}')
