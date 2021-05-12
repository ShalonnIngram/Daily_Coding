'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

user_input = input("Please input a short sentence. ")
vowels = "a,e,i,o,u"
print("Users input: {}".format(user_input))

count = user_input.count("a") + user_input.count("e") + user_input.count("i") + user_input.count("o") + user_input.count("u")
print("Total number of vowels: {}".format(count))

a = user_input.count("a")
e = user_input.count("e")
i = user_input.count("i")
o = user_input.count("o")
u = user_input.count("u")

print("a occurs {} times".format(a))
print("e occurs {} times".format(e))
print("i occurs {} times".format(i))
print("o occurs {} times".format(o))
print("u occurs {} times".format(u))



