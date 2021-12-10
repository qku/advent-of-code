from day10 import *


def test_first_illegal():
    with open('test_input.txt') as f:
        first_line = f.readlines()[2].strip()
    assert find_first_illegal_in_line(first_line) == '}'


def test_score():
    assert score_syntax_error('test_input.txt') == 26397
