'''
 reading mode- Denoted by r, means only read the file, dont want to do the changes.
writing mode-  denoted by w, means you can change the file.
appending mode- denoted by a, means you can append some changes, but cant do changes.
reading and writing- denoted by r+, provide all powers of reading and writing
'''


# 1st function

employee_file = open("employees.py", "r")

print(employee_file.readable())

employee_file.close()


# 2nd function

employee_file = open("employees.py", "r")

print(employee_file.read())

employee_file.close()

# 3rd function

employee_file = open("employees.py", "r")

print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())


employee_file.close()


# 4the function

employee_file = open("employees.py", "r")

print(employee_file.readlines())

employee_file.close()

# 5th function

employee_file = open("employees.py", "r")

print(employee_file.readlines()[1])

employee_file.close()

# 6th function

employee_file = open("employees.py", "r")

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
