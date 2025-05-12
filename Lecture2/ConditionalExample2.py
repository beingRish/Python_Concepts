"""
Grade students baseed on marks
    marks >= 90, grade = "A"
    90 > marks >= 80, grade = "B"
    80 > marks >= 70, grade = "C"
    70 > marks, grade = "D"
"""
marks = int(input("Enter marks:"))
if marks >= 90:
    grade = "A"
elif 90 > marks and marks >= 80:
    grade = "B"
elif 80 > marks and marks >= 70:
    grade = "C"
elif 70 > marks:
    grade = "D"

print("grade of the student ->", grade)