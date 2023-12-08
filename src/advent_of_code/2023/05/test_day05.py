from day05 import read_input, map_seed, part_1, part_2

def test_read_input():
    seeds, maps = read_input('test_input.txt')
    assert seeds == [79, 14, 55, 13]
    assert len(maps) == 7
    assert (50, 98, 2) in maps[0]

def test_map_seed():
    map_entries = [(50, 98, 2), (52, 50, 48)]
    assert map_seed(79, map_entries) == 81
    assert map_seed(14, map_entries) == 14
    assert map_seed(55, map_entries) == 57
    assert map_seed(13, map_entries) == 13

def test_part_1():
    assert part_1('test_input.txt') == 35

def test_part_2():
    assert part_2('test_input.txt') == 46
