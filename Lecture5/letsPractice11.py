# WAP to find the sum of first n natural numbers. (using while)
n = int(input("Enter a number: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print("Sum =",sum)