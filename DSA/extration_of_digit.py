def extraction_digi(nums:int):
    n = nums
    while n > 0:
        last_digit = n%10
        # print("last_digit",last_digit)
        print("=======",last_digit, end= "")
        n = n//10
        print("----",n)



extraction_digi(54321)
    