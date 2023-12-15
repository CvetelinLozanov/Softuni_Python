rows, cols = [int(num) for num in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(num) for num in input().split()])

for col in range(cols):
    sum_of_columns = 0
    for row in range(rows):
        sum_of_columns += matrix[row][col]

    print(sum_of_columns)