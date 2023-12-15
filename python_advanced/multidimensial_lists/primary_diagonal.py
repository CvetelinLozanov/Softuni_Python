matrix = [[int(el) for el in input().split()] for row in range(int(input()))]

diagonal_sum = 0

for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)