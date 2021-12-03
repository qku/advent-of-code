import numpy as np


def most_common_bit(a):
    n = a.shape[0]
    return (a.sum(axis=0) >= (n / 2)).astype(int)


def bin_to_decimal(a):
    s = ''
    for _i in a:
        s += str(_i)
    return int(s, base=2)


def rate(a, invert=False):
    rows_to_keep = a
    for i in range(a.shape[1]):
        column = rows_to_keep[:, i]
        most_common_in_column = most_common_bit(column)
        if invert:
            most_common_in_column = (most_common_in_column + 1) % 2
        rows_to_keep = rows_to_keep[most_common_in_column == column]
        n_rows_left = rows_to_keep.shape[0]
        print(n_rows_left)
        if n_rows_left == 1:
            break
    return bin_to_decimal(rows_to_keep[0])


report = np.genfromtxt('input.txt', delimiter=1, dtype=int)

gamma_rate_bin = most_common_bit(report)
eps_rate_bin = (gamma_rate_bin + 1) % 2

print(gamma_rate_bin)
print(eps_rate_bin)
print()

gamma_rate = bin_to_decimal(gamma_rate_bin)
eps_rate = bin_to_decimal(eps_rate_bin)
print(f'Gamma rate: {gamma_rate}')
print(f'Epsilon rate: {eps_rate}')
print(f'Power consumption: {gamma_rate * eps_rate}')

# Part Two


oxygen_rate = rate(report)
co2_rate = rate(report, invert=True)
print(f'Oxygen gen. rating: {oxygen_rate}')
print(f'CO2 scrubber rating: {co2_rate}')
print(f'Life support rating: {oxygen_rate * co2_rate}')
