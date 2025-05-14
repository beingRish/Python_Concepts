#Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the number to be searched: "))
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
i = 0
found = False
while i < len(tup):
    if x==tup[i]:
        print("Number found at index:",i)
        found = True
    else:
        print("Finding...")
    i+=1
if not found:
    print("Not present")