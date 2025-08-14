a = [1, 3, 1, 5, 3, 6, 8, 9, 6, 6, 7, 8]

first = second = float('-inf')
print("first", first)
for i in a:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i

print("Second highest:", second)  # Output: 8
