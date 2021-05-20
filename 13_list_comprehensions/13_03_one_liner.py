'''
Use a one-line list comprehension to express the following functionality:

letters = []

for letter in 'suchalongword':
    letters.append(letter)

print(letters)

'''
# letters = []
#
# for letter in 'suchalongword':
#     letters.append(letter)
#
# print(letters)


word = 'suchalongword'
letters = [x for x in word]
print(letters)