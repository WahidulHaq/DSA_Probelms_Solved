# ROTATE LIST BY 1 PLACE
# FIRST METHOD
# nums = [1,2,3,4,5,6,7,8,9]

# nums[:] = [nums[-1]] + nums[0:-1]
# print(n)

# SECOND METHOD

# nums = [1,2,3,4,5,6,7,8,9]
# temp = nums[-1]
# n = len(nums)
# for i in range(n-2,-1,-1):
#     nums[i+1] = nums[i]
# nums[0] = temp
# print(nums)



# ROTATE THE LIST BY K:
# BRTUTE SOLUTIONS
# nums = [1,2,3,4,5,6,7,8,9]
# k = 3
# n = len(nums)
# print(n)
# k = n%k

# for i in range(0,k):
#     e = nums.pop(i)
#     nums.insert(0,e)
# print(nums)


# OPTIMAL SOLUTION USING SLISING /



# nums = [1,2,3,4,5,6,7,8,9]
# k = 5

# n = len(nums)
# k =  k%n

# print(n-k)
# nums[:]  = nums[-k:]+ nums[:-k]
# print(nums)



nums = [1,2,3,4,5,6,7,8,9]
k = 5
def reverse(nums, left,right):
    while left<right:
        nums[left], nums[right] = nums[right],nums[left]
        left +=1
        right -=1
    return nums

n = len(nums)
print(reverse(nums,n-k,n-1))
print(reverse(nums,0,n-k-1))
print(reverse(nums,0,n-1))