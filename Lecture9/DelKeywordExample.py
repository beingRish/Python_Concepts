class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Rishabh")
print(s1.name)

del s1
print(s1.name) #Error