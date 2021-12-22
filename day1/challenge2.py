increase_count = 0
list = []
file = open("input.txt", 'r')

for line in file:
    list.append(int(line))

for index, item in enumerate(list):
    if index != 0:
        try:
            num1 = list[index-1] + list[index] + list[index + 1]
            num2 = list[index] + list[index + 1] + list[index + 2]
        except IndexError:
            break
        if num2 > num1:
            increase_count += 1
print(increase_count)
