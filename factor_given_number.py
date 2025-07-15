# If the number is 20 then 1 to 20 which number is divisio by 20 
# Fisrt Approch 
n = 20
num = n 
result = []
for  i in range(1 ,n+1):
    if num % i == 0:
        result.append(i)

print(result)

# Second Approch Why i itretare full list till 20 i will iterate  half of the list 



# m = 20
# num = m
# result= []

# for i in range(1, num//2 +1):
#     if num %i ==0:
#         result.append(i)
# result.append(m)
# print(result)


# OPTIMAL SLUTIONS

# num = 36
# from math import sqrt

# result = []
# for i in range(1, int(sqrt(num))+1):
#     if num % i ==0:
#         result.append(i)
#         if num//i != i:
#             result.append(num//i)
# # include the i and also division data also 
# # OUTPUT = [1, 36, 2, 18, 3, 12, 4, 9, 6]
# print(result)


