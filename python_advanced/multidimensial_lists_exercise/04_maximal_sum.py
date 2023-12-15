rows, columns = [int(num) for num in input().split()]

matrix = []
max_sum = float('-inf')
max_row_index = 0
max_col_index = 0

for _ in range(rows):
    elements = [int(num) for num in input().split()]
    matrix.append(elements)

for row in range(rows - 2):
    for col in range(columns - 2):
        current_sum = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                current_sum += matrix[r][c]

        if current_sum > max_sum:
            max_sum = current_sum
            max_row_index = row
            max_col_index = col


print(f'Sum = {max_sum}')

sub_matrix = [matrix[row][max_col_index:max_col_index + 3] for row in range(max_row_index, max_row_index + 3)]
[print(*row) for row in sub_matrix]
