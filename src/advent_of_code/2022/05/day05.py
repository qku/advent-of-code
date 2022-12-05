def read_input(file_name='input.txt'):
    """
    read initial stacks
    """
    with open(file_name) as f:
        lines = f.readlines()
    stack_input = []
    i = lines.pop(0)
    while i.strip():
        stack_input.append(i)
        i = lines.pop(0)

    stack_indices = stack_input.pop()
    stack_input.reverse()

    stacks = []
    i = 1
    while True:
        try:
            k = stack_indices.index(str(i))
        except ValueError:
            break
        stacks.append([])
        for layer in stack_input:
            c = layer[k]
            if c != ' ':
                stacks[i-1].append(c)
            else:
                break
        i += 1
    return lines, stacks


def read_instruction(s):
    _, n, _, source, _, destination = s.split()
    return int(n), int(source), int(destination)


def print_top_stacks(stacks):
    top_stacks = ''
    for stack in stacks:
        top_stacks += stack[-1]

    print(top_stacks)


# part I
instructions, stacks = read_input()
for instruction in instructions:
    n, source, destination = read_instruction(instruction)
    for i in range(n):
        c = stacks[source-1].pop()
        stacks[destination-1].append(c)
print_top_stacks(stacks)

# part II
instructions, stacks = read_input()
for instruction in instructions:
    n, source, destination = read_instruction(instruction)
    temp_stack = []
    for i in range(n):
        c = stacks[source-1].pop()
        temp_stack.append(c)
    stacks[destination-1] += reversed(temp_stack)
print_top_stacks(stacks)


