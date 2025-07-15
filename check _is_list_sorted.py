# CHECK THE LIST IS SORTED OR NOT 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# TC = O(N)
# SP = O(1)

def is_sorted(nums):
    n = len(nums)
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

result = is_sorted(nums)
print(result)   # Output: True
