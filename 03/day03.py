import numpy as np


def bin_to_decimal(a):
    s = ''
    for i in a:
        s += str(i)
    return int(s, base=2)


report = np.genfromtxt('input.txt', delimiter=1, dtype=int)
n = report.shape[0]

gamma_rate_bin = (report.sum(axis=0) > (n / 2)).astype(int)
eps_rate_bin = (gamma_rate_bin + 1) % 2

print(gamma_rate_bin)
print(eps_rate_bin)
print()

gamma_rate = bin_to_decimal(gamma_rate_bin)
eps_rate = bin_to_decimal(eps_rate_bin)
print(f'Gamma rate: {gamma_rate}')
print(f'Epsilon rate: {eps_rate}')
print(f'Power consumption: {gamma_rate * eps_rate}')
