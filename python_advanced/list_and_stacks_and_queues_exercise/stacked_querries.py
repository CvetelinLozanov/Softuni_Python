from collections import deque
from sys import maxsize


def check_max_value_in_stack(max_value, value):
    return max_value < value


def check_min_value_in_stack(min_value, value):
    return min_value > value


num = int(input())
stack = deque()
max_value = -maxsize
min_value = maxsize

for _ in range(num):
    command = input().split()

    if len(command) == 2:
        stack.append(int(command[1]))

    else:

        if len(stack) == 0:
            continue

        if command[0] == '2':
            stack.pop()

        elif command[0] == '3':

            for index in range(len(stack)):
                number = int(stack[index])

                if check_max_value_in_stack(max_value, number):
                    max_value = number

            print(max_value)

        elif command[0] == '4':

            for index in range(len(stack)):
                number = int(stack[index])

                if check_min_value_in_stack(min_value, number):
                    min_value = number

            print(min_value)

while len(stack) != 1:

    print(stack.pop(), end=', ')

print(stack.pop())
