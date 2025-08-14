num = [1,3,4,2,5,6,7,8,6,5,6,7,8,9,8,4,3,1,2,34,5]
freq_map = dict()
for n in range(1,len(num)):
    if num[n] in freq_map:
        freq_map[num[n]] += 1
    else:
        freq_map[num[n]] =1
print(freq_map)