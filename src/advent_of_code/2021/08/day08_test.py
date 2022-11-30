from day08 import *


def test_count_out():
    assert count1478(load_just_outputs('test_input.txt')) == 26


def test_decode_line():
    line = load_complete('test_input.txt')[0]
    assert decode_line(line) == 8394
