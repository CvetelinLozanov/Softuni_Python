row, columns = [int(num) for num in input().split()]

matrix = []

for _ in range(row):
    elements = list(input().split())
    matrix.append(elements)

identical_characters_counter = 0

for row in range(row - 1):
    for col in range(columns - 1):
        current_element = matrix[row][col]
        next_element = matrix[row][col + 1]
        element_below = matrix[row + 1][col]
        diagonal_element = matrix[row + 1][col + 1]

        if current_element == next_element and next_element == element_below and element_below == diagonal_element:
            identical_characters_counter += 1

print(identical_characters_counter)