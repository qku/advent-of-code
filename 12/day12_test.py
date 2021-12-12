from day12 import *


def test_find_all1():
    assert find_all_paths('test_input_1.txt') == 10


def test_find_all3():
    assert find_all_paths('test_input_3.txt') == 226


def test_find_all1_twice():
    assert find_all_paths('test_input_1.txt', allow_twice=True) == 36


def test_find_all3_twice():
    assert find_all_paths('test_input_3.txt', allow_twice=True) == 3509
