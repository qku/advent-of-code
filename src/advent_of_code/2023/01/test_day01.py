from day01 import part_1, part_2, find_first_written_digit

def test_part_1():
    assert part_1('test_input.txt') == 142

def test_find_written():
    assert find_first_written_digit('7pqrstsixteen') == (6, 6)
    assert find_first_written_digit('two1nine'[::-1], rev=True) == (9, 0)

def test_part_2():
    assert part_2('test_input_part_2.txt') == 281
