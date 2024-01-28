numbers = [int(num) for num in input().split()]
middle_index = len(numbers) // 2

first_racer = numbers[:middle_index]
second_racer = numbers[middle_index + 1:]
second_racer.reverse()

first_racer_sum = 0
second_racer_sum = 0

for index in range(middle_index):
    first_racer_time = first_racer[index]
    second_racer_time = second_racer[index]

    first_racer_sum += first_racer_time
    second_racer_sum += second_racer_time

    if first_racer_time == 0:
        first_racer_sum *= 0.80

    if second_racer_time == 0:
        second_racer_sum *= 0.80

if first_racer_sum <= second_racer_sum:
    print(f'The winner is left with total time: {first_racer_sum:.1f}')
else:
    print(f'The winner is right with total time: {second_racer_sum:.1f}')

