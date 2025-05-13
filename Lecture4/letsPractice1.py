'''
Store following word meanings in a python dictionary:
    table: "a piece of furniture", "list of facts & figures"
    cat: "a small animal"

You are given a list of subjects for students.
Assume one classroom is required for 1 subject.
How many classrooms are needed by all students.
    "python", "java", "C++", "python", "javascript",
    "java", "python", "java", "C++", "C"
'''

word_with_meaning = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal"
}

subjects_for_students = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(subjects_for_students))   #5