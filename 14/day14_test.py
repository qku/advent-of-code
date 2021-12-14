from day14 import *


def test_read_input():
    template, pair_dict = read_input('test_input.txt')
    assert template == list('NNCB')
    assert pair_dict['BH'] == 'H'


def test_step():
    template, pair_dict = read_input('test_input.txt')
    assert polymer_step(template, pair_dict) == list('NCNBCHB')


def test_part1():
    assert diff_after_n_steps('test_input.txt', 10) == 1588
