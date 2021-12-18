import numpy as np


def convert(s):
    i_min, i_max = s.split('=')[-1].split('..')
    i_min = int(i_min)
    i_max = int(i_max)
    return i_min, i_max


def get_target_area(f):
    with open(f) as file:
        line = file.readline().strip()
    x, y = line.split(',')

    x = convert(x)
    y = convert(y)

    return x, y


def possible_x_vel(target):
    x_vel_hit = []
    x_vel = 1
    x = 0
    # increase x-velocity until it overshoots
    while not x > target[0][1]:
        x_vel += 1
        x = np.arange(x_vel+1).sum()
        if x >= target[0][0]:
            x_vel_hit.append(x_vel)
    return x_vel_hit


def hit_target_y(target, initial_x_vel, initial_y_vel):
    y = 0
    y_vel = initial_y_vel

    for i in range(initial_x_vel):
        y += y_vel
        y_vel -= 1

    while y > target[1][1]:
        y += y_vel
        y_vel -= 1
    if y >= target[1][0]:
        # in target area
        return True
    else:
        # overshoot
        return False


def optimal_y_vel(target, x_vel):
    y_vel = x_vel
    last_working = -1
    while hit_target_y(target, x_vel, y_vel):
        last_working = y_vel
        y_vel += 1
    return last_working


def find_highest(target):
    x_vel_hit = possible_x_vel(target)
    x_vel_max, y_vel_max = 0, 0
    # for x_vel in x_vel_hit:
    for x_vel in range(target[0][1] + 30):
        y_vel = optimal_y_vel(target, x_vel)
        if y_vel < 0:
            continue
        print(y_vel)
        if y_vel > y_vel_max:
            y_vel_max = y_vel
            x_vel_max = x_vel
    return x_vel_max, y_vel_max


def highest_point(y_vel):
    return np.arange(y_vel+1).sum()


if __name__ == '__main__':
    _, best_y_vel = find_highest(get_target_area('input.txt'))
    # _, best_y_vel = find_highest(((20, 30), (-10, -5)))
    highest = highest_point(best_y_vel)
    print(f'Highest point: {highest}')

