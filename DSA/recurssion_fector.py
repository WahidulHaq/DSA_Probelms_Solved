# Method1
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     return num * factorial(num - 1)

# print(factorial(5))  # Output: 120


# Method2
# def factorial_iterative(num):
#     result = 1
#     for i in range(2, num + 1):
#         result *= i
#     return result

# print(factorial_iterative(5))  # Output: 120


# RECURSION PRINT N X time TIME USNG HEAD  

def func(x , n):
    if x == 0:
        return
    print("n",n)
    print("X",x)
    func(x-1, n)


func(2,20)
    
# PRINT 1TO N USING RECURSION HEAD


# def func(i ,n):
#     if i > n:
#         return
#     print(i)
#     func(i+1, n)

# func(1,5)


# PRINT 1TO N USING RECURSION TAIL

# def func(i,n):
#     if i == 0:
#         return 
#     func(i-1, n)
#     print(i)

# func(5,5)
    

# Function Recusrion 

# def func(n):
#     if n==1:
#         return 1
#     return n+func(n-1)

# print(func(5    ))

# FECTORIAL USING FOOR LOOP

# def func(num):
#     result = 1
#     for i in range(1,num+1):
#         result *= i
#         print(result)
#     return result


# print(func(5))

# REVERSE USING RECURSION

# def func(nums, left, right):
#     if left>=right:
#         return
#     nums[left],nums[right] = nums[right],nums[left]
#     func(nums, left+1 , right-1)



# def revser(nums,1,8):
#     func(nums, 1,8)
#     return nums

# REVERSE USING WHILE LOOP

# nums = [3,4,1,2,3,4,5,6,5,4,3,5,7,8,9]

# right = 0
# left = 14

# while left >=right:
#     print(left,"===",right)
#     nums[left],nums[right] = nums[right],nums[left]
#     right += 1
#     left -= 1

# print(nums)


# CHECK THE STRING IS PALINDROME OR NOT USING RECURSION 

# s = 'wahid'
# n = len(s)
# left = 0
# right = n - 1
# while left <= right:
#     if s[left] != s[right]:
#         print(False)
#         break
#     left += 1
#     right -= 1
# else:
#     print(True)


# def func(s, left, right):
#     if left>= right:
#         return True
#     if s[left] != s[right]:
#         return False
#     return func(s,left+1, right -1)


# print(func(s,0,4))