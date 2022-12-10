# file = 'test_input.txt'
file = 'input.txt'

with open(file) as f:
    instructions = f.readlines()

values = [1]
for i in instructions:
    i = i.strip()
    last = values[-1]
    values.append(last)
    if i == 'noop':
        continue
    else:
        k = int(i.split()[1])
        values.append(k + last)

signal_strength = 0
for i in range(20, 221, 40):
    val = values[i - 1]
    print(val)
    signal_strength += i * val

print(f'Signal strength: {signal_strength}')
print()

# part II
horizontal_lines = []
current_line = ''
crt_column = 0
for sprite_pos in values:
    if abs(crt_column - sprite_pos) < 2:
        current_line += '#'
    else:
        current_line += '.'
    crt_column += 1
    if crt_column == 40:
        print(current_line)
        horizontal_lines.append(current_line)
        current_line = ''
        crt_column = 0
