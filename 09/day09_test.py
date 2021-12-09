import numpy as np
from day09 import *


def test_load_and_pad():
    assert pad_map(load_map('test_input.txt'))[1, 1] == 2


test_map = pad_map(load_map('test_input.txt'))


def test_find_minimum_values():
    assert total_risk_value(find_minimum_values(test_map)) == 15
