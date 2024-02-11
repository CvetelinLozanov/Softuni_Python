def group_of_ten_s():
    numbers = list(map(int, input().split(', ')))
    filtered_numbers = []
    group_counter = 10

    while numbers:
        filtered_numbers = list(filter(lambda x: x <= group_counter, numbers))

        for num in filtered_numbers:
            numbers.remove(num)

        print(f"Group of {group_counter}'s: {filtered_numbers}")
        group_counter += 10


group_of_ten_s()
