#WAP to find the factorial of first n natural numbers. (using for)
n = int(input("Enter a number:"))
fact = 1
for i in range(1, n+1):
    fact *= i

print("Factorial=",fact)