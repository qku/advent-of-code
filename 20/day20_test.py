from day20 import *


def test_bright_spots():
    algorithm, image = read_input('test_input.txt')
    image = apply_algorithm_n_times(algorithm, image)
    assert bright_spots(image) == 35


def test_bright_spots_50():
    algorithm, image = read_input('test_input.txt')
    image = apply_algorithm_n_times(algorithm, image, n=50)
    assert bright_spots(image) == 3351
