def simple_interest(principal_amount, time_period, rate_of_interest):
    return (principal_amount * time_period * rate_of_interest) / 100


#! take user inputs:
p = float(input('Enter the principal amount: '))
t = float(input('Enter the time period: '))
r = float(input('Enter the rate of interest: '))

print(f'Simple interest is: {simple_interest(p, t, r)}')
