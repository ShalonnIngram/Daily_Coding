'''
given two strings, check to see if they are anagrams. An anagram is when two stings can be written using the exact same letters  -  you can just rearrange the letters to get different phrase or word

ex: public relations is an anagram of ---> crap built on lies
    clint eastwood is an anagram of ---> old west action 
'''

s1 = s1.replace(" ", "")
s2 = s2.replace(" ", "")

def anagram(s1, s2):
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # check to see if all letters are 0
    for c in count:
        if count[c] != 0:
            return False
    return True

print(anagram(s1, s2))


'''
first string
for every letter in the string,
if that letter is already in the dictionary, add one to key
else just set count to one

second string
do reverse of  one

check to see if all the count match
'''
