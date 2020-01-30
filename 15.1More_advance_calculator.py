num1 = float(input("Enter a number: "))
op = input("Enter an operation: ")
num2 = float(input("Enter another number: "))

if op == "+":
    print(num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "*":
    print(num1 * num2)

elif op == "/":
    print(num1 / num2)

else:
    print("Invalid input")


q = input("Want to use again, yes or no??")
if q == "no":
    print("okay thanks!")

while q == "yes":

    num1 = float(input("Enter a number: "))
    op = input("Enter an operation: ")
    num2 = float(input("Enter another number: "))

    if op == "+":
        print(num1 + num2)

    elif op == "-":
        print(num1 - num2)

    elif op == "*":
        print(num1 * num2)
s
    elif op == "/":
        print(num1 / num2)

    else:
        print("Invalid input")

    q = input("Want to use again, yes or no??")
    if q == "no":
        print("okay thanks!")

else:
    q = print(input("eihter choose yes or no: "))