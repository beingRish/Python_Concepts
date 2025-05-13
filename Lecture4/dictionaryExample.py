info = {
    "name": "Rishabh",
    "userName": "being_rish_",
    "age": 23,
    "is_adult": True,
    "marks": 94.3,
    "subjects": ["Python", "C", "Java"],
    "topics": ("dict", "set"),
    12: 24,
    56.3: 32,
    (1, 2, 3): 35
}

print(info)
print(type(info))   #<class 'dict'>
print(info["name"]) #Rishabh
print(info["userName"]) #being_rish_
print(info["age"]) #23
print(info["is_adult"]) #True
# print(info["surname"]) #Error

info["name"] = "Ritik"
print(info)

info["surname"] = "Singh"
print(info)

null_dict = {}
null_dict["name"] = "Vishwjeet"
print(null_dict)

#Nested Dictionary
student = {
    "name": "Rishabh Singh",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["math"])

#Dictionary Methods
print(list(student.keys()))     #['name', 'subjects']
print(len(student))             #2
print(list(student.values()))   #['Rishabh Singh', {'phy': 97, 'chem': 98, 'math': 95}]
print(list(student.items()))    #[('name', 'Rishabh Singh'), ('subjects', {'phy': 97, 'chem': 98, 'math': 95})]
pairs = list(student.items())
print(pairs[0])                 #('name', 'Rishabh Singh')
print(pairs[1])                 #('subjects', {'phy': 97, 'chem': 98, 'math': 95})

# print(student["name2"])     #Error
print(student.get("name"))  #Rishabh Singh
print(student.get("name2")) #None

new_dict = {"city": "Delhi", "age": 16}
student.update(new_dict)
print(student)