with open('input.txt') as f:
    rucksacks = f.readlines()


def score(c):
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96


prio = 0
for i in rucksacks:
    i = i.strip()
    n = len(i)
    left = set(i[:len(i)//2])
    right = set(i[len(i)//2:])

    duplicate = (left & right).pop()
    prio += score(duplicate)

print(prio)

group_prio = 0
n = len(rucksacks)
for i in range(0, n, 3):
    a, b, c = set(rucksacks[i].strip()), set(rucksacks[i+1].strip()), set(rucksacks[i+2].strip())
    badge = (a & (b & c)).pop()
    group_prio += score(badge)

print(group_prio)
