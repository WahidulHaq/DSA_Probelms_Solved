def check_if_palindrom(nums: int):
    original = nums
    n = nums
    result = 0
    while n > 0:
        last_digit = n % 10
        result = (result * 10) + last_digit
        n = n // 10
    print(result)
    if original == result:
        return True
    else:
        return False

# Test
nums = 121
print(check_if_palindrom(nums))  # Output: True




def check_if_palindrome_string(s: str):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
print(check_if_palindrome_string("Madam"))
