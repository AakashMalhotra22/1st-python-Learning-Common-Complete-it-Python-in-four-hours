class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


from Student import Student

Student1 = Student("Jim", "Accounts", 3.1, False)

print(Student1.name)