#Write a Function to convert  USD to INR.
def convertUSDToINR(amountInUSD):
    amountInINR = amountInUSD*83
    return amountInINR

amountInUSD = int(input("Enter the amount in USD: "))
amountInINR = convertUSDToINR(amountInUSD)
print(amountInUSD,"$ =", "₹",amountInINR)