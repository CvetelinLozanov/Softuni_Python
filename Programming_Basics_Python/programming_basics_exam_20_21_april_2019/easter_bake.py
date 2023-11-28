from math import  ceil

number_of_easter_breads = int(input())

#needed_sugar = number_of_easter_breads * 0.95
#needed_flour = number_of_easter_breads * 0.75

total_used_flour = 0
total_used_sugar = 0

sugar_counter = 1
flour_counter = 1

max_used_flour = 0
max_used_sugar = 0

for _ in range(number_of_easter_breads):

    used_sugar = int(input())
    used_flour = int(input())

    total_used_flour += used_flour
    total_used_sugar += used_sugar

    if used_sugar > max_used_sugar:
        max_used_sugar = used_sugar

    if used_flour > max_used_flour:
        max_used_flour = used_flour

print(f'Sugar: {ceil(total_used_sugar / 950)}')
print(f'Flour: {ceil(total_used_flour / 750)}')
print(f'Max used flour is {max_used_flour} grams, max used sugar is {max_used_sugar} grams.')
