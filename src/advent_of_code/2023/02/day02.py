def min_rgb(game_str: str) -> (int, int, int):
    red, green, blue = 0, 0, 0
    rounds = game_str.split(': ')[1].strip().split('; ')
    for r in rounds:
        contents = r.split(', ')
        for c in contents:
            n = int(c.split(' ')[0])
            if c.endswith('red'):
                red = max(red, n)
            elif c.endswith('green'):
                green = max(green, n)
            elif c.endswith('blue'):
                blue = max(blue, n)
            else:
                raise AssertionError
    return red, green, blue


def part_1(input_file: str) -> int:
    possible = 0
    with open(input_file) as f:
        for i, line in enumerate(f.readlines()):
            red, green, blue = min_rgb(line)
            if red <= 12 and green <= 13 and blue <= 14:
                possible += i + 1
    return possible


def power_of_min_set(r: int, g: int, b: int) -> int:
    return r * g * b


def part_2(input_file: str) -> int:
    power_min_set_sum = 0
    with open(input_file) as f:
        for i, line in enumerate(f.readlines()):
            red, green, blue = min_rgb(line)
            power_min_set_sum += red * green * blue
    return power_min_set_sum


if __name__ == '__main__':
    solution_part_1 = part_1('input.txt')
    print(f'Solution to part 1: {solution_part_1}')

    solution_part_2 = part_2('input.txt')
    print(f'Solution to part 2: {solution_part_2}')
