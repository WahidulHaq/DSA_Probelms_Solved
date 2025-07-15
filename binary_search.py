# BINARY SEARCH YOU HAVE TO GIVEN ONE TARGET
# VALUE YOU NEED TO FIND THE VALUE IN THE LSIT IF YOU GOT THE NUMBER RTURN THEIRE INDEX ELSE -1
nums = [2,4,6,7,9,11,18,19]
target_value = 7

def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    while low<= high:
        mid = (low + high)//2
        if nums[mid]== target:
            return mid
        elif nums[mid]< high:
            low = mid+1
        else:
            high = mid -1
    return -1



print(binary_search(nums, target_value))
    
