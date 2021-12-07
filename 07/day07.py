import numpy as np


def read_positions(f):
    p = np.loadtxt(f, delimiter=',', dtype=int)
    return p


def fuel_cost(p, target):
    return np.abs(p - target).sum()


def find_optimal_target(p):
    return int(np.median(p))


init_positions = read_positions('input.txt')
optimal_target = find_optimal_target(init_positions)
optimal_fuel_cost = fuel_cost(init_positions, optimal_target)
print(f'Reaching optimal target ({optimal_target}) costs {optimal_fuel_cost} fuel.')
