str1 = "This is a string.\twe are creating it in python."
str2 = 'ApnaCollege'
str3 = """this is a string"""
str4 = "this is apnacollege's tutorial"

print(str1)

#concatenation
finalString = str1+str2
print(finalString)

#length of string
print(len(str1))

name = "Rishabh"
title = "Singh"
final_str = name + " " + title
print(final_str)

#indexing
str = 'apna college'
ch = str[3]
#str[4] = "_" #not allowed
print('zeroth element is', ch)

#slicing
print(str[1:4])         #pna
print(str[:4])          #[0:4]  #apna
print(str[5:len(str)])  #college
print(str[5:])          #[5:len(str)]  #college

#slicing with negative indexing
str = "apple"
print(str[-5:-2])   #str[-5: -2 + len(str)]   #app

#String Function
str5 = "i am studying python from Apnacollege"
print(str5.endswith('ege')) #True
print(str5.capitalize())    #I am studying python from ApnaCollege
print(str5)                 #i am studying python from ApnaCollege
str5 = str5.capitalize()    #if I want to capitalize the first char in original string.
print(str5)

print(str5.replace("o", "a"))   #I am studying pythan fram apnacallege
print(str5)

print(str5.replace("python", "javascript")) #I am studying javascript from apnacollege

print(str5.find('python'))  #14
print(str5.find('o'))  #18
print(str5.find('from'))  #21
print(str5.find("Q"))   #-1
print(str5.count("o"))  #o