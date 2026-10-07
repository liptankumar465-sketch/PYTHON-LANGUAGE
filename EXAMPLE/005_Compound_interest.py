def compound_interest(principal_amount, time_period, rate_of_interest):
    amount = principal_amount * pow(1 + rate_of_interest / 100, time_period)
    return amount - principal_amount


#! take user inputs:
p = float(input('Enter the principal amount: '))
t = float(input('Enter the time period: '))
r = float(input('Enter the rate of interest: '))

print(f'Compound interest is: {compound_interest(p, t, r)}')
