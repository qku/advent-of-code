from io import StringIO
import numpy as np


def read_input(file):
    with open(file) as f:
        lines = [i.replace('\n', '') for i in f.readlines()]
    _turns = lines.pop(-1)
    lines.pop()

    _grid = construct_grid(lines)
    _instructions = process_instructions(_turns)

    return _grid, _instructions


def construct_grid(_lines):
    width = max([len(i) for i in _lines])
    reconstructed = ''
    for i in _lines:
        i = i.replace('.', '0')
        i = i.replace('#', '1')
        for _ in range(width - len(i)):
            i += ' '
        i = i.replace(' ', '2')
        reconstructed += i + '\n'

    _grid = np.genfromtxt(StringIO(reconstructed), delimiter=1, dtype=int)
    _grid = np.pad(_grid, 1, constant_values=2)
    return _grid


def process_instructions(_turns):
    _instructions = []
    number_string = ''
    for c in _turns:
        if c in ['R', 'L']:
            if number_string:
                _instructions.append(int(number_string))
                number_string = ''
            _instructions.append(c)
        else:
            number_string += c
    if number_string:
        _instructions.append(int(number_string))
    return _instructions


def move_right(_grid, _p, n_steps):
    return _move_horizontal(_grid, _p, n_steps)


def move_left(_grid, _p, n_steps):
    _grid_flipped = np.fliplr(_grid)
    _p_flipped = (_p[0], _grid.shape[1] - _p[1] - 1)
    _p_flipped = _move_horizontal(_grid_flipped, _p_flipped, n_steps)
    _p = (_p_flipped[0], _grid.shape[1] - 1 - _p_flipped[1])
    return _p


def move_down(_grid, _p, n_steps):
    _grid_rotated = np.rot90(_grid)
    p_rot = (_grid.shape[1] - _p[1] - 1, _p[0])
    p_rot = _move_horizontal(_grid_rotated, p_rot, n_steps)
    _p = (p_rot[1], _grid.shape[1] - 1 - p_rot[0])
    return _p


def move_up(_grid, _p, n_steps):
    _grid_rotated = np.rot90(_grid)
    p_rot = (_grid.shape[1] - _p[1] - 1, _p[0])
    _grid_rot_flip = np.fliplr(_grid_rotated)
    p_rot_flip = (p_rot[0], _grid_rotated.shape[1] - p_rot[1] - 1)
    p_rot_flip = _move_horizontal(_grid_rot_flip, p_rot_flip, n_steps)
    p_rot = (p_rot_flip[0], _grid_rotated.shape[1] - p_rot_flip[1] - 1)
    _p = (p_rot[1], _grid.shape[1] - 1 - p_rot[0])
    return _p


def _move_horizontal(_grid, _p, n_steps):
    if n_steps < 0:
        raise AssertionError
    row = _grid[_p[0]]
    steps_to_obstacle = np.argmax(row[_p[1]:] > 0)
    steps_beyond = n_steps - steps_to_obstacle
    p_just_before = _p[0], _p[1] + steps_to_obstacle - 1
    if n_steps < steps_to_obstacle:
        return _p[0], _p[1] + n_steps
    elif row[_p[1] + steps_to_obstacle] == 1:
        return p_just_before
    else:
        # wrap
        first_index = np.argmax(row != 2)
        if row[first_index] == 1:
            return p_just_before
        else:
            _p = (_p[0], first_index)
            return _move_horizontal(_grid, _p, steps_beyond)


def walk_path(_grid, _instructions):
    facing = 0
    p_column = np.argmax(_grid[1] == 0)
    p = (1, p_column)
    print(p)

    for i in _instructions:
        if i == 'R':
            facing = (facing + 1) % 4
        elif i == 'L':
            facing = (facing - 1) % 4
        else:
            match facing:
                case 0:
                    p = _move_horizontal(_grid, p, i)
                case 1:
                    p = move_down(_grid, p, i)
                case 2:
                    p = move_left(_grid, p, i)
                case 3:
                    p = move_up(_grid, p, i)
        print(i, p, facing)
    return p, facing


def get_password(_p, _facing):
    return 1000 * _p[0] + 4 * _p[1] + _facing


if __name__ == '__main__':
    grid, instructions = read_input('input.txt')
    final_p, final_facing = walk_path(grid, instructions)
    password = get_password(final_p, final_facing)
    print(f'Password: {password}')
