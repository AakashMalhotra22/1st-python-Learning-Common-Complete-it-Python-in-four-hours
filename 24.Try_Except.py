number = int(input("Ener a number: "))
print(number)

#2.


try:
    number = int(input("Ener a number: "))
    print(number)
except:
    print("Invalid Input")


#3.

try:
    value = 10 / 0
    number = int(input("Ener a number: "))
    print(number)
except ZeroDivisionError:
    print("Divide by zero")
except ValueError:
    print("Invalid Input")

#4.

try:
    value = 10 / 0
    number = int(input("Ener a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
