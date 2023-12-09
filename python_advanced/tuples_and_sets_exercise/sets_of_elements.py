numbers = [int(num) for num in input().split()]

first_set = set()
second_set = set()

for _ in range(numbers[0]):
    number = int(input())
    first_set.add(number)

for _ in range(numbers[1]):
    number = int(input())
    second_set.add(number)

[print(num) for num in first_set & second_set]
