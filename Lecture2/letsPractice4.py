#WAP to find the greatest of 4 numbers entered by the user.
firstNumber = int(input("Etner the first number:"))
secondNumber = int(input("Etner the second number:"))
thirdNumber = int(input("Etner the third number:"))
fourthNumber = int(input("Etner the fourth number:"))

if (firstNumber >= secondNumber) and (firstNumber >= thirdNumber) and (firstNumber >= fourthNumber):
    print(firstNumber, "is the greatest")
elif (secondNumber >= thirdNumber):
    print(secondNumber, "is the greatest")
elif (thirdNumber >= fourthNumber):
    print(thirdNumber, "is the greatest")
else:
    print(fourthNumber, "is the greatest")