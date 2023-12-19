from day13 import read_input, find_horizontal_split, part_1, part_2

def test_read_input():
    patterns = read_input('test_input.txt')
    assert len(patterns) == 2
    assert patterns[0].shape == (7, 9)

def test_horizontal_split():
    patterns = read_input('test_input.txt')
    assert find_horizontal_split(patterns[0]) == -1
    assert find_horizontal_split(patterns[0].T) == 5
    assert find_horizontal_split(patterns[1]) == 4

def test_smudged():
    patterns = read_input('test_input.txt')
    assert find_horizontal_split(patterns[0], smudged=True) == 3
    assert find_horizontal_split(patterns[1], smudged=True) == 1

def test_part_1():
    assert part_1('test_input.txt') == 405

def test_part_2():
    assert part_2('test_input.txt') == 400
