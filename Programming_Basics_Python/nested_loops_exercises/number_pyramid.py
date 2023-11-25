number = int(input())
current = 1
is_current_bigger_than_number = False

for num1 in range(1, number + 1):
    for num2 in range(num1):
        if current > number:
            is_current_bigger_than_number = True
            break
        print(current, end=' ')
        current += 1

    if is_current_bigger_than_number:
        break

    print()
