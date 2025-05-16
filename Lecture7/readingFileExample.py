f = open("Lecture7/demo.txt", "r")
# data = f.read()
# data = f.read(5)    #reads only 5 characters

# print(data)
# print(type(data))   #<class 'str'>


line1 = f.readline()    #reads one line at a time.
print(line1)            #I am learning

line2 = f.readline()    #reads one line at a time.
print(line2)            #Python from ApnaCollege

line3 = f.readline()
print(line3)            #

f.close()