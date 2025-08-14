
def liner_search(nums, target):
    for i in range(0,len(nums)):
        if nums[i] == target:
            return f"index is {i}"
            
    return -1            
nums = [1,3,5,6,7,4,3,5,6,9]
target = 10
print(liner_search(nums,target))

