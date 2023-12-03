from day03 import (is_number, neighbors, contains_symbol, part_1,
                   get_gear_indices, get_lines, part_2)

def test_is_number():
    assert is_number('x') == False
    assert is_number('3') == True

def test_contains_symbol():
    assert contains_symbol(['4', '.', '3']) == False
    assert contains_symbol(['4', '.', '/']) == True

def test_neighbors():
    with open('test_input.txt') as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

    assert neighbors(0, 0, lines) == ['6', '.', '.']
    assert '*' in neighbors(2, 3, lines)
    assert '3' in neighbors(1, 9, lines)

def test_part_1():
    assert part_1('test_input.txt') == 4361

def test_get_gear_indices():
    lines = get_lines('test_input.txt')
    assert get_gear_indices(lines) == [(1, 3), (4, 3), (8, 5)]

def test_part_2():
    assert part_2('test_input.txt') == 467835
