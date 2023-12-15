def is_index_in_matrix_length(index, value):
    return 0 <= index < value


rows, cols = [int(num) for num in input().split()]

matrix = [[x for x in input().split()] for row in range(rows)]

while True:

    command_args = input().split()

    if command_args[0] == 'END':
        break

    if not len(command_args) == 5 or not command_args[0] == 'swap':
        print('Invalid input!')
        continue

    first_row, first_col, second_row, second_col = [int(x) for x in command_args[1:]]

    if is_index_in_matrix_length(first_row, rows) or is_index_in_matrix_length(first_col, cols) \
        or is_index_in_matrix_length(second_row, rows) or is_index_in_matrix_length(second_col, cols):
        current_element = matrix[first_row][first_col]
        matrix[first_row][first_col] = matrix[second_row][second_col]
        matrix[second_row][second_col] = current_element
        [print(*el)for el in matrix]

    else:
        print('Invalid input!')






