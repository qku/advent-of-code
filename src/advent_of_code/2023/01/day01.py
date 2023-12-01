def part_1(input_file: str) -> int:
    calibration_value = 0
    with open(input_file) as f:
        for line in f.readlines():
            for i in line:
                try:
                    first_digit = int(i)
                    break
                except ValueError:
                    continue
            else:
                raise AssertionError
            for i in line[::-1]:
                try:
                    last_digit = int(i)
                    break
                except ValueError:
                    continue
            else:
                raise AssertionError
            calibration_value += int(f'{first_digit}{last_digit}')
    return calibration_value

numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

reversed_numbers = {number[::-1]: value for number, value in numbers.items()}

def find_first_written_digit(s: str, rev=False):
    first_number_found = 0
    first_number_index = len(s)
    if rev:
        my_numbers = reversed_numbers
    else:
        my_numbers = numbers
    for number, value in my_numbers.items():
        i = s.find(number)
        if 0 <= i < first_number_index:
            first_number_found = value
            first_number_index = i
    return first_number_found, first_number_index


def part_2(input_file: str) -> int:
    calibration_value = 0
    with open(input_file) as f:
        for line in f.readlines():
            for i, number in enumerate(line):
                try:
                    first_digit = int(number)
                    break
                except ValueError:
                    continue
            first_written, first_written_index = find_first_written_digit(line)
            if first_written_index < i:
                first_number = first_written
            else:
                first_number = first_digit
            for i, number in enumerate(line[::-1]):
                try:
                    last_digit = int(number)
                    break
                except ValueError:
                    continue
            last_written, last_written_index = find_first_written_digit(
                line[::-1], rev=True)
            if last_written_index < i:
                last_number = last_written
            else:
                last_number = last_digit
            calibration_value += int(f'{first_number}{last_number}')
    return calibration_value


if __name__ == '__main__':
    solution_part_1 = part_1('input.txt')
    print(f'Solution to part 1: {solution_part_1}')

    solution_part_2 = part_2('input.txt')
    print(f'Solution to part 2: {solution_part_2}')
