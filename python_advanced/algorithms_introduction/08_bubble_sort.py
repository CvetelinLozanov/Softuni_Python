def bubble_sort(nums):
    is_sorted = False
    s = 0

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(nums) - s):
            if nums[j - 1] > nums[j]:
                is_sorted = False
                nums[j - 1], nums[j] = nums[j], nums[j - 1]

        s += 1

    return nums


numbers = [int(num) for num in input().split()]
print(*bubble_sort(numbers))