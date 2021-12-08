import numpy as np


def load_just_outputs(f):
    with open(f) as file:
        out_lines = [i.split('|')[1] for i in file.readlines()]
    o = []
    for i in out_lines:
        o += i.split()
    return o


def load_complete(f):
    with open(f) as file:
        o = []
        for i in file.readlines():
            _ = i.split('|')
            unique, out = _[0], _[1]
            o.append((unique.split(), out.split()))
    return o


def count1478(o):
    n = 0
    for i in o:
        if len(i) in [2, 3, 4, 7]:
            n += 1
    return n


# total number of occurrences (* = unique)
# a 8   unique by comparing 1 & 7
# b 6 *
# c 8   can be determined once a is known
# d 7   occurs in 4
# e 4 *
# f 9 *
# g 7   can be determined once d is known

def decode_segments(unique_combos):
    encoding = {}

    total_occurrences = ''.join(i for i in unique_combos)
    for segment in 'abcdefg':
        n = total_occurrences.count(segment)
        if n == 6:
            encoding[segment] = 'b'
        elif n == 4:
            encoding[segment] = 'e'
        elif n == 9:
            encoding[segment] = 'f'

    sorted_by_l = sorted(unique_combos, key=len)
    number1, number7 = sorted_by_l[0], sorted_by_l[1]
    for segment in number7:
        if segment not in number1:
            encoding[segment] = 'a'
            continue
        if segment in number1 and segment not in encoding.keys():
            encoding[segment] = 'c'

    number4 = sorted_by_l[2]
    remaining = [i for i in number4 if i not in encoding.keys()][0]
    encoding[remaining] = 'd'

    remaining = [i for i in 'abcdefg' if i not in encoding.keys()][0]
    encoding[remaining] = 'g'

    return encoding


seven_segment_encoding = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}


def decode_number(s, encoding):
    s_decoded = ''.join(encoding[i] for i in s)
    s_decoded_sorted = ''.join(i for i in sorted(s_decoded))
    return seven_segment_encoding[s_decoded_sorted]


def decode_line(line):
    four_digits = ''
    unique, out = line
    encoding = decode_segments(unique)
    for i in out:
        four_digits += str(decode_number(i, encoding))
    return int(four_digits)


my_outputs = load_just_outputs('input.txt')
print(f'Number of unique: {count1478(my_outputs)}')

data = load_complete('input.txt')
sum_of_all = 0
for i in data:
    sum_of_all += decode_line(i)

print(f'Sum of all numbers: {sum_of_all}')
