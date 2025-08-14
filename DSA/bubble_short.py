nums = [2,3,4,1,6,4,5,67,8,2,3,45,1]

n = len(nums)

# TC  = O(n2)
# SP = O(1)
# for i in range(n-2,-1,-1):
#     for j in range(0,i+1):
#         if nums[j] > nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]

# print(nums) 

# LETS TAKE SUPPOS LIST ALREADY SHORTED
# 
for i in range(n-2,-1,-1):
    # TC = O(n)
    # SP = o(1)
    is_swap = False
    for j in range(0,i+1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            is_swap = True
    if is_swap == False:
        break

print(nums) 
        
