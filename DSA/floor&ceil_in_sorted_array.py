
nums = [3,4,4,4,8,9,9,10,12,12,14,15]

def floor_ceil_sorted_array(nums):
    n = len(nums)
    target = 6
    floor = -1
    ceil = -1
    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2
        print("-----MID----", mid)
        if nums[mid] == target:
            return [nums[mid], nums[mid]]
        elif nums[mid] > target:
            ceil = nums[mid]
            print("---CEIL--", ceil)
            high = mid -1
        else:
            floor = nums[mid]
            print("===FLOOR===", floor)
            low = mid +1
    return [floor, ceil]

        






print(floor_ceil_sorted_array(nums=nums))



