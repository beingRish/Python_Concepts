#for loop with lists
nums = [1, 2, 3, 4, 5]
for value in nums:
    print(value)

vaggies = ["potato", "bringal", "ladyfinger", "cucumber"]
for val in vaggies:
    print(val)

#for loop with tupples
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for num in tup:
    print(num)

#for loop with strings
str1 = "apnacollege"
for char in str1:
    print(char)

#for loop with else
str2 = "Rishabh Singh"
for char in str2:
    if(char == 'b'):
        print("b found")
        break
    print(char)
else:
    print("Loop Ends")