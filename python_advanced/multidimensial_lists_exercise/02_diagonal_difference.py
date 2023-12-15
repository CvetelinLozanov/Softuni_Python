matrix = [[int(el) for el in input().split(' ')] for row in range(int(input()))]

primary_diagonal_numbers = []
secondary_diagonal_numbers = []

sum_primary_diagonal = 0
sum_right_diagonal = 0

for index in range(len(matrix)):
    sum_primary_diagonal += matrix[index][index]
    sum_right_diagonal += matrix[index][len(matrix) - index - 1]

print(abs(sum_primary_diagonal - sum_right_diagonal))