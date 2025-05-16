#Write a Function to find the factorial of n.(n is the parameter)
def findFactorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i

    print("factorial = ",fact)

n = int(input("Enter a number:"))
findFactorial(n)