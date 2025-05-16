f = open("Lecture7/demo.txt", "w")

f.write("I want to learn Django tomorrow. 123") #Overwrites the entire file

f = open("Lecture7/demo.txt", "a")

f.write("\nThen I'll move to the Full Stack") #Adds to the file

f2 = open("Lecture7/sample.txt", "w")

f2.write("A new file will create automatically if not exists.")



f.close()
f2.close()