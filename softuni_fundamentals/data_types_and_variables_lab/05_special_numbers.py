number = int(input())

for cur_num in range(1, number + 1):
    number_as_str = str(cur_num)
    current_sum = 0

    for num in number_as_str:
        current_sum += int(num)

    is_special = False
    if current_sum == 5 or current_sum == 7 or current_sum == 11:
        is_special = True

    print(f"{cur_num} -> {is_special}")