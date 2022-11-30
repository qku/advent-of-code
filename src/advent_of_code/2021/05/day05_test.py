import numpy as np

from day05 import *

test_lines = read_vent_file('test_input.txt')


def test_read_vent_file():
    assert read_vent_file('test_input.txt')[1, 3] == 8


def test_get_non_diagonal():
    horizontal = get_horizontal_lines(test_lines)
    vertical = get_vertical_lines(test_lines)
    assert horizontal.shape[0] + vertical.shape[0] == 6


def test_get_diagonal():
    diagonal = get_diagonal_lines(test_lines)
    assert diagonal.shape[0] == 4


def test_map():
    vent_map = draw_map(test_lines, map_size=10)
    assert evaluate_map(vent_map) == 5


def test_viz():
    vent_map = draw_map(test_lines, map_size=10)
    print()
    print_map(vent_map)


def test_map_diag():
    vent_map = draw_map(test_lines, map_size=10, consider_diagonal=True)
    assert evaluate_map(vent_map) == 12


def test_viz_diagonal():
    vent_map = draw_map(test_lines, map_size=10, consider_diagonal=True)
    print()
    print_map(vent_map)
