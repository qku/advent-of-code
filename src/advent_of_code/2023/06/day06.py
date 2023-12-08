import math

def distance(total_time: int, acc_time: int) -> int:
    assert acc_time <= total_time
    return (total_time - acc_time) * acc_time


def get_p(times: list[int], records: list[int]) -> int:
    all_p = 1
    for t, r in zip(times, records):
        x_1 = math.ceil((t + math.sqrt(t ** 2 - 4 * r)) / 2)
        x_2 = math.floor((t - math.sqrt(t ** 2 - 4 * r)) / 2)
        p = int(abs(x_2 - x_1)) - 1
        all_p *= p
    return all_p


def part_1(input_file: str) -> int:
    with open(input_file) as f:
        times = [int(i) for i in f.readline().split(':')[1].split()]
        records = [int(i) for i in f.readline().split(':')[1].split()]
    return get_p(times, records)


def part_2(input_file: str) -> int:
    with open(input_file) as f:
        times = [int(f.readline().split(':')[1].replace(' ', ''))]
        records = [int(f.readline().split(':')[1].replace(' ', ''))]
    return get_p(times, records)


if __name__ == '__main__':
    solution_part_1 = part_1('input.txt')
    print(f'Solution to part 1: {solution_part_1}')

    solution_part_2 = part_2('input.txt')
    print(f'Solution to part 2: {solution_part_2}')
