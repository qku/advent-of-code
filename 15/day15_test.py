from day15 import *


def test_dijkstra():
    assert lowest_risk_dijkstra('test_input.txt') == 40


def test_dijkstra_expanded():
    assert lowest_risk_dijkstra('test_input.txt', n_expand=5) == 315
