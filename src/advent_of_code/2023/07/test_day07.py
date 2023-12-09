from day07 import map_to_numbers, hand_type, part_1, part_2

def test_map_to_numbers():
    assert map_to_numbers('32T3K') == [1, 0, 8, 1, 11]

def test_hand_type():
    assert hand_type('32T3K') == 1
    assert hand_type('T55J5') == 3

def test_part_1():
    assert part_1('test_input.txt') == 6440

def test_part_2():
    assert part_2('test_input.txt') == 0
