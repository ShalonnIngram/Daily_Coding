'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
def divisible(num):
    if num % 4 == 0 or num % 7 == 0:
        return True
    else:
        return False


# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def divisible(num):
    if num % 4 == 0 and num % 7 == 0:
        return True
    else:
        return False


# take in a number from the user between 1 and 1,000,000,000
user_input1 = int(input("Please input a number between 1 and 1,000,000,000: "))
user_input2 = int(input("Please input a number between 1 and 1,000,000,000: "))

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 
my_number1 = print(divisible(user_input1))
my_number2 = print(divisible(user_input2))

# print your new variables to display the results
print(my_number1, my_number2)