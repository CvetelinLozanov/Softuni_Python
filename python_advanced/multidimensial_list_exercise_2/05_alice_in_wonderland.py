def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


n = int(input())

matrix = []
alice_start_row = None
alice_start_col = None
directions = {
    'up': lambda a, b: [a - 1, b + 0],
    'down': lambda a, b: [a + 1, b + 0],
    'right': lambda a, b: [a + 0, b + 1],
    'left': lambda a, b: [a + 0, b - 1]
}
tea_bags = 0
are_bags_collected = False

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'A':
            alice_start_row = row
            alice_start_col = col

matrix[alice_start_row][alice_start_col] = '*'

while True:
    direction = input()

    if direction in directions:
        alice_start_row = directions[direction](alice_start_row, alice_start_col)[0]
        alice_start_col = directions[direction](alice_start_row, alice_start_col)[1]
        if is_valid(alice_start_row, alice_start_col, matrix):
            if matrix[alice_start_row][alice_start_col] == 'R':
                print('Alice didn\'t make it to the tea party.')
                matrix[alice_start_row][alice_start_col] = '*'
                break

            current_value = matrix[alice_start_row][alice_start_col]
            matrix[alice_start_row][alice_start_col] = '*'
            if current_value.isdigit():
                tea_bags += int(current_value)
        else:
            print('Alice didn\'t make it to the tea party.')
            break

        if tea_bags >= 10:
            print('She did it! She went to the party.')
            break

[print(*el) for el in matrix]