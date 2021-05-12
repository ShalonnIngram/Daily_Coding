'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

investment = int(input("Please input your investment amount. "))
interest_rate = float(input("Please input your interest rate. "))
interest_rate = interest_rate / 100
num_years = int(input("Please input the number of years to invest. "))

result = (investment * interest_rate) * num_years
print("You will have ${} in {} years". format(result, num_years))