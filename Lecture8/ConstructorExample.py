class Student:
    college_name = "ABC College"    #class attribute
    
    #default constructors
    def __init__(self):
        pass

    #parameterized constructors0
    def __init__(self, name, marks):
        self.name = name    #obj attr > class attr
        self.marks = marks
    
    def welcome(self):
        print("welcome student", self.name)

    def get_marks(self):
        return self.marks


s1 = Student("Rishabh", 82)
print(s1.name, s1.marks, s1.college_name)
print(Student.college_name)
s1.welcome()
print(s1.get_marks())

s2 = Student("Ritik", 74)
print(s2.name, s1.marks, s2.college_name)
print(Student.college_name)
s2.welcome()
print(s2.get_marks())
