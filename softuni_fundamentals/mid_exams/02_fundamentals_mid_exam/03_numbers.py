numbers = list(map(int, input().split()))

average = sum(numbers) / len(numbers)

greater_than_average = list(filter(lambda num: num > average, numbers))
greater_than_average.sort(reverse=True)
if greater_than_average:
    print(' '.join(map(str, greater_than_average[:5])))
else:
    print('No')
