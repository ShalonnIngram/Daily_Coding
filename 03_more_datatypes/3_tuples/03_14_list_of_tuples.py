'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

user_input = input("Please input a word: ")

user_split = user_input.split()

#    TODO:
# take a string
# convert to tuple
# put each tuple into list


# my_list = []
# for l in range(0, len(user_split)):
#     temp_word = tuple(user_split[l])
#     my_list += [temp_word]
#
# print(my_list)

my_list = []
for word in user_split:
    # print(word)
    my_list.append(tuple(word))
print(my_list)







