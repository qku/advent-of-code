from day12 import part_1, part_2, is_valid, tree

def test_is_valid():
    assert is_valid('#.#.###', (1, 1, 3)) == True
    assert is_valid('#.#####', (1, 1, 3)) == False
    assert is_valid('.#...#....###.', (1, 1, 3)) == True

def test_tree():
    assert tree('???.###', (1, 1, 3)) == 1
    assert tree('.??..??...?##.', (1, 1, 3)) == 4

def test_part_1():
    assert part_1('test_input.txt') == 21

def test_part_2():
    assert part_2('test_input.txt') == 0
