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
s = 'Welc&&&@@ome to Inter$$$$view 123'
clean_text = re.sub(r'[^a-zA-Z0-9 ]', '',s)
words = clean_text.split()
print(words)
final = []
for word in words:
    revserce = ''
    for char in word:
        revserce = char +revserce
    final.append(revserce)
  
print(final)





def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + recursive_sum(arr[1:])

x = [1, 2, 3, 4, 7]
result = recursive_sum(x)
print(result)   # Output: 17
