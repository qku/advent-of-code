from day03 import *


def test_score():
    assert score('Z') == 52
    assert score('z') == 26


def test_find_duplicate():
    assert find_duplicate('vJrwpWtwJgWr', 'hcsFMMfFFhFp') == 'p'


def test_find_triplicate():
    assert find_triplicate(
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw') == 'Z'
