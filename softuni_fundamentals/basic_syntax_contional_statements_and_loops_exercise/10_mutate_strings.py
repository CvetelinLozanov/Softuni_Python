first_string = list(input())
second_string = list(input())

for index in range(len(first_string)):
    if first_string[index] != second_string[index]:
        first_string[index] = second_string[index]
        print(''.join(first_string))