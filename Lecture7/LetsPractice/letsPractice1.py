'''
Create a new file "practice.txt" using python. Add the following data in it:
    Hi everyone
    we are learning File I/O
    using Java.
    I like programming in Java.
'''

with open("Lecture7/LetsPractice/practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")