# retrun: It allow to return the information from the python function.
#It can be used to return any datatype, it can be string, bullien and anything.

# 1st right method

def cube(num1):
    print(num1*num1*num1)

cube(3.5)

# 2nd by use of return statement

def cube(num2):
    return num2*num2*num2

print(cube(3))

# 3rd by use of return statement

def cube(num2):
    return num2*num2*num2

result = (cube(3))
print(result)

#You can execute a fuction after return statement

def cube(num2):
    return num2*num2*num2
    print("ram")

result = (cube(15))
print(result)
