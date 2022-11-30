from io import StringIO
import numpy as np
from scipy.spatial import distance_matrix
from scipy.spatial.distance import cdist


def read_input(f):
    with open(f) as file:
        scanners = []
        scanner_data = ''
        for line in file.readlines()[1:]:
            if line == '':
                continue
            elif 'scanner' in line and scanner_data:
                c = StringIO(scanner_data)
                a = np.loadtxt(c, delimiter=',', dtype=int)
                scanners.append(a)
                scanner_data = ''
            else:
                scanner_data += line
        c = StringIO(scanner_data)
        a = np.loadtxt(c, delimiter=',', dtype=int)
        scanners.append(a)
    return scanners


def comp_dist_matrices(a, b):
    d_a = distance_matrix(a, a)
    d_b = distance_matrix(b, b)
    a_in_b = np.isin(d_a, d_b)
    b_in_a = np.isin(d_b, d_a)

    n_matches_min = 12
    a_row_mask = a_in_b.sum(axis=1) >= n_matches_min
    b_row_mask = b_in_a.sum(axis=1) >= n_matches_min
    a_overlap_columns = d_a[:, a_in_b.sum(axis=0) >= n_matches_min]
    b_overlap_columns = d_b[:, b_in_a.sum(axis=0) >= n_matches_min]

    ordered_matches = []
    for i_a, (a, m_a) in enumerate(zip(a_overlap_columns, a_row_mask)):
        if not m_a:
            continue
        for i_b, (b, m_b) in enumerate(zip(b_overlap_columns, b_row_mask)):
            if not m_b:
                continue
            cond = np.isin(a, b)
            if cond.all():
                ordered_matches.append((i_a, i_b))
                break

    return np.array(ordered_matches)


def transform_to_reference(ref_pos, trans_pos, ordered_matches):
    a = ref_pos[ordered_matches[:, 0]][:2]
    b = trans_pos[ordered_matches[:, 1]][:2]
    flip, perm, d = iterate_over_orientations(a, b)

    print(flip, perm, d)
    return trans_pos[:, perm] * flip + d, d


def iterate_over_orientations(a, b):
    flips = [[+1, +1, +1],
             [+1, -1, -1],
             [-1, -1, +1],
             [-1, +1, -1],
             [+1, +1, -1],
             [+1, -1, +1],
             [-1, +1, +1],
             [-1, -1, -1]]
    perms = [[0, 1, 2],
             [0, 2, 1],
             [1, 0, 2],
             [1, 2, 0],
             [2, 0, 1],
             [2, 1, 0]]

    for perm in perms:
        for flip in flips:
            d = a - (b[:, perm] * flip)
            if np.all((d[0] - d[1]) == 0):
                return flip, perm, d[0]


def get_absolute_beacon_pos(scanners):
    # start with beacon positions according to scanner 0
    transformed = [scanners.pop(0)]
    scanner_pos = [np.zeros(3)]
    ref = transformed[0]

    i_t = 0
    while scanners:
        to_delete = []
        for i, scanner_data in enumerate(scanners):
            ordered_matches = comp_dist_matrices(ref, scanner_data)
            print(ref[0, 0], scanner_data[0, 0])
            n = len(ordered_matches)
            print(n)
            if n > 0:
                # print(f'Scanner {i_t:02d} -> {i:02d}: {n} matches')
                t, s = transform_to_reference(ref, scanner_data, ordered_matches)
                scanner_pos.append(s)
                transformed.append(t)
                # transformed.append(scanner_data)
                to_delete.append(i)

        for i in reversed(to_delete):
            del scanners[i]
        i_t += 1
        ref = transformed[i_t]

    beacon_pos = transformed.pop(0)
    for i in transformed:
        beacon_pos = np.append(beacon_pos, i, axis=0)
    beacon_pos = np.unique(beacon_pos, axis=0)
    print(beacon_pos)

    return beacon_pos, scanner_pos


def largest_manhattan(beacon_pos):
    d = cdist(beacon_pos, beacon_pos, metric='cityblock')
    return int(d.max())


if __name__ == '__main__':
    scanner_datasets = read_input('input.txt')
    abs_pos, abs_pos_scanners = get_absolute_beacon_pos(scanner_datasets)
    n_beacons = abs_pos.shape[0]
    print(f'Number of beacons: {n_beacons}')
    d_max = largest_manhattan(abs_pos_scanners)
    print(f'Largest scanner distance: {d_max}')
