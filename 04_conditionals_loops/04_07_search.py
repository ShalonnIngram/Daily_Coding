'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
import random
number_search = random.randint(1, 10)
guess = None

while guess != number_search:
    guess = input("input number: ")
    if guess == number_search:
        print(guess)
        break
    else:
        print("keep guessing")
