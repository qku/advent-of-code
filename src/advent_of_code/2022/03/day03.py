with open('input.txt') as f:
    rucksacks = f.readlines()


def score(c):
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96


def find_duplicate(a, b):
    for k in a:
        if k in b:
            return k


def find_triplicate(a, b, c):
    for k in a:
        if k in b and k in c:
            return k


prio = 0
for i in rucksacks:
    i = i.strip()
    n = len(i)
    left = i[:len(i)//2]
    right = i[len(i)//2:]

    assert len(left) == len(right)
    duplicate = find_duplicate(left, right)
    prio += score(duplicate)

print(prio)

group_prio = 0
n = len(rucksacks)
for i in range(0, n, 3):
    badge = find_triplicate(
        rucksacks[i],
        rucksacks[i+1],
        rucksacks[i+2])
    group_prio += score(badge)

print(group_prio)
