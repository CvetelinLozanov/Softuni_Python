from collections import deque


def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def explosion(damage, row, col, matrix):
    if is_valid(row - 1, col, matrix) and matrix[row - 1][col] > 0:
        matrix[row - 1][col] -= damage

    if is_valid(row - 1, col - 1, matrix) and matrix[row - 1][col - 1] > 0:
        matrix[row - 1][col - 1] -= damage

    if is_valid(row - 1, col + 1, matrix) and matrix[row - 1][col + 1] > 0:
        matrix[row - 1][col + 1] -= damage

    if is_valid(row + 1, col, matrix) and matrix[row + 1][col] > 0:
        matrix[row + 1][col] -= damage

    if is_valid(row + 1, col + 1, matrix) and matrix[row + 1][col + 1] > 0:
        matrix[row + 1][col + 1] -= damage

    if is_valid(row + 1, col - 1, matrix) and matrix[row + 1][col - 1] > 0:
        matrix[row + 1][col - 1] -= damage

    if is_valid(row, col - 1, matrix) and matrix[row][col - 1] > 0:
        matrix[row][col - 1] -= damage

    if is_valid(row, col + 1, matrix) and matrix[row][col + 1] > 0:
        matrix[row][col + 1] -= damage

    matrix[row][col] -= damage

    return matrix


matrix = [[int(el) for el in input().split()] for _ in range(int(input()))]
bomb_coordinates = deque([int(x) for el in input().split() for x in el.split(',')])

while bomb_coordinates:
    bomb_row = bomb_coordinates.popleft()
    bomb_col = bomb_coordinates.popleft()

    bomb_damage = matrix[bomb_row][bomb_col]

    if is_valid(bomb_row, bomb_col, matrix) and bomb_damage > 0:
        matrix = explosion(bomb_damage, bomb_row, bomb_col, matrix)


alive_matrix = [x for el in matrix for x in el if x > 0]

print(f'Alive cells: {len(alive_matrix)}')
print(f'Sum: {sum(alive_matrix)}')
[print(*el) for el in matrix]