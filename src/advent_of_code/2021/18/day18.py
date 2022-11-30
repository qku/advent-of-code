from copy import deepcopy


def read_input(f):
    numbers = []
    with open(f) as file:
        for line in file:
            numbers.append(eval(line))
    return numbers


def add_numbers(numbers):
    _sum = numbers[0]
    for number in numbers[1:]:
        _sum = [_sum, number]
        _sum = reduce(_sum)
    return _sum


def snail_split(number):
    for lr, content in enumerate(number):
        if type(content) == int:
            if content > 9:
                # split
                a, b = divmod(content, 2)
                number[lr] = [a, a + b]
                return True, number
        else:
            split_performed, number[lr] = snail_split(content)
            if split_performed:
                return True, number
            else:
                continue
    return False, number


def explosion(number, level):
    level += 1
    explosion_pair = None
    for lr, content in enumerate(number):
        if type(content) != list:
            continue

        if level == 4:
            # pairs about to explode should only contain regulars
            assert type(content[0]) == type(content[1]) == int

            explosion_pair = number[lr]
            number[lr] = -1
            break

        # check for explosions on a lower level
        else:
            explosion_pair, number[lr] = explosion(content, level)
            if explosion_pair:
                break

    return explosion_pair, number


def explosion_add(explosion_pair, number):
    number_string = str(number)
    i_explosion = number_string.index('-1')
    number_string = number_string.replace('-1', '0')

    for i in range(i_explosion + 1, len(number_string)):
        v = number_string[i]
        k = 0
        while v in '0123456789':
            v = number_string[i+k+1]
            k += 1
        if k:
            regular = int(number_string[i:i+k])
            number_string = (number_string[:i]
                             + str(regular + explosion_pair[1])
                             + number_string[i+k:])
            break

    for i in reversed(list(range(i_explosion))):
        v = number_string[i]
        k = 0
        while v in '0123456789':
            v = number_string[i+k-1]
            k -= 1
        if k:
            regular = int(number_string[i+k+1:i+1])
            number_string = (number_string[:i+k+1]
                             + str(regular + explosion_pair[0])
                             + number_string[i+1:])
            break

    return eval(number_string)


def reduce(number):
    explosion_performed, split_performed = True, True
    while explosion_performed or split_performed:
        explosion_pair, number = explosion(number, 0)
        if explosion_pair:
            number = explosion_add(explosion_pair, number)
            explosion_performed = True
            continue
        else:
            explosion_performed = False
        split_performed, number = snail_split(number)
    return number


def magnitude(number):
    left, right = number[0], number[1]
    if type(left) == int:
        m_left = left
    else:
        m_left = magnitude(left)
    if type(right) == int:
        m_right = right
    else:
        m_right = magnitude(right)
    return 3 * m_left + 2 * m_right


def max_magnitude(numbers):
    res = 0
    for a in numbers:
        for b in numbers:
            if a == b:
                continue
            summands = deepcopy([a, b])
            _sum = add_numbers(summands)
            m = magnitude(_sum)
            res = max(res, m)
    return res


if __name__ == '__main__':
    snail_numbers = read_input('input.txt')
    hw_mag = magnitude(add_numbers(snail_numbers))
    hw_mag_max = max_magnitude(snail_numbers)
    print(f'Magnitude of result: {hw_mag}')
    print(f'Maximum magnitude: {hw_mag_max}')
