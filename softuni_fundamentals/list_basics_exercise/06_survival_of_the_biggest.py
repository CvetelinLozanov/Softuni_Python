numbers = [int(num) for num in input().split()]
numbers_to_remove = int(input())

for tries in range(numbers_to_remove):
    min_num = min(numbers)
    numbers.remove(min_num)

print(', '.join([str(num) for num in numbers]))
