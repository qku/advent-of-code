import numpy as np

def read_input(input_file: str) -> np.ndarray:
    with open(input_file) as f:
        lines = [
            i.strip().replace('.', '0').replace('#', '1')
            for i in f.readlines()
        ]
    return np.array([[int(k) for k in i] for i in lines])

def expand(image: np.ndarray) -> np.ndarray:
    for axis in range(2):
        i, inserted = 0, 0
        while i + inserted < image.shape[axis]:
            if image.sum(axis=int(not axis))[i + inserted] == 0:
                image = np.insert(image, i + inserted, 0, axis=axis)
                inserted += 1
            i += 1
    return image

def find_galaxies(image: np.ndarray) -> list[tuple[int, int]]:
    return [tuple(i) for i in np.transpose(np.nonzero(image))]

def min_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def sum_of_distances(galaxies: list[tuple[int, int]]) -> int:
    distances = []
    while galaxies:
        a = galaxies.pop()
        for b in galaxies:
            distances.append(min_distance(a, b))
    return sum(distances)

def sum_of_distances_after_expansion(image: np.ndarray, n: int = 1) -> int:
    galaxies = find_galaxies(image)
    unexpanded_sum = sum_of_distances(galaxies)
    image = expand(image)
    galaxies = find_galaxies(image)
    single_expanded_sum = sum_of_distances(galaxies)
    return unexpanded_sum + n * (single_expanded_sum - unexpanded_sum)

def part_1(input_file: str) -> int:
    image = read_input(input_file)
    return sum_of_distances_after_expansion(image)

def part_2(input_file: str) -> int:
    image = read_input(input_file)
    return sum_of_distances_after_expansion(image, n=1000000-1)


if __name__ == '__main__':
    solution_part_1 = part_1('input.txt')
    print(f'Solution to part 1: {solution_part_1}')

    solution_part_2 = part_2('input.txt')
    print(f'Solution to part 2: {solution_part_2}')
