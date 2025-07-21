def check_if_armstrong_number(nums):
    n = nums
    total = 0
    lod = len(str(nums))

    while n > 0:
        last_digit = n %10
        total = total + (last_digit **lod)
        print(total)
        n = n //10


check_if_armstrong_number(153)