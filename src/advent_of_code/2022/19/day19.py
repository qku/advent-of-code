import numpy as np


def read_blueprints(file):
    with open(file) as f:
        b = []
        for i in f.readlines():
            _, i = i.split(':')
            robots = i.split('.')
            ore_for_ore = int(robots[0].split()[4])
            ore_for_clay = int(robots[1].split()[4])
            ore_for_obsidian = int(robots[2].split()[4])
            clay_for_obsidian = int(robots[2].split()[7])
            ore_for_geode = int(robots[3].split()[4])
            obsidian_for_geode = int(robots[3].split()[7])

            _costs = (
                np.array([ore_for_ore, 0, 0, 0]),
                np.array([ore_for_clay, 0, 0, 0]),
                np.array([ore_for_obsidian, clay_for_obsidian, 0, 0]),
                np.array([ore_for_geode, 0, obsidian_for_geode, 0])
            )
            b.append(_costs)
    return b


def dfs(__stock, __robots, _remaining_minutes, _costs, _robot_to_build_next=None):
    _stock = __stock.copy()
    _robots = __robots.copy()
    global global_max
    if _robot_to_build_next is not None:
        while np.any(_stock - _costs[_robot_to_build_next] < 0) and _remaining_minutes:
            _stock += _robots
            _remaining_minutes -= 1

        if _remaining_minutes:
            _stock -= _costs[_robot_to_build_next]
            _stock += _robots
            _remaining_minutes -= 1
            _robots[_robot_to_build_next] += 1
        else:
            global_max = max(global_max, _stock[3])
            return

    if _remaining_minutes:
        _results = []
        if _robots[2] > 0:
            # there is an obsidian robot
            # try for a geode robot
            dfs(_stock.copy(), _robots.copy(), _remaining_minutes, _costs, _robot_to_build_next=3)
        if _robots[1] > 0 and _robots[2] < _costs[3][2]:
            # there is a clay robot
            # try for an obsidian robot
            turns_to_build = 1 + min(0, abs((_stock - _costs[2]).min()))
            remaining_turns = _remaining_minutes - turns_to_build
            upper_bound = remaining_turns * _robots[3] + np.arange(remaining_turns + 1).sum() + _stock[3]
            if upper_bound > global_max:
                dfs(_stock.copy(), _robots.copy(), _remaining_minutes, _costs, _robot_to_build_next=2)
        for robot in [1, 0]:
            # ore and clay robots are always possible to build
            if _robots[robot] < max([c[robot] for c in _costs]):
                turns_to_build = 1 + min(0, abs((_stock - _costs[robot]).min()))
                remaining_turns = _remaining_minutes - turns_to_build
                upper_bound = remaining_turns * _robots[3] + np.arange(remaining_turns + 1).sum() + _stock[3]
                if upper_bound > global_max:
                    dfs(_stock, _robots, _remaining_minutes, _costs, _robot_to_build_next=robot)

    global_max = max(global_max, _stock[3])


if __name__ == '__main__':
    blueprints = read_blueprints('input.txt')

    results = []
    for costs in blueprints:
        global_max = 0
        dfs(np.zeros(4, dtype=int), np.array([1, 0, 0, 0]), 24, costs)
        print(global_max)
        results.append(global_max)

    quality_level = sum([(i + 1) * max_geodes for i, max_geodes in enumerate(results)])
    print(f'Quality level of best blueprint: {quality_level}')

    # part II
    product = 1
    for costs in blueprints[:3]:
        global_max = 0
        dfs(np.zeros(4, dtype=int), np.array([1, 0, 0, 0]), 32, costs)
        print(global_max)
        product *= global_max

    print(f'Product of first three blueprints: {product}')
