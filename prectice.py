num = 4444555566667777
num_str = str(num)

# # mask_number = '*'*(len(num)-4)+num[-4:]
# # print(mask_number,"-----",num[-4:])
num_list = list(num_str)

for i in range(len(num_list)-4):
    num_list[i] = "*"


print(''.join(num_list))

# nums= [1,2,3,1,4,6,79,44]

# largest_nums = nums[0]

# for i in nums:
#     if i > largest_nums:
#         largest_nums = i
# print(largest_nums)