import itertools
import math


def read_file(file):
    _flow_rate = {}
    _adj = {}
    with open(file) as f:
        for i in f.readlines():
            i = i.strip()
            a, b = i.split(';')
            valve_id = a.split()[1]
            _flow_rate[valve_id] = int(a.split('=')[1])
            try:
                _adj[valve_id] = b.split('valves ')[1].split(', ')
            except IndexError:
                _adj[valve_id] = [b.split()[-1]]
    return _flow_rate, _adj


def shortest_path(target, start, _adj):
    # dijkstra algorithm
    dist = {k: 100 for k in _adj}
    dist[start] = 0
    q = [start]
    c = start
    while q:
        new_d = dist[c] + 1
        for n in _adj[c]:
            if new_d < dist[n]:
                dist[n] = new_d
                if n not in q:
                    q.append(n)
        q.remove(c)
        if c == target:
            return dist[c]
        c = min(q, key=dist.get)


def calculate_path_result(_path, _adj, _path_costs, _flow_rate):
    minutes = 30
    released = 0
    c = _path[0]
    for v in _path[1:]:
        cost = 1 + _path_costs[v][c]
        if cost > minutes:
            break
        minutes -= cost
        released += _flow_rate[v] * minutes
        c = v
    return released


def build_shortest_path_list(_adj):
    _path_costs = {i: {} for i in _adj}
    for start in _adj:
        for target in _adj:
            _path_costs[start][target] = shortest_path(target, start, _adj)
    return _path_costs


def brute_force(start, _adj, _flow_rate):
    _flow_rate = _flow_rate.copy()
    working_valves = [k for k, v in _flow_rate.items() if v > 0]
    outcomes = []
    n_perm = math.factorial(len(working_valves))
    i = 0

    _path_costs = build_shortest_path_list(_adj)

    for path in itertools.permutations(working_valves):
        i += 1
        path = list(path)
        path.insert(0, start)
        r = calculate_path_result(path, _adj, _path_costs, _flow_rate)
        outcomes.append(r)
        print(f'Permutation {i}/{n_perm}: released {r}')
    return max(outcomes)


def dfs(current, _flow_rate, _path_costs, total_released=0, _closed_valves=None, minutes=30):
    if _closed_valves is None:
        _closed_valves = {i for i in _flow_rate}
    results = []
    for v in _closed_valves:
        rate = _flow_rate[v]
        # print(v, current)
        travel_minutes = _path_costs[v][current]
        this_minutes = minutes - travel_minutes
        if this_minutes < 1:
            continue
        this_closed_valves = _closed_valves.copy()
        this_total_released = total_released
        if v in this_closed_valves:
            # print(v)
            this_minutes -= 1
            # pot_benefit = rate * this_minutes
            this_total_released += rate * this_minutes
            this_closed_valves.remove(v)
        # print(v, this_open_valves)
        if this_minutes > 1 and this_closed_valves != set():
            # print(this_minutes, this_closed_valves)
            results.append(dfs(v, _flow_rate, _path_costs, total_released=this_total_released, _closed_valves=this_closed_valves, minutes=this_minutes))
        else:
            # print(v, this_open_valves)
            results.append(this_total_released)
    # print(_open_valves, results)
    # print(this_minutes, this_closed_valves, max(results))
    if results:
        return max(results)
    else:
        return total_released


if __name__ == '__main__':
    flow_rate, adj = read_file('input.txt')
    path_costs = build_shortest_path_list(adj)
    flow_rate = {k: v for k, v in flow_rate.items() if v > 0}

    # released_pressure = brute_force('AA', adj, flow_rate)
    # print(f'Released pressure brute force: {released_pressure}')

    released_pressure = dfs('AA', flow_rate, path_costs)
    print(f'Maximum released pressure: {released_pressure}')

    # part II
    our_minutes = 26
    n_valves = len(flow_rate)
    our_results = []
    for elephant_share in itertools.combinations(flow_rate, n_valves // 2):
        elephant_flow_rate = {k: flow_rate[k] for k in elephant_share}
        my_flow_rate = {k: flow_rate[k] for k, v in flow_rate.items() if k not in elephant_share}

        elephant_released_pressure = dfs('AA', elephant_flow_rate, path_costs, minutes=our_minutes)
        my_released_pressure = dfs('AA', my_flow_rate, path_costs, minutes=our_minutes)

        our_results.append(elephant_released_pressure + my_released_pressure)

    best_result = max(our_results)
    print(f'Maximum released pressure with an elephant to help: {best_result}')
