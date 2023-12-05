from collections import deque

parentheses_input = deque(input())

if len(parentheses_input) % 2 != 0:
    print('NO')
    exit()

while parentheses_input:
    first_par = parentheses_input.popleft()
    last_par = parentheses_input.popleft()
    if first_par == '{' and last_par == '}':
        continue

    elif first_par == '(' and last_par == ')':
        continue

    elif first_par == '[' and last_par == ']':
        continue

    else:
        parentheses_input.appendleft(last_par)
        parentheses_input.appendleft(first_par)
        new_first_par = parentheses_input.popleft()
        new_second_par = parentheses_input.pop()

        if new_first_par == '{' and new_second_par == '}':
            continue

        elif new_first_par == '(' and new_second_par == ')':
            continue

        elif new_first_par == '[' and new_second_par == ']':
            continue

        print('NO')
        break

else:
    print('YES')


