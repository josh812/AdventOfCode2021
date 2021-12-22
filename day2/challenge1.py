horizontal = 0
depth = 0
file = open('input.txt', 'r')

for line in file:
    direction, x = line.split()
    x = int(x)
    if direction == 'forward':
        horizontal += x
    elif direction == 'down':
        depth += x
    elif direction == 'up':
        depth -= x

print(horizontal * depth)