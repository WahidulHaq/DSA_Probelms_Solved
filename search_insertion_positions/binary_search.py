nums = [1,3,4,5,9,11,14,15,17]

target = 12


def binary_search(nums):
    n = len(nums)
    lower_bound = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low +high)//2
        if nums[mid] >= target:
            lower_bound = mid
            high = mid -1
        else:
            low = mid +1
        
    return lower_bound

print(binary_search(nums))