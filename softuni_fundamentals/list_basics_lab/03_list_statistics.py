num = int(input())

positive_nums = []
negative_nums = []

for _ in range(num):
    number = int(input())
    if number < 0:
        negative_nums.append(number)
    else:
        positive_nums.append(number)

print(positive_nums)
print(negative_nums)
print(f'Count of positives: {len(positive_nums)}')
print(f'Sum of negatives: {sum(negative_nums)}')
