'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

# take string from user
user_input = input("Please input a word: ")

# create empty dictionary
char_count = {}

# iterate over each character of user input
# add characters to char_count
# if letter is already added, += 1 value else value is 1
for l in user_input:
    if l in char_count:
        char_count[l] += 1
    else:
        char_count[l] = 1

print(char_count)




# split letters and count occurences