'''
In case of appending, the added line will be added  in the file.
In case of write, the whole material is replaced by the line.

'''


#1st type

employee_file = open("employees1.py", "a")

print(employee_file.readable())

employee_file.close()

#2nd type

employee_file = open("employees1.py", "a")

employee_file.write("Toby - Human resources")

employee_file.close()


#3rd type

employee_file = open("employees1.py", "a")

employee_file.write("\nRam - Done")

employee_file.close()


# 4th type write mode

employee_file = open("employeew.py", "w")

employee_file.write("\nRam - Done")

employee_file.close()


# 5th write mode to crete new file

employee_file = open("ram.py", "w")

employee_file.write("\nRam - Done")

employee_file.close()

# 6th write mode to create html file

employee_file = open("ram.html", "w")

employee_file.write("<p>This is html<p>")

employee_file.close()
