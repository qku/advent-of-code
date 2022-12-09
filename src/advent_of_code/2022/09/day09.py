from numpy import sign

file = 'input.txt'
# file = 'test_input.txt'
with open(file) as f:
    steps = f.readlines()

head, tail = [0, 0], [0, 0]
visited = [(0, 0)]

for step in steps:
    direction, n = step.strip().split()
    print(step.strip())
    for i in range(int(n)):
        print(f'Head: {head} - Tail: {tail}')
        # move head
        match direction:
            case 'D':
                head[0] += 1
            case 'U':
                head[0] -= 1
            case 'R':
                head[1] += 1
            case 'L':
                head[1] -= 1

        # move tail
        vertical_distance = head[0] - tail[0]
        horizontal_distance = head[1] - tail[1]
        if abs(vertical_distance) > 1 or abs(horizontal_distance) > 1:
            tail[0] += sign(vertical_distance)
            tail[1] += sign(horizontal_distance)

        # save tail position
        visited.append(tuple(tail))

print(f'Head: {head} - Tail: {tail}')

unique_visited = set(visited)
print(f'Tail visited {len(unique_visited)} spots.')
