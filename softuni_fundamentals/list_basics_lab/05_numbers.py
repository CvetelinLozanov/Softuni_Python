EVEN_COMMAND = 'even'
ODD_COMMAND = 'odd'
NEGATIVE_COMMAND = 'negative'
POSITIVE_COMMAND = 'positive'

num = int(input())

numbers = [int(input()) for n in range(num)]
command = input()
result = []

for number in numbers:

    filtered_command = (
        (EVEN_COMMAND == command and number % 2 == 0) or
        (ODD_COMMAND == command and number % 2 != 0) or
        (NEGATIVE_COMMAND == command and number < 0) or
        (POSITIVE_COMMAND == command and number >= 0)
    )

    if filtered_command:
        result.append(number)

print(result)
