s = 'players'
t = 'parsley'

def isAnagram(s, t):
    # check to see if the lengths are equal
    if len(s) != len(t):
        return False

    # create empty hashmaps
    countS, countT = {}, {}

    # build out the hashmaps but iterating over the strings
    # add character & count to the hashmaps as key & values
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    # iterate through the counts
    # use the count of the first string to compare to the second string
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True


print(isAnagram(s, t))
