# ------1---------
# print all even nubers from 1 to 100 using list comprehension

# even_number = [ i for i in range(1,100) if i %2 == 0]
# print(even_number)

# number = int(input("Please enter the number: "))
# ---------2---------------------------
# days_dict = {
#     1: "Monday",
#     2: "Tuesday",
#     3: "Wednesday",
#     4: "Thursday",
#     5: "Friday",
#     6: "Saturday",
#     7: "Sunday"
# }

# # This will handle the valid days or provide a default message
# print(days_dict.get(number, "Invalid number. Please enter a number between 1 and 7."))

# ----------3------------------

# Given a list of integers, write a list comprehension to generate a list of strings based on the following rules:
# If the number is divisible by 3, replace it with "Fizz"
# If divisible by 5, replace it with "Buzz"
# If divisible by both 3 and 5, replace it with "FizzBuzz"
# Otherwise, keep the number as a string
# numbers = [1, 3, 5, 15, 7, 9, 10, 12, 20, 30]

# fizzbuzz = [
#     "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else
#     "Fizz" if num % 3 == 0 else
#     "Buzz" if num % 5 == 0 else
#     str(num)
#     for num in numbers
# ]

# print(fizzbuzz)


import re
# s = 'Welc&&&@@ome to Inter$$$$view 123'
# clean_text = re.sub(r'[^a-zA-Z0-9 ]', '',s)
# words = clean_text.split()
# print(words)
# final = []
# for word in words:
#     revserce = ''
#     for char in word:
#         revserce = char +revserce
#     final.append(revserce)
  
# print(final)





# def recursive_sum(arr):
#     if len(arr) == 0:
#         return 0
#     return arr[0] + recursive_sum(arr[1:])

# x = [1, 2, 3, 4, 7]
# result = recursive_sum(x)
# print(result)   # Output: 17




# def flatten_list(nested_list):
#     result = []
#     for item in nested_list:
#         # print(item)
#         if isinstance(item, list):
#             result.extend(flatten_list(item))  # Recursively flatten
#             # print("Extend Resut", result)
#         else:
#             result.append(item)
#             print("Result", result)
#     return result

# nested = [1, [2, 3], [4, 5, 6], [[7, 8], 9], 10]
# flat = flatten_list(nested)
# print(flat)




x = [1, 2, 3, 1, 5, 3, 8, 9, 6, 4, 9, 4, 7, 2]

# Step 1: Reverse the list in-place
x.reverse()

# Step 2: Even left, Odd right (DSA style)
# i, j = 0, 0
# while j < len(x):
#     if x[j] % 2 == 0:
#         print(x[i],"---",x[j])
#         x[i], x[j] = x[j], x[i]
#         i += 1
#     j += 1

# print(x)


# FIND THE DIGIT WHOS COUNT IS 1
# from collections import Counter
# nums = [1,2,3,4,4,4,3,4,56,7,7,7]

# dict = Counter(nums)
# print(dict)

# for k, v in dict.items():
#     if v == 1:
#         print(k)
    




# Place the even digits at the end while keeping the positions of other digits unchanged.
# nums = [1, 2, 3, 4, 4, 4, 3, 4, 5, 6, 7]
# n = len(nums)
# i = 0
# for j in range(n):
#     # print(j)
#     if nums[j] % 2 != 0:  # odd
#         print(nums[i],"===",nums[j])
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
# print(nums)


# Create a dictionary that stores the count of each digit in a string.

# data = "wahidulhaqkhan"

# dict = {}
# for i in data:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] =1
# print(dict)


# list = [1,1,4,3,2,3,4]
# 1) Find the occurance of each element.
# 2) Also, find the index of each number or position.
# dit = {}
# for i in list:
#     if i in dit:
#         dit[i] +=1
#     else:
#         dit[i] = 1

# index_position = {}

# for index , num in enumerate(list):
#     if num in index_position:
#         index_position[num].append(index)
#     else:
#         index_position[num] = [index]

# print(index_position)

# Reverse list without using inbuild functions
# num = [1,1,4,3,2,3,4]
# start  = 0
# end = len(num) -1
# while start < end:
#     num[start], num[end] = num[end], num[start]
#     start +=1
#     end -=1
# print(num)


# nums = [1,2,3,4,5,6,7,8,9]

# result = []

# for i in range(0 , len(nums)):
#     if nums[i]%2 == 0:
#         result.append(nums[i]**2)
# print(result)


# 2. Create a class Animal with an attribute name and a method speak whose output is:
# "<name> makes a sound."


# 3. Create another class Dog that inherits from Animal. Override the speak method to output:
# "<name> barks."

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound."


# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} barks."

# animal = Animal("GenericAnimal")
# print(animal.speak())  # GenericAnimal makes a sound.

# dog = Dog("Buddy")
# print(dog.speak())     # Buddy barks.


# Create a flattened list from a list of lists.
# nums = [1,[2,3],4,[5,6],7,[8,9],10]


# def flattend(nums):
#     result  = []
#     for items in nums:
#         if isinstance(items , list):
#             result.extend(flattend(items))
#         else:
#             result.append(items)

#     return result

# a = flattend(nums)
# print(a)


# Crate a pandas using dictionary of list
# import pandas as pd

# data = {
#     "name":["Alice", "Bob", "Charlie", "David"],
#     "age": [25, 30, 35, 40],
#     "location": ["New York", "Los Angeles", "Chicago", "Houston"]
# }

# df = pd.DataFrame(data)
# # print(df)
# group_by = df.groupby("location")["age"].apply(list)
# # print(group_by)

# df["category"] = ["young" if age < 30 else "Adult" for age in df["age"]]

# print(df)



# TWO SUM OF TARGET 
# nums = [2, 7, 11, 15]
# target = 9
# seen = {}

# for  i , num in enumerate(nums):
#     diff = target - num
#     print("diff", diff, "iiii",i)
#     if diff in seen:
#         print([seen[diff], i])
#         break
#     seen[num] = i
    

