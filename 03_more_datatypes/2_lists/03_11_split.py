'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
# Fun Friday its Finally Friday Friday is Fun Day Fun Fun Fun

user_input = input("please input a short sentence. ")
user_input_split = user_input.split()
user_input_list = list(user_input_split)

# convert into a set to get all unique values
user_input_set = set(user_input_list)

# create a dictionary that counts the number of occurrences
user_input_dictionary = {inputs:user_input_list.count(inputs) for inputs in user_input_set}

# list all values
all_values = list(user_input_dictionary.values())

# list all keys
all_keys =list(user_input_dictionary.keys())


print(all_keys[all_values.index(max(all_values))])
