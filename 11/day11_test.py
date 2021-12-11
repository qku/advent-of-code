from day11 import *


def test_part_1():
    assert do_n_steps('test_input.txt', 100) == 1656


def test_part_2():
    assert first_simultaneous('test_input.txt') == 195
