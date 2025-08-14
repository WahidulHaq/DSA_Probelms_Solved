# REMOVE DUPLICATE VALUE FROM THE LIST
# BURTD SOLUTION
nums = [1,1,3,3,4,5,6,7,8,8,9,9,2,2,5]
n = len(nums)
dict= {}

for i in range(0,n):
    dict[nums[i]] = 0

# print(dict)

j = 0
for k in dict:
    nums[j] = k
    j+=1




final_list = []
# OTHER WAYS
for i in nums:
    if i not in final_list:
        final_list.append(i)
# print(final_list)


# OTEHR WAYS


def remove_duplicate(nums):
    n = len(nums)
    i = 0

    for j in range(1, n):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1, nums[:i + 1]


nums = [1, 1, 2, 2, 3, 4, 4, 5]
length, unique_nums = remove_duplicate(nums)

print("Unique length:", length)
print("Unique list:", unique_nums)






