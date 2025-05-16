#resursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

'''
5
4
3
2
1
'''

#Find Factorial of n using Recursion
def calc_fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * calc_fact(n-1)

print(calc_fact(5))