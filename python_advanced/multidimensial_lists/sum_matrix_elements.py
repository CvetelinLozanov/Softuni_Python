rows, cols = [int(x) for x in input().split(', ')]

matrix = []
sum_of_numbers = 0

#test_matrix = [[int(el) for el in input().split(', ')] for i in range(int(input().split(', ')[0]))]

for _ in range(rows):
    elements = [int(x) for x in input().split(', ')]
    sum_of_numbers += sum(elements)
    matrix.append(elements)

print(sum_of_numbers)
print(matrix)
