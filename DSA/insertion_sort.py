nums = [3,2,4,7,1,2,3,6,8,9,5,4,2,1]

n = len(nums)

for i in range(1,n):
    key  = nums[i]

    j = i-1
    print(f"K-->{key} and J {j} and NUms Of J {nums[j]}")
    while j >=0 and nums[j]> key:
        nums[j+1] = nums[j]
        j -= 1
    nums[j+1] = key
print(nums) 
