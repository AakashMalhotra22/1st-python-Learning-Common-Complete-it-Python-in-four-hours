print(2**3)

# Type -I

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result*base_num
    return result

print(raise_to_power(2,3))


#Type-II

ba1 = int(input("Enter bas_num: "))
ba2 = int(input("Enter pow_num: "))

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result*base_num
    return result

print(raise_to_power(ba1,ba2))