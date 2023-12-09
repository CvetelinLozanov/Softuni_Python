number = int(input())

longest_set = set()

for _ in range(number):
    ranges = input().split('-')
    first_set = set()
    second_set = set()
    first_range = ranges[0].split(',')
    second_range = ranges[1].split(',')

    first_range_start_num = int(first_range[0])
    first_range_end_num = int(first_range[1]) + 1

    second_range_start_num = int(second_range[0])
    second_range_end_num = int(second_range[1]) + 1

    [first_set.add(num) for num in range(first_range_start_num, first_range_end_num)]
    [second_set.add(num) for num in range(second_range_start_num, second_range_end_num)]

    current_set = first_set & second_set

    if len(longest_set) < len(current_set):
        longest_set = current_set


result = ', '.join([str(item) for item in longest_set])
longest_intersection = len(longest_set)
print(f'Longest intersection is [{result}] with length {longest_intersection}')