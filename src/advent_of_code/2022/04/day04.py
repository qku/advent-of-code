with open('input.txt') as f:
    lines = f.readlines()


def get_start_end(r):
    start, end = r.split('-')
    return int(start), int(end)


fully_overlapping = 0
partially_overlapping = 0
for i in lines:
    range_a, range_b = i.strip().split(',')
    start_a, end_a = get_start_end(range_a)
    start_b, end_b = get_start_end(range_b)

    if start_a >= start_b and end_a <= end_b:
        fully_overlapping += 1
    elif start_b >= start_a and end_b <= end_a:
        fully_overlapping += 1
    elif start_a <= start_b <= end_a:
        partially_overlapping += 1
    elif start_a <= end_b <= end_a:
        partially_overlapping += 1
    elif start_b <= start_a <= end_b:
        partially_overlapping += 1
    elif start_b <= end_a <= end_b:
        partially_overlapping += 1


print(fully_overlapping)
print(fully_overlapping + partially_overlapping)
