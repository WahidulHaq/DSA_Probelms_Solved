# nums = [1, 0, 2, 4, 0, 7, 9, 7, 8, 5, 0, 3]

# temp = []
# n = len(nums)

# # Step 1: Store all non-zero elements in temp
# for i in range(n):
#     if nums[i] != 0:
#         temp.append(nums[i])

# # Step 2: Copy non-zero elements back to nums
# for j in range(len(temp)):
#     nums[j] = temp[j]  # ✅ Use j, not i

# # Step 3: Fill the rest of the array with zeros
# for k in range(len(temp), n):
#     nums[k] = 0

# print(nums)

nums = [1, 0, 4, 6, 2, 4, 0, 9, 8, 0, 7]

def move_zero_element_last(nums):
    if len(nums) <= 1:
        return nums

    i = 0
    while i < len(nums):
        if nums[i] == 0:
            break
        i += 1

    if i == len(nums):
        return nums

    j = i + 1
    while j < len(nums):
        if nums[j] != 0:   # Fix here
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

    return nums


print(move_zero_element_last(nums))


