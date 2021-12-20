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


def x_vel_range(target):
    t_x_min, t_x_max = target[0]
    # maximal velocity: hit target in one step
    x_vel_max = t_x_max

    # minimal velocity
    x_vel_min, i = 0, 0
    while sum(range(i)) < t_x_min:
        x_vel_min = i
        i += 1

    return x_vel_min, x_vel_max


def hit_target(target, initial_x_vel, initial_y_vel):
    x, y = 0, 0
    x_vel, y_vel = initial_x_vel, initial_y_vel

    # step until overshoot
    while x <= target[0][1] and y >= target[1][0]:
        if target[0][0] <= x and target[1][1] >= y:
            return True
        x += x_vel
        y += y_vel
        if x_vel > 0:
            x_vel -= 1
        y_vel -= 1
    return False


def find_all(target):
    x_vel_min, x_vel_max = x_vel_range(target)
    y_vel_min = target[1][0]
    vel_hit = []
    for x_vel in range(x_vel_min, x_vel_max + 1):
        y_vel_max = x_vel_max
        for y_vel in range(y_vel_min, y_vel_max + 1):
            if hit_target(target, x_vel, y_vel):
                vel_hit.append((x_vel, y_vel))
    return vel_hit


def highest_point(vel_hit):
    y_vel = [i[1] for i in vel_hit]
    return np.arange(max(y_vel)+1).sum()


if __name__ == '__main__':
    _all = find_all(get_target_area('input.txt'))
    highest = highest_point(_all)

    print(f'Highest point: {highest}')
    print(f'Number of initial velocities: {len(_all)}')
