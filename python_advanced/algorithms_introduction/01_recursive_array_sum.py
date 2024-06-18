def calc_sum(numbers, index=0):

    if index == len(numbers) - 1:
        return numbers[index]

    return numbers[index] + calc_sum(numbers, index + 1)


nums = [int(num) for num in input().split()]
print(calc_sum(nums))