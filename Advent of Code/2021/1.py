nums = list(map(int, open('input')))
print(sum(b > a for a, b in zip(nums, nums[1:])))
