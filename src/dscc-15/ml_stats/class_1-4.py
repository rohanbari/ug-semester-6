nums = [1, 2, 3]
same_nums = nums
print(id(nums) == id(same_nums))

same_nums = nums.copy()
same_nums[0] = 0
print(nums)
print(same_nums)

print(id(nums) == id(same_nums))

# is = memory
# == = values
