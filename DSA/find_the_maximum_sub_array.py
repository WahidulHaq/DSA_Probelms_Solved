
# OPTIMAL SOLUTIONS 
# SUB ARRAY THAT MEANS PICK ANY ARRAY FROM THE GIVEN ARRAY AND THE SUM IS MAXUM FROM THE GIVEN ARRAY 
# IS CALLED IS SUBARRAY
nums = [-2,1,-3,4-1,2,1-5,4]

def maximum_sub_array(nums):
    n  = len(nums)
    total = 0
    maximum = float("-inf")
    for i in range(0,n):
        total = total+nums[i]
        if total > maximum:
            maximum = total
        if total<0:
            total = 0
    print(maximum)
    return maximum


print(maximum_sub_array(nums))