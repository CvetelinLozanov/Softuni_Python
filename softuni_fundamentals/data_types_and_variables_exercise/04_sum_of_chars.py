num = int(input())

sum_of_characters = 0
for _ in range(num):
    char = input()

    sum_of_characters += ord(char)

print(f'The sum equals: {sum_of_characters}')