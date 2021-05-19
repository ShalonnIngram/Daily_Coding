'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

words_twenty = []
with open('words.txt', 'r') as fin:
    for f in fin.readlines():
        f = f.rstrip()
        if len(f) > 20:
            words_twenty.append(f)
    fin.close()

print(words_twenty)


