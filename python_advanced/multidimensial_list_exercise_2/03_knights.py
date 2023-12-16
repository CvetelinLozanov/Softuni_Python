from collections import deque

def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def is_on_knight(row, col, matrix, knights):
    if is_valid(row - 2, col - 1, matrix):
        if matrix[row - 2][col -1] == 'K':
            if (row, col) not in knights:
                knights[row, col] = 0
            knights[row, col] += 1

    if is_valid(row - 2, col + 1, matrix):
        if matrix[row - 2][col + 1] == 'K':
            if (row, col) not in knights:
                knights[row, col] = 0
            knights[row, col] += 1
    if is_valid(row + 2, col + 1, matrix):
        if matrix[row + 2][col + 1] == 'K':
            if (row, col) not in knights:
                knights[row, col] = 0
            knights[row, col] += 1
    if is_valid(row + 2, col - 1, matrix):
        if matrix[row + 2][col - 1] == 'K':
            if (row, col) not in knights:
                knights[row, col] = 0
            knights[row, col] += 1
    if is_valid(row - 1, col - 2, matrix):
        if matrix[row - 1][col - 2] == 'K':
            if (row, col) not in knights:
                knights[row, col] = 0
            knights[row, col] += 1
    if is_valid(row + 1, col - 2, matrix):
        if matrix[row + 1][col - 2] == 'K':
            if (row, col) not in knights:
                knights[row, col] = 0
            knights[row, col] += 1
    if is_valid(row - 1, col + 2, matrix):
        if matrix[row - 1][col + 2] == 'K':
            if (row, col) not in knights:
                knights[row, col] = 0
            knights[row, col] += 1
    if is_valid(row + 1, col + 2, matrix):
        if matrix[row + 1][col + 2] == 'K':
            if (row, col) not in knights:
                knights[row, col] = 0
            knights[row, col] += 1

    return knights


matrix = [[el for el in input()] for x in range(int(input()))]
knights = {}

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == 'K':
            knights = is_on_knight(row, col, matrix, knights)

knights = deque(sorted(knights.items(), key=lambda x: x[1], reverse=True))

counter = 0

while knights:
    test = knights.popleft()
    row_index = test[0][0]
    col_index = test[0][1]
    value = test[1]
    if value > 0:
        matrix[row_index][col_index] = '0'
        counter += 1
        knights = {}
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if matrix[row][col] == 'K':
                    knights = is_on_knight(row, col, matrix, knights)

    knights = deque(sorted(knights.items(), key=lambda x: x[1], reverse=True))

print(counter)
