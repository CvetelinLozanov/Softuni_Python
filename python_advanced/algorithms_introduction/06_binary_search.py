def binary_search(nums, target_num):

    start_index = 0
    end_index = len(nums) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        mid_num = nums[mid_index]

        if mid_num == target_num:
            return mid_index

        if mid_num < target_num:
            start_index = mid_index + 1

        if mid_num > target_num:
            end_index = mid_index - 1

    return -1


numbers = [int(num) for num in input().split()]
searched_num = int(input())
print(binary_search(numbers, searched_num))

#1 2 3 4 5 6 7 8
