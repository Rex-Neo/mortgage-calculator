mortgage_principle = float(input("Enter your Mortgage Principle: "))
mortgage_annual_interest = float(input("Enter your Annual Interest Rate: "))
payment_years = float(input("Enter the number of years in your term: "))


mortgage_payments = mortgage_principle * ((mortgage_annual_interest / 12) * (1 + mortgage_annual_interest) ** (payment_years * 12)) / ((1 + mortgage_annual_interest) ** (payment_years * 12 - 1))
# M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]
# P = principal loan amount
# i = monthly interest rate
# n = number of months required to repay the loan

print("Your monthly payments will be:", mortgage_payments)