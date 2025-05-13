marks = [35.8, 67.7, 43.4, 67.8, 43.9]
print(marks)
print(type(marks))  #<class 'list'>
print(len(marks))   #5
print(marks[0])     #35.8
print(marks[1])     #67.7

student = ["Rishah", 95.4, 22, "Delhi"]
print(student)  #['Rishah', 95.4, 22, 'Delhi']

student[0] = "Ritik"
print(student)  #['Ritik', 95.4, 22, 'Delhi']

# print(student[5])   #IndexError: list index out of range

#List Slicing
print(marks[1:4])       #[67.7, 43.4, 67.8]
print(marks[:4])        #[35.8, 67.7, 43.4, 67.8]
print(marks[1:])        #[67.7, 43.4, 67.8, 43.9]
print(marks[-3:-1])     #[43.4, 67.8]

#List Methods
list = [2, 1, 3]
list.append(4)
print(list) #[2, 1, 3, 4]

list.sort() #sorts in ascending order
print(list) #[1, 2, 3, 4]

list.sort(reverse=True) #sorts in descending order
print(list) #[4, 3, 2, 1]

fruits = ["banana", "litchi", "apple"]
fruits.sort()
print(fruits)    #['apple', 'banana', 'litchi']

fruits.sort(reverse=True)
print(fruits)   #['litchi', 'banana', 'apple']

chars = ['a', 'd', 'e', 'f', 'c', 'b']
chars.sort()
print(chars)    #['a', 'b', 'c', 'd', 'e', 'f']

chars.sort(reverse=True)
print(chars)    #['f', 'e', 'd', 'c', 'b', 'a']

friends = ["Rishabh", "Ritik", "Shashank", "Vishwjeet", "Suryanshu"]
friends.reverse()
print(friends)  #['Suryanshu', 'Vishwjeet', 'Shashank', 'Ritik', 'Rishabh']

friends.insert(2, "Prince")
print(friends)  #['Suryanshu', 'Vishwjeet', 'Prince', 'Shashank', 'Ritik', 'Rishabh']

list = [2, 1, 3, 1]
list.remove(1)
print(list) #[2, 3, 1]

list.pop(1)
print(list) #[2, 1]