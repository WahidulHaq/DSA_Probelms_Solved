nums = 54545445

def count_of_digit(nums:int):
    n = nums
    count = 0
    while n > 0:
        # print(number)
        count +=1
        n = n // 10
    print(count)
    
          
count_of_digit(nums=nums)
