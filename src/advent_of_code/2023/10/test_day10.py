from day10 import neighbor, read_grid, find_start, part_1, part_2

def test_neighbor():
    assert neighbor(2, 0, 0) == (1, 0)

def test_find_start():
    grid = read_grid('test_input.txt')
    assert find_start(grid) == (2, 0)

def test_part_1():
    assert part_1('test_input.txt') == 8

def test_part_2_2():
    assert part_2('test_input_2.txt') == 4

def test_part_2_3():
    assert part_2('test_input_3.txt') == 4

def test_part_2_4():
    assert part_2('test_input_4.txt') == 8

def test_part_2_5():
    assert part_2('test_input_5.txt') == 10
