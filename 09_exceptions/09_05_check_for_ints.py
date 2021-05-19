'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

user_input = None

while type(user_input) != int:
    try:
        user_input = int(input("input number: "))
        print("integer!")
    except:
        print("this isnt a int")





