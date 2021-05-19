'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

all_words = []
with open('words.txt', 'r') as fin:
    for f in fin.readlines():
        f = f.rstrip()
        all_words.append(f)
        fin.close()


reverse_words = all_words.reverse()


with open('words_reverse.txt', 'w') as revfile:
        revfile.write('\n'.join(all_words))


