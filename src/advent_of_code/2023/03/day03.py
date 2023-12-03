def is_number(c: str) -> bool:
    try:
        int(c)
    except ValueError:
        return False
    else:
        return True


def neighbors_indices(row: int, column: int, matrix: list[str]) -> list[tuple[int, int]]:
    res = []
    row_count = len(matrix)
    column_count = len(matrix[0])
    for d_row in [-1, 0, 1]:
        for d_column in [-1, 0, 1]:
            neighbor_row = row + d_row
            neighbor_column = column + d_column
            if d_row == d_column == 0:
                continue
            if 0 <= neighbor_row < row_count and 0 <= neighbor_column < column_count:
                res.append((row + d_row, column + d_column))
    return res

def neighbors(row: int, column: int, matrix: list[str]) -> list[str]:
    indices = neighbors_indices(row, column, matrix)
    res = [matrix[row][column] for row, column in indices]
    return res


def contains_symbol(chars: list[str]) -> bool:
    for i in chars:
        if not is_number(i) and i != '.':
            return True
    return False


def get_lines(input_file: str) -> list[str]:
    with open(input_file) as f:
        lines = f.readlines()
        return [l.strip() for l in lines]


def part_1(input_file: str) -> int:
    lines = get_lines(input_file)
    sum_of_part_numbers = 0
    for row, line in enumerate(lines):
        current_number = ''
        adjacent_to_symbol = False
        for column, c in enumerate(line):
            if is_number(c):
                current_number += c
                n = neighbors(row, column, lines)
                if contains_symbol(n):
                    adjacent_to_symbol = True
            if not is_number(c) or column == len(line) - 1:
                if current_number:
                    if adjacent_to_symbol:
                        sum_of_part_numbers += int(current_number)
                    current_number = ''
                    adjacent_to_symbol = False

    return sum_of_part_numbers

# iterate again: for each number, if adjacent to start, save to which star
# and multiply by extingn gear ratio onec number is done

def get_gear_indices(lines: list[str]) -> list[tuple[int, int]]:
    res = []
    for row, line in enumerate(lines):
        for column, c in enumerate(line):
            if c == '*':
                res.append((row, column))
    return res


def part_2(input_file: str) -> int:
    lines = get_lines(input_file)
    gear_indices = get_gear_indices(lines)
    gear_ratios = {i: [] for i in gear_indices}

    for row, line in enumerate(lines):
        current_number = ''
        adjacent_to_gear = False
        for column, c in enumerate(line):
            if is_number(c):
                current_number += c
                for n_row, n_column in neighbors_indices(row, column, lines):
                    if lines[n_row][n_column] == '*':
                        adjacent_to_gear = (n_row, n_column)
            if not is_number(c) or column == len(line) - 1:
                if current_number:
                    print(current_number, adjacent_to_gear)
                    if adjacent_to_gear:
                        gear_ratios[adjacent_to_gear].append(int(current_number))
                    current_number = ''
                    adjacent_to_gear = False
    return sum([i[0] * i[1] for i in gear_ratios.values() if len(i) == 2])


if __name__ == '__main__':
    solution_part_1 = part_1('input.txt')
    print(f'Solution to part 1: {solution_part_1}')

    solution_part_2 = part_2('input.txt')
    print(f'Solution to part 2: {solution_part_2}')
