def check_valid_index(num, elements):
    return 0 <= num < len(elements)


elements = input().split()
turns = 0

while True:
    command = input()

    if command == 'end':
        break

    num1, num2 = command.split()
    num1 = int(num1)
    num2 = int(num2)

    if num1 == num2 or not check_valid_index(num1, elements) or not check_valid_index(num2, elements):
        first_element = elements[0]
        turns += 1
        elements.insert(len(elements) // 2, str(f'-{turns}a'))
        elements.insert(len(elements) // 2, str(f'-{turns}a'))
        print(f'Invalid input! Adding additional elements to the board')

        continue

    if elements[num1] == elements[num2]:
        element_to_remove = elements[num1]
        elements.remove(element_to_remove)
        elements.remove(element_to_remove)
        print(f'Congrats! You have found matching elements - {element_to_remove}!')

    elif elements[num1] != elements[num2]:
        print('Try again!')

    turns += 1

    if len(elements) == 0:
        print(f'You have won in {turns} turns!')
        break

if elements:
    print(f'Sorry you lose :(\n{" ".join(elements)}')


