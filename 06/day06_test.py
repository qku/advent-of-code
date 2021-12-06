from day06 import *

test_pop = initial_population('test_input.txt')


def test_initial_population():
    assert (test_pop == np.array([0, 1, 1, 2, 1, 0, 0, 0, 0])).all()


def test_simulate_n_days():
    assert simulate_n_days(test_pop, 80) == 5934


def test_simulate_more_days():
    assert simulate_n_days(test_pop, 256) == 26984457539
