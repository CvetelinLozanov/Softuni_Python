def calc_sum(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + calc_sum(nums, idx + 1)


nums = [int(n) for n in input().split()]
print(calc_sum(nums, 0))
