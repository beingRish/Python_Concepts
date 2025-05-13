collection = {1, 2, 3, 4, 2, "hello", "world", "world"}

print(collection)
print(type(collection)) #<class 'set'>

collection1 = {} #empty dictionary
collection2 = set()
collection2.add(1)
collection2.add(2)
collection2.add(2)
collection2.add("beingRish")
collection2.add((1,2,3))
# collection2.add([1,2,3])    #we can't add the list here because it is mutable
collection2.remove(1)
collection2.clear()
print(collection2)

collection3 = {"hello", "beingRish", "world", "coding", "python"}
print(collection3.pop())
print(collection3.pop())

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2)) #{1, 2, 3, 4}
print(set1)
print(set2)

print(set1.intersection(set2))  #{2, 3}