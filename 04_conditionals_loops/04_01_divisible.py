'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

user_input = int(input("Please input a number between 1 and 1,000,000,000: "))


if user_input % 3 == 0:
    print("Yes, this number is divisible by 3.")
else:
    print("No, this number is not divisible by 3.")