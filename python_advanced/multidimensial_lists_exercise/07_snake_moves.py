from collections import deque

rows, cols = [int(num) for num in input().split()]

word = deque(input())
matrix = []
for row in range(rows):
    matrix.append([''] * cols)
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = word[0]
            word.rotate(-1)
        else:
            matrix[row][-1 - col] = word[0]
            word.rotate(-1)

[print(''.join(row)) for row in matrix]