# aggregate data from different sources
# find the most commonly used word given multiple text sources

import glob


# iterates ver files, if first appearance add to the dict, if multiple appears add to the count
def find_most_common_word():
    txt_files = glob.glob('*.txt')
    tracker = dict()
    

# open file, read in line by line then split into multiple words if line not blank
# remove special characters,  and converting words to lowercase
    for txt in txt_files:
        with open('file.txt') as f:
            line = f.readline()
            while line != '':
                words = line.split()
                for word in words:
                    word = word.replace(',', '').replace('.', '').lower()
                    if word not in tracker:
                        tracker[word] = 1
                    else:
                        tracker[word] = tracker[word] + 1
                line = f.readline()
    max(tracker, key=tracker.get)
    maxValue = max(tracker.values())

    print(f'Most common word: {maxkey}')
    print(f'How many times: {maxValue}')

if __name__ == '__main__':
    find_most_common_word()
