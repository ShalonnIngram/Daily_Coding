## STEPS
# 1. initiate and set up dictionary with freq counts
# 2. iterate over indexes of string
# 3. if count is one then return the index of the character


def firstnonrepeating(string):
    charcount = {}
    for char in string:
        charcount[char] = charcount.get(char, 0) + 1

    for i in range(len(string)):
        char = string[i]
        if charcount[char] == 1:
            return i
    return -1
