def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


matrix = [[int(x) for x in input().split()] for num in range(int(input()))]

while True:
    command = input().split()

    if command[0] == 'END':
        break

    row, col, value = [int(num) for num in command[1:]]

    if command[0].upper() == 'ADD':
        if is_valid(row, col, matrix):
            matrix[row][col] += value
        else:
            print('Invalid coordinates')

    elif command[0].upper() == 'SUBTRACT':
        if is_valid(row, col, matrix):
            matrix[row][col] -= value
        else:
            print('Invalid coordinates')


[print(*num) for num in matrix]