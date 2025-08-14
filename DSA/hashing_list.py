num = [5,3,3,2,4,6,7,8,9,2]
m = [5,3,10,23,20,2,6,6,7,9]

hash_list = [0]*11

for i in num:
    hash_list[i]+=1
print(hash_list)
for j in m:
    if j<0 or j>10:
        print("0")
    else:
        print(hash_list[j])
print("hash_list",hash_list)