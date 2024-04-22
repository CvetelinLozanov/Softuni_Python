def numbers_searching(*args):
    start_index = min(args)
    end_index = max(args)
    unique_nums = set()
    missing_number = 0
    for num in range(start_index, end_index + 1):
        if num not in args:
            missing_number = num
        else:
            if args.count(num) > 1:
                unique_nums.add(num)

    sorted_nums = sorted(unique_nums)
    final_result = [missing_number, sorted_nums]
    return final_result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
