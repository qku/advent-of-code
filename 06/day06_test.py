from day06 import *

test_pop = np.array([3, 4, 3, 1, 2], dtype=int)


def test_simulate_n_days():
    assert simulate_n_days(test_pop, 80) == 5934
