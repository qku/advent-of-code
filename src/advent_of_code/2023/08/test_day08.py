from day08 import read_input, part_1, find_periodicity, part_2

def test_read_input():
    directions, desert_map = read_input('test_input.txt')
    assert directions == [0, 0, 1]
    assert len(desert_map) == 3
    assert desert_map['AAA'] == ('BBB', 'BBB')

def test_part_1():
    assert part_1('test_input.txt') == 6

def test_find_periodicity():
    directions, desert_map = read_input('test_input_part_2.txt')
    assert find_periodicity(directions, desert_map, '11A') == 2
    assert find_periodicity(directions, desert_map, '22A') == 3

def test_part_2():
    assert part_2('test_input_part_2.txt') == 6
