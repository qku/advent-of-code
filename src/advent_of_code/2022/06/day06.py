with open('input.txt') as f:
    buffer = f.read()
    buffer.strip()

buffer = list(buffer)
buffer.reverse()

# k = 4
k = 14
last = [buffer.pop() for i in range(k)]

print(last)

while buffer:
    if len(set(last)) == len(last):
        print(k)
        break

    last.append(buffer.pop())
    del last[0]
    k += 1
