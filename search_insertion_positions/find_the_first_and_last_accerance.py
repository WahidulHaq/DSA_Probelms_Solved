'''nums = [1,2,3,3,3,3,4,5,6,7,8,9] #ALWAY IN SORETD MANNER
target = 3
lower = -1
high = -1
n = len(nums)

for i in range(0,n):
    if nums[i]== target:
        if lower == -1:
            lower = i
        else:
            high = i

print(lower, high)'''



#COUNT OF OCCURANCE IN SORTED ARRAY 


nums = [1,2,3,3,3,3,3,4,5,6,7,8,9,9,9,10]
target = 5

count  = 0
n = len(nums)

for i in range(0,n):
    if nums[i] ==target:
        count +=1
print(count)

