# PALINDROME
n = 121
num = n 
result = 0
while num > 0:
    ld = num %10 
    print("-LD--",ld)
    result = (result*10) +ld
    print("result:", result*10)
    num = num //10
    # print("num:", num)
if n == result:
    print("Yes")
else:
    print("NO")