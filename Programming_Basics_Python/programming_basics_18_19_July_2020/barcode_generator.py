first_number = input()
second_number = input()

first_number_first_digit = int(first_number[0])
first_number_second_digit = int(first_number[1])
first_number_third_digit = int(first_number[2])
first_number_forth_digit = int(first_number[3])
second_number_first_digit = int(second_number[0])
second_number_second_digit = int(second_number[1])
second_number_third_digit = int(second_number[2])
second_number_forth_digit = int(second_number[3])

for i in range(first_number_first_digit, second_number_first_digit + 1):
    if i % 2 == 0:
        continue

    for j in range(first_number_second_digit, second_number_second_digit + 1):
        if j % 2 == 0:
            continue

        for k in range(first_number_third_digit, second_number_third_digit + 1):
            if k % 2 == 0:
                continue

            for h in range(first_number_forth_digit, second_number_forth_digit + 1):
                if h % 2 == 0:
                    continue

                else:
                    result = f'{i}{j}{k}{h}'
                    print(result, end=' ')