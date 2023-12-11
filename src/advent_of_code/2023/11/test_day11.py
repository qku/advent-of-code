from day11 import read_input, expand, find_galaxies, sum_of_distances_after_expansion, part_1

def test_read_input():
    assert read_input('test_input.txt').shape == (10, 10)

def test_expand():
    image = read_input('test_input.txt')
    assert expand(image).shape == (12, 13)

def test_find_galaxies():
    image = read_input('test_input.txt')
    assert len(find_galaxies(image)) == 9

def test_part_1():
    assert part_1('test_input.txt') == 374

def test_part_2():
    image = read_input('test_input.txt')
    assert sum_of_distances_after_expansion(image, n=9) == 1030
    assert sum_of_distances_after_expansion(image, n=99) == 8410
