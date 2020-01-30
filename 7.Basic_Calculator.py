# 1st wrong way

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = num1 + num2
print(result)

# 2nd wrong way


num1 = input("Enter a number: ")
num2 = input("Enter anothe number: ")

result = int(num1)+ int(num2)

print(result)

# 3rd right way by use of float function
# Float function converts the all decimals in the number form.


num1 = input("Enter a number: ")
num2 = input("Enter anothe number: ")

result = float(num1)+ float(num2)

print(result)

# 4th right way

num1 = float(input("Enter a number: "))
num2 = float(input("Enter anothe number: "))

result = (num1)+ (num2)

print(result)

#Note: You can directly write print statement without writing result statement.
# For example:

num1 = float(input("Enter a number: "))
num2 = float(input("Enter anothe number: "))

print(num1+ num2)
