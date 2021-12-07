from day07 import *


def test_read_positions():
    assert read_positions('test_input.txt')[2] == 2


test_positions = read_positions('test_input.txt')


def test_fuel_cost():
    assert fuel_cost(test_positions, 1) == 41


def test_find_optimal():
    assert find_optimal_target(test_positions) == 2
