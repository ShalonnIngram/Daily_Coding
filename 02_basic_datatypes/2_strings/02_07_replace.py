'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

string_input = input("Please input a few words. ")
symbol_input = input("Please input a symbol. ")
string_letter = string_input[0]
result = string_input.replace(string_letter, symbol_input)

print("String input: {}".format(string_input))
print("Letter input: {}". format(symbol_input))
print("Result: {}".format(result))