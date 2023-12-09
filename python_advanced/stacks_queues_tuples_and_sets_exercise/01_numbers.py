first_set = set([int(num) for num in input().split()])
second_set = set([int(num) for num in input().split()])

n = int(input())
is_subset = False

for _ in range(n):
    command = input().split()

    if command[0] == 'Add':
        set = command[1]
        if set == 'First':
            first_set.update([int(num) for num in command[2:]])

        elif set == 'Second':
            second_set.update([int(num) for num in command[2:]])

    elif command[0] == 'Remove':
        set = command[1]
        items_to_remove = [int(num) for num in command[2:]]
        if set == 'First':
            first_set.difference_update(items_to_remove)

        elif set == 'Second':
            second_set.difference_update(items_to_remove)
    elif command[0] == 'Check':
        print(first_set < second_set or second_set < first_set)


print(', '.join([str(item) for item in sorted(first_set)]))
print(', '.join([str(item) for item in sorted(second_set)]))