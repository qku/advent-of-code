from day21 import *


def test_read_input():
    assert read_input('test_input.txt') == [4, 8]


def test_move():
    assert move(7, 5) == 2


def test_det():
    assert deterministic_game('test_input.txt') == 739785
