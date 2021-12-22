increase_count = 0
file = open("input.txt", 'r')
array = []

for line in file:
    array.append(int(line))

for index, item in enumerate(array):
    if index != 0:
        if item > array[index-1]:
            increase_count += 1

print(increase_count)