import numpy as np
from tqdm import tqdm

def read_input(input_file: str) -> tuple[list[int], list[list[tuple[int, int, int]]]]:
    with open(input_file) as f:
        lines = f.readlines()
    seeds = lines.pop(0).split(':')[1]
    seeds = [int(i) for i in seeds.split()]

    maps = []
    while lines:
        l = lines.pop(0).strip()
        if l == '':
            maps.append(list())
            lines.pop(0)
        else:
            numbers = tuple([int(i) for i in l.split()])
            maps[-1].append(numbers)

    sorted_maps = [sorted(m, key=lambda x: x[1]) for m in maps]
    return seeds, sorted_maps


def map_seed(seed: int, map_entries: list[tuple[int, int, int]]) -> int:
    for m in map_entries:
        dst_rng_start, src_rng_start, rng_length = m
        if src_rng_start <= seed < src_rng_start + rng_length:
            return seed + dst_rng_start - src_rng_start
    return seed


def map_seed_range(
        seed_rng_start : int,
        seed_rng_length: int,
        map_entries: list[tuple[int, int, int]]) -> list[tuple[int, int]]:
    unmapped_ranges = [(seed_rng_start, seed_rng_length)]
    mapped_ranges = []
    for m in map_entries:
        dst_rng_start, src_rng_start, rng_length = m
        seed_rng_start, seed_rng_length = unmapped_ranges.pop()
        overlap_start = max(seed_rng_start, src_rng_start)
        overlap_stop = min(seed_rng_start + seed_rng_length, src_rng_start + rng_length)
        overlap = overlap_stop - overlap_start
        if overlap > 0:
            mapped_ranges.append((
                overlap_start + dst_rng_start - src_rng_start,
                overlap
            ))
            lower_not_overlap = overlap_start - seed_rng_start
            upper_not_overlap = seed_rng_start + seed_rng_length - overlap_stop
            if lower_not_overlap > 0:
                unmapped_ranges.append((
                    seed_rng_start,
                    lower_not_overlap
                ))
            if upper_not_overlap > 0:
                unmapped_ranges.append((
                    overlap_stop,
                    upper_not_overlap
                ))
        else:
            unmapped_ranges.append((
                seed_rng_start,
                seed_rng_length
            ))
        if not unmapped_ranges:
            break
    mapped_ranges += unmapped_ranges
    return mapped_ranges


def part_1(input_file: str) -> int:
    seeds, maps = read_input(input_file)
    locations = []
    for seed in seeds:
        for m in maps:
            seed = map_seed(seed, m)
        locations.append(seed)
    return min(locations)


def part_2(input_file: str) -> int:
    seed_ranges, maps = read_input(input_file)
    unmapped_ranges = [(a, b) for a, b in zip(seed_ranges[::2], seed_ranges[1::2])]

    for m in maps:
        mapped_ranges = []
        for seed_range in unmapped_ranges:
            mapped_ranges += map_seed_range(seed_range[0], seed_range[1], m)
        unmapped_ranges = mapped_ranges

    return min([i[0] for i in mapped_ranges])


if __name__ == '__main__':
    solution_part_1 = part_1('input.txt')
    print(f'Solution to part 1: {solution_part_1}')

    solution_part_2 = part_2('input.txt')
    print(f'Solution to part 2: {solution_part_2}')
