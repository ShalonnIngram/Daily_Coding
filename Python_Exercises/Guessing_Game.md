# Guessing Game


Traditional guessing where the user guess the random generated number by the computer.

Topic Displayed
- Control Flow
- Loops
- Random module



``` python

import random

random_number = random.randint(1, 10)
print(random_number)
guess = None

while guess != random_number:
    guess = input('Guess a number from 1 to 10: ')
    guess = int(guess)
    if guess < random_number:
            print('Your guess is too low :(!')
    elif guess > random_number:
            print('Your guess is too high!')
    else:
        print('You guess the right number! Congratulations!')
        keep_playing = input('Would you like to keep playing? (y/n) ')
        if keep_playing == 'y':
            random_number = random.randint(1, 10)
        else:
            print('Thank you for playing!')
            break
