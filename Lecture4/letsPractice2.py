#WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#Start with an empty dictionary & add one by one.
#Use subject name as key & marks as value.
marks = {}

marks.update({"phy": int(input("enter phy: "))})
marks.update({"chem": int(input("enter chem: "))})
marks.update({"math": int(input("enter math: "))})

print(marks)