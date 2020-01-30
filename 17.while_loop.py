i = 10
while i <= 100:
    print(i)
    i+= 10

print("done with loop")


q = input("Enter yes or no: ")

while q == "yes":
    print(input("Enter a alphabet: "))
    q = input("Do you want to use it again: ")

if q == "no":
    print("GOOD BYE!")


# 3rd type more ccmplex:



r = input("Enter yes or no: ")

while r == "yes":
    print(input("Enter a alphabet: "))
    r = input("Do you want to use it again: ")

if r == "no":
    print("GOOD BYE!")

else:
    r = (input("Either choose yes or no: "))
    while r == "yes":
        print(input("Enter a alphabet: "))
        r = input("Do you want to use it again: ")

    if r == "no":
        print("GOOD BYE!")



# type IV way:


r = input("Enter 1 or 2: ")

while r == "1":
    print(input("Enter a alphabet: "))
    r = input("Do you want to use it again: ")

if r == "2":
    print("GOOD BYE!")

while r!= 1 or r!=2:
    input("choose either 1 or 2: ")