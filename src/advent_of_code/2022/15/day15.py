import numpy as np


def read_input(file):
    with open(file) as f:
        readings = []
        for i in f.readlines():
            d = {}
            elements = i.split()
            d['sensor_x'] = decode_number(elements[2])
            d['sensor_y'] = decode_number(elements[3])
            d['beacon_x'] = decode_number(elements[8])
            d['beacon_y'] = decode_number(elements[9])
            d['dist'] = manhattan(d['sensor_x'], d['sensor_y'], d['beacon_x'], d['beacon_y'])
            readings.append(d)
    return readings


def decode_number(s):
    return int(s.split('=')[1].strip(',').strip(':'))


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def check_if_possible(_x, _y, _data):
    for _reading in _data:
        if manhattan(_x, _y, _reading['sensor_x'], _reading['sensor_y']) <= _reading['dist']:
            break
    else:
        return True
    return False


if __name__ == '__main__':
    data = read_input('input.txt')
    # y_of_interest = 10
    y_of_interest = 2000000

    beacons_x_on_line = []
    for i in data:
        if i['beacon_y'] == y_of_interest:
            beacons_x_on_line.append(i['beacon_x'])

    impossible_x = []
    # iterate over sensors
    for reading in data:
        dist_y = abs(reading['sensor_y'] - y_of_interest) - 1
        for i in range(reading['dist'] - dist_y):
            impossible_x.append(reading['sensor_x'] + i)
            impossible_x.append(reading['sensor_x'] - i)

    impossible_x = set(impossible_x) - set(beacons_x_on_line)
    n = len(impossible_x)
    print(f'Impossible locations: {n}')

    # part II
    # max_coordinate = 20
    max_coordinate = 4_000_000
    i_sensor = 0
    for reading in data:
        i_sensor += 1
        print(i_sensor)
        d = reading['dist'] + 2
        x_s, y_s = reading['sensor_x'], reading['sensor_y']

        a = np.arange(d)
        circle_quadrant = np.vstack([a, a[::-1]]).T
        for rel_x, rel_y in circle_quadrant:
            for x_q in [-1, 1]:
                for y_q in [-1, 1]:
                    x = (x_q * rel_x) + x_s
                    y = (y_q * rel_y) + y_s
                    if not 0 <= x <= max_coordinate or not 0 <= y <= max_coordinate:
                        continue
                    if check_if_possible(x, y, data):
                        tuning_freq = x * 4_000_000 + y
                        print(f'Found distress beacon at {x}, {y} with tuning frequency {tuning_freq}.')
