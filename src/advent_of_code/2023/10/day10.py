import matplotlib.pyplot as plt

# labelling N, E, S, W with 0, 1, 2, 3
PIPE = {
    '|': (0, 2),
    '-': (1, 3),
    'L': (0, 1),
    'J': (0, 3),
    '7': (2, 3),
    'F': (1, 2),
    '.': (),
}

def neighbor(row: int, column: int, direction: int) -> tuple[int, int]:
    if direction == 0:
        return row - 1, column
    if direction == 1:
        return row, column + 1
    if direction == 2:
        return row + 1, column
    if direction == 3:
        return row, column - 1

def read_grid(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [i.strip() for i in f.readlines()]

def find_start(grid: list[str]) -> tuple[int, int]:
    row = 0
    for row_pipes in grid:
        column = row_pipes.find('S')
        if column >= 0:
            return row, column
        row += 1

def back_direction(direction: int):
    return (direction + 2) % 4

def find_initial_direction(s_row: int, s_column: int, grid: list[str]) -> int:
    for direction in range(4):
        row, column = neighbor(s_row, s_column, direction)
        if back_direction(direction) in PIPE[grid[row][column]]:
            return direction

def find_loop(grid: list[str]) -> list[tuple[int, int]]:
    loop = [find_start(grid)]
    last_direction = find_initial_direction(loop[0][0], loop[0][1], grid)
    loop.append(
        neighbor(loop[0][0], loop[0][1], last_direction)
    )
    while not loop[-1] == loop[0]:
        connections = PIPE[grid[loop[-1][0]][loop[-1][1]]]
        for direction in connections:
            if back_direction(direction) != last_direction:
                loop.append(
                    neighbor(loop[-1][0], loop[-1][1], direction)
                )
                last_direction = direction
                break
    return loop

def plot_loop(loop: list[tuple[int, int]]) -> None:
    x = [i[0] for i in loop]
    y = [i[1] for i in loop]
    fig, ax = plt.subplots(tight_layout=True)
    ax.plot(x, y, '-', c='black')
    ax.set_aspect('equal', 'box')
    ax.axis('off')
    fig.savefig('pipes.svg', bbox_inches='tight')

def part_1(input_file: str) -> int:
    grid = read_grid(input_file)
    loop = find_loop(grid)
    plot_loop(loop)
    return len(loop) // 2

def part_2(input_file: str) -> int:
    # Sektorformel von Leibniz
    grid = read_grid(input_file)
    loop = find_loop(grid)
    area = 0
    old_x, old_y = loop.pop(0)
    for new_x, new_y in loop:
        d_x = new_x - old_x
        d_y = new_y - old_y
        area += new_x * d_y - new_y * d_x
        old_x, old_y = new_x, new_y
    return (abs(area) - len(loop)) // 2 + 1


if __name__ == '__main__':
    solution_part_1 = part_1('input.txt')
    print(f'Solution to part 1: {solution_part_1}')

    solution_part_2 = part_2('input.txt')
    print(f'Solution to part 2: {solution_part_2}')
