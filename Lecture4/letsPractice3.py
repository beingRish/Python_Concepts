#Figure out a way to store 9 & 9.0 as separate values in the set.
#(You can take help of built-in data types)

#first possible solution
values = {9, "9.0"}
print(values)

#second possible solution
values2 = {
    ("float", 9.0),
    ("int", 9)
}

print(values2)