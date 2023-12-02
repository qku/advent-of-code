from day02 import part_1, part_2, min_rgb

def test_min_rgb():
    s = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
    assert min_rgb(s) == (4, 2, 6)

def test_part_1():
    assert part_1('test_input.txt') == 8

def test_part_2():
    assert part_2('test_input.txt') == 2286
