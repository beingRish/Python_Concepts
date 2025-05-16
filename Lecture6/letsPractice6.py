#Write a recursive function to calculate the sum of first n natural numbers.

def cal_sum_of_first_n_natural_numbers(n):
    if(n==0):
        return 0
    return cal_sum_of_first_n_natural_numbers(n-1) + n


print(cal_sum_of_first_n_natural_numbers(10))