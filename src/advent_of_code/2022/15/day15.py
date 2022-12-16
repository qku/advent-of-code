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


if __name__ == '__main__':
    data = read_input('input.txt')
    # y_of_interest = 10
    y_of_interest = 2000000

    min_x = min([min(i['sensor_x'], i['beacon_x']) for i in data])
    max_x = max([max(i['sensor_x'], i['beacon_x']) for i in data])

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
