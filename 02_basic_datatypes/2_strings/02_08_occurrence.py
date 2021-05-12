'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

string_input = input("Please input a few words. ")
letter_input = input("Please input a letter in previous words you inputted earlier. ")
result = string_input.find(letter_input)
print("String input: {}".format(string_input))
print("Letter input: {}". format(letter_input))
print("Result: {}".format(result))
