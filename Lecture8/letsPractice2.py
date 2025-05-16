'''
Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance.
'''

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        print("Account number",self.account_no,"balance",self.balance)

acc1 = Account(1200, 123)
acc1.debit(200)
acc1.credit(500)


acc1 = Account(45000, 12345)
acc1.debit(3000)
acc1.credit(5000)