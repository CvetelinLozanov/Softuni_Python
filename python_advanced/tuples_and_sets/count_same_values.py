numbers = tuple(float(num) for num in input().split())

dict = {}

for num in numbers:
    if num not in dict:
        dict[num] = numbers.count(num)
        print(f'{num} - {dict[num]} times')

