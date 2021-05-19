'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
dividend = input("enter a number: ")
divisor = input("enter another number: ")

try:
    print(dividend/divisor)
except (TypeError, ZeroDivisionError):
    print("you must enter a number other than zero, & not a word")







