


def print_one_to_n(num):
    if num == 100:
        return 
    print(num)
    return print_one_to_n(num +1)

print(print_one_to_n(0))