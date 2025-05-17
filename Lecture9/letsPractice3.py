'''
Create a class called Order which stors item & its price.
Use Dunder function __gt__() to convey that:
order1>order2 if pricee of order1>price of order2
'''

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, o2):
        return self.price > o2.price

o1 = Order("chips", 20)
o2 = Order("tea", 15)

print(o1.item)
print(o1.price)

print(o2.item)
print(o2.item)

print(o1>o2)