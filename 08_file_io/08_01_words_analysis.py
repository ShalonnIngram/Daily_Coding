'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''


word_count = []
# open file, strip unwanted characters & print all words to a list
with open('words.txt', 'r') as fin:
    for f in fin.readlines():
        f = f.rstrip()
        word_count.append(f)
        fin.close()


shortest = min(word_count, key=len)
longest = max(word_count, key=len)
total_words = len(word_count)

# prints shortest word
print(shortest, longest, total_words)





