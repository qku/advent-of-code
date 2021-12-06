from day06 import *

test_pop = np.array([3, 4, 3, 1, 2], dtype=int)

def test_simulate_day():
    assert np.all(simulate_day(test_pop) == np.array([2, 3, 2, 0, 1]))
