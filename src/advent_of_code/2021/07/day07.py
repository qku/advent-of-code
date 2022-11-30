import numpy as np
from scipy.optimize import minimize_scalar

def read_positions(f):
    p = np.loadtxt(f, delimiter=',', dtype=int)
    return p


def fuel_cost(p, target):
    return np.abs(p - target).sum()


def complex_fuel_cost(target, p):
    steps_required = np.abs(p - int(round(target)))
    step_cost = np.cumsum(np.arange(steps_required.max() + 1))
    return step_cost[steps_required].sum()


def find_optimal_target(p):
    return int(np.median(p))


def complex_find_optimal_target(p):
    res = minimize_scalar(complex_fuel_cost, args=p)
    return round(res.x)


init_positions = read_positions('input.txt')
optimal_target = find_optimal_target(init_positions)
optimal_fuel_cost = fuel_cost(init_positions, optimal_target)
complex_optimal_target = complex_find_optimal_target(init_positions)
complex_optimal_cost = complex_fuel_cost(complex_optimal_target, init_positions)
print(f'Reaching optimal target ({optimal_target}) costs {optimal_fuel_cost} fuel.')
print(f'Considering complex dynamics, ...')
print(f'... reaching ({complex_optimal_target}) costs {complex_optimal_cost} fuel.')
