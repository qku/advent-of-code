from day15 import *


def test_dijkstra():
    assert lowest_risk_dijkstra('test_input.txt') == 40


def test_dijkstra_heuristics():
    assert lowest_risk_dijkstra('test_input.txt', use_heuristics=True) == 40


def test_dijkstra_expanded_heuristics():
    assert lowest_risk_dijkstra('test_input.txt', n_expand=5, use_heuristics=True) == 315
