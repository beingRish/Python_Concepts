#Search for a number x in this tuple using for loop
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a number: "))
idx = 0
for num in nums:
    if num == x:
        print("Number Found at",idx)
        break
    idx += 1
else:
    print("Number not Found")
    