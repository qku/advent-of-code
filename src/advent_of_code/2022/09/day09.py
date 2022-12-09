from numpy import sign


def follow(pos, head_pos):
    vertical_distance = head_pos[0] - pos[0]
    horizontal_distance = head_pos[1] - pos[1]
    if abs(vertical_distance) > 1 or abs(horizontal_distance) > 1:
        pos[0] += sign(vertical_distance)
        pos[1] += sign(horizontal_distance)


file = 'input.txt'
# file = 'test_input.txt'
with open(file) as f:
    steps = f.readlines()

# part I: 2 elements, part II: 10 elements
n_elements = 10

elements = [[0, 0] for i in range(n_elements)]
visited = [(0, 0)]

for step in steps:
    direction, n = step.strip().split()
    print(step.strip())
    for _ in range(int(n)):
        # print(f'Head: {head} - Tail: {tail}')
        # move head
        match direction:
            case 'D':
                elements[0][0] += 1
            case 'U':
                elements[0][0] -= 1
            case 'R':
                elements[0][1] += 1
            case 'L':
                elements[0][1] -= 1

        for i in range(1, n_elements):
            follow(elements[i], elements[i-1])

        # save tail position
        visited.append(tuple(elements[-1]))

unique_visited = set(visited)
print(f'Last tail element visited {len(unique_visited)} spots.')
