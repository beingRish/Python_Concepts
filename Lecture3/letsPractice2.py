#WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
list1 = ['m', 'a', 'a', 'm']

copy_list1 = list1.copy()
copy_list1.reverse()

if list1 == copy_list1:
    print("list contains a palindrome of elements")
else:
    print("list does not contain a palindrome of elements")