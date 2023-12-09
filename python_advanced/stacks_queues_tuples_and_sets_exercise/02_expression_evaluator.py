from collections import deque

expression = deque(input().split())
numbers = deque()
operators = '*+-/'
result = int(expression.popleft())

while expression:
    element = str(expression.popleft())
    if element not in operators:
        numbers.append(element)
        continue

    elif element == '+':
        while numbers:
            result += int(numbers.popleft())

    elif element == '-':
        while numbers:
            result -= int(numbers.popleft())

    elif element == '*':
        while numbers:
            result *= int(numbers.popleft())

    elif element == '/':
        while numbers:
            result //= int(numbers.popleft())


print(result)