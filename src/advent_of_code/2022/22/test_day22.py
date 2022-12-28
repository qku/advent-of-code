from day22 import *


_grid, _instructions = read_input('test_input.txt')


def test_simple_move_right():
    assert move_right(_grid, (4, 9), 2) == (4, 11)


def test_simple_move_left():
    assert move_left(_grid, (4, 10), 1) == (4, 9)


def test_blocked_move_right():
    assert move_right(_grid, (1, 9), 3) == (1, 11)


def test_blocked_move_left():
    assert move_left(_grid, (3, 11), 12) == (3, 10)


def test_wrapped_move_right():
    assert move_right(_grid, (4, 9), 10) == (4, 11)


def test_wrapped_move_left():
    assert move_left(_grid, (4, 9), 7) == (4, 10)


def test_wrapped_blocked_move_left():
    assert move_left(_grid, (1, 11), 12) == (1, 9)


def test_simple_move_down():
    assert move_down(_grid, (2, 12), 10) == (4, 12)


def test_wrapped_move_down():
    assert move_down(_grid, (5, 1), 10) == (7, 1)


def test_wrapped_move_up():
    assert move_up(_grid, (5, 1), 9) == (8, 1)


def test_some():
    assert walk_path(_grid, [1, 'L', 1, 'L', 1, 'L', 1, 'L']) == ((1, 9), 0)
