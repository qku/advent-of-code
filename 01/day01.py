import numpy as np

readings = np.loadtxt('input.txt')
n_readings = readings.size
change = np.diff(readings)
is_increasing = change > 0
n_is_increasing = np.count_nonzero(is_increasing)

print(f'Total readings: {n_readings}')
print(f'Increasing: {n_is_increasing}')

# Part II

window_sums = []
for i in range(3):
    crop = (n_readings - i) % 3
    print(f'Cropping {crop} readings.')

    if crop != 0:
        relevant_readings = readings[i:-crop]
    else:
        relevant_readings = readings[i:]

    sliding_windows = relevant_readings.reshape(-1, 3)

    window_sum = sliding_windows.sum(axis=1)
    window_sums.append(window_sum)

n_windows = np.sum([a.size for a in window_sums])
all_windows = np.empty(n_windows)

for i, a in enumerate(window_sums):
    all_windows[i::3] = a

change = np.diff(all_windows)
is_increasing = change > 0
n_is_increasing_window = np.count_nonzero(is_increasing)

print(f'Sliding windows: {n_windows}')
print(f'Increasing sliding windows: {n_is_increasing_window}')




