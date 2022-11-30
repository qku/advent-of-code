import numpy as np
from day17 import *


def test_get_target():
    assert get_target_area('input.txt') == ((240, 292), (-90, -57))


def test_highest_point():
    test_target = ((20, 30), (-10, -5))
    _all = find_all(test_target)
    assert highest_point(_all) == 45


def test_find_all():
    test_target = ((20, 30), (-10, -5))
    all_test = np.loadtxt('test_input.txt', delimiter=',')
    _all = find_all(test_target)
    for (a, b) in all_test:
        print(a, b)
        assert (a, b) in _all

    # print(_all)
    # assert len(_all) == 112
