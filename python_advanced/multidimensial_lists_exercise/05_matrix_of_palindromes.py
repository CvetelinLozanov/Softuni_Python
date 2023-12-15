rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        first_and_last_letter = chr(97 + row)
        middle_letter = chr(97 + row + col)
        word = first_and_last_letter + middle_letter + first_and_last_letter
        matrix[row].append(word)

[print(*row) for row in matrix]