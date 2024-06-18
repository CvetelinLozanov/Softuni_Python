def selection_sort(nums):
    for index in range(len(nums)):
        min_index = index
        for cur_index in range(index + 1, len(nums)):
            if nums[cur_index] < nums[min_index]:
                min_index = cur_index

        nums[index], nums[min_index] = nums[min_index], nums[index]

    return nums


numbers = [int(num) for num in input().split()]
print(*selection_sort(numbers))