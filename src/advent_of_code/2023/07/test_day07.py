from day07 import map_to_numbers, hand_type, part_1, part_2

def test_map_to_numbers():
    assert map_to_numbers('32T3K') == [1, 0, 8, 1, 11]

def test_hand_type():
    assert hand_type('32T3K') == 1
    assert hand_type('T55J5') == 3
    assert hand_type('TTT55') == 4
    assert hand_type('KKKKK') == 6

    assert hand_type('32TJK', joker=True) == 1
    assert hand_type('T554J', joker=True) == 3
    assert hand_type('TTJ55', joker=True) == 4
    assert hand_type('KKKJK', joker=True) == 6

def test_part_1():
    assert part_1('test_input.txt') == 6440

def test_part_2():
    assert part_2('test_input.txt') == 5905
