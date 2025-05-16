def calc_sum(a, b):
    return a+b

print(calc_sum(5,10))   #15
print(calc_sum(12,14))  #26

def print_hello():
    print("Hello")

print_hello()   #Hello

output = print_hello()
print(output)   #None

#average of 3 numbers

def calc_avg(a, b, c):
    avg = (a + b + c)/3
    return avg

print(calc_avg(23, 45, 65)) #44.333333333333336

#default parameters
def cal_prod(a, b=6):
    return a*b

print(cal_prod(4))