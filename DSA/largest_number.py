nums = [55,22,1,44,55,77,88,45,76]
largest = nums[0]
# METHID 1
for i in nums:
    if i > largest:
        largest = i
# print(largest)

# METHOD 2

n  = len(nums)
for i in range(0,n):
    largest = max(largest, nums[i])

# print(largest)

# method 3
nums = [55,22,1,44,55,77,88,45,76]
largest = float("-inf")
for i in range(0, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
print(largest)
