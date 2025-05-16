#Write a Function to print the element of a list in a single line. (list is the parameter)
def printElementOfListInSingleLine(list_data):
    for item in list_data:
        print(item, end=" ")    

printElementOfListInSingleLine([35, "Rishabh", 35.6, [1,2,3,4,5]])