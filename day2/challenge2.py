horizontal = 0
depth = 0
aim = 0
file = open('input.txt', 'r')

for line in file:
    direction, x = line.split()
    x = int(x)
    if direction == 'forward':
        horizontal += x
        depth += (aim * x)
    if direction == 'up':
        aim -= x
    if direction == 'down':
        aim += x

print(horizontal * depth)