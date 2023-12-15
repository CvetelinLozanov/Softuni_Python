rows, columns = [int(num) for num in input().split(', ')]

matrix = []
sub_matrix = []

max_sum = float('-inf')

for _ in range(rows):
    elements = [int(el) for el in input().split(', ')]
    matrix.append(elements)

for row in range(rows - 1):
    for col in range(columns - 1):
        current_element = matrix[row][col]
        next_element = matrix[row][col + 1]
        element_below = matrix[row + 1][col]
        element_diagonal = matrix[row + 1][col + 1]

        current_sum = current_element + next_element + element_below + element_diagonal

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_element, next_element], [element_below, element_diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
