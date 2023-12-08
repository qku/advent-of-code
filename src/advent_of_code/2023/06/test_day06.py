from day06 import distance, part_1, part_2

def test_distance():
    assert distance(7, 3) == 12

def test_part_1():
    assert part_1('test_input.txt') == 288

def test_part_2():
    assert part_2('test_input.txt') == 71503
