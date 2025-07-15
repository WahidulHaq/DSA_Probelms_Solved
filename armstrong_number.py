n = 153 
num = n
total = 0
lod = len(str(num))
while num > 0:
    digit = num %10
    total = total +  (digit ** lod)
    num = num // 10
if total == n:
    print(f"{n} is a armstrong number of {lod}")    
else:   
    print(f"{n} is not a armstrong number of {lod}")