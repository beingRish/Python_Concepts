'''
Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average.
'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Hii",self.name,"your avg score is:",sum/len(self.marks))

s1 = Student("Rishabh", [34, 45, 67, 43])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()