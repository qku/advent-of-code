from day17 import *


def test_get_target():
    assert get_target_area('input.txt') == ((240, 292), (-90, -57))


#def test_highest():
#    target = ((20, 30), (-10, -5))
#    assert find_highest(target) == (6, 9)


def test_highest_point():
    target = ((20, 30), (-10, -5))
    _, y_vel = find_highest(target)
    assert highest_point(y_vel) == 45
