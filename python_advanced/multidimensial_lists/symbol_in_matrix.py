matrix = [[el for el in input()] for row in range(int(input()))]

searched_symbol = input()
is_element = None

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        current_element = matrix[row][col]
        if current_element == searched_symbol:
            is_element = current_element
            print(f'({row}, {col})')
            exit()

if not is_element:
    print(f'{searched_symbol} does not occur in the matrix')
