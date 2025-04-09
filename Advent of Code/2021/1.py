nums = list(map(int, open('input')))
print(sum(b > a for a, b in zip(
    map(sum, zip(nums, nums[1:], nums[2:])),
    map(sum, zip(nums[1:], nums[2:], nums[3:]))
)))
