# BRUTH SOLUTIONS
# nums = [5,43,23,12,55,66,35,67,32,45,90]

# largest = float('inf')
# second = float('-inf')
# n = len(nums)
# for i in range(0,n):
#     largest = max(largest, nums[i])
# for i in range(0,n):
#     if nums[i]> second and nums[i]!= largest:
#         second = nums[i]
# print("second", second)
# OPTIMAL SOLUTIONS

nums = [55,12,23,67,40,89,98,99]
largest = float("-inf")
second = float("-inf")
n  = len(nums)
for i in range(0,n): #TIME COMPLEXITY  = O(N) AND SPACE COMPLEXITY = O(1)
    if nums[i] > largest:
        # print(nums[i])
        second = largest
        largest = nums[i]
        # print("second", second)
        # print("largest",largest)
    elif nums[i]> second and nums[i] != largest:
        second = nums[i]
print(second)
