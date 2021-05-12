'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
user_input = input("Please input a three words. ")

split_word_one = user_input.split()[0]
split_word_two = user_input.split()[1]
split_word_three = user_input.split()[2]


print(str(len(split_word_one)) + "," + " " + split_word_one)
print(str(len(split_word_two)) + "," + " " + split_word_two)
print(str(len(split_word_three)) + "," + " " + split_word_three)

