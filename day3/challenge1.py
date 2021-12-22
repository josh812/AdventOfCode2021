gamma = 0
epsilon = 0
binary_list_gamma = []
binary_string_gamma = ''
binary_string_epsilon = ''

for i in range(12):
    file = open('input.txt', 'r')

    one_count = 0
    zero_count = 0

    for line in file:
        if line[i] == '1':
            one_count += 1
        elif line[i] == '0':
            zero_count += 1
        
    if one_count > zero_count:
        binary_list_gamma.append(1)
    elif zero_count > one_count:
        binary_list_gamma.append(0)

    file.close()

for value in binary_list_gamma:
    binary_string_gamma += str(value)

for letter in binary_string_gamma:
    if letter == '1':
        binary_string_epsilon += '0'
    elif letter == '0':
        binary_string_epsilon += '1'

binary_string_gamma = int(binary_string_gamma, 2)
binary_string_epsilon = int(binary_string_epsilon, 2)

print(binary_string_gamma * binary_string_epsilon)