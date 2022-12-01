with open('input.txt') as f:
    lines = f.readlines()

lines = [i.strip() for i in lines]


s = 0
elf_sums = []
for i in lines:
    if i:
        s += int(i)
    else:
        elf_sums.append(s)
        s = 0

max_sum = max(elf_sums)
print(max_sum)

elf_sums.sort()
sum_of_three = sum(elf_sums[-3:])
print(sum_of_three)
