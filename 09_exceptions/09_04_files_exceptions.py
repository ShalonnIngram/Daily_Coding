'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable OK

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string OK

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''
# read in war_peace_txt
war_list = []
with open('/Users/cianikaingram/Documents/CodingNomads/labs/python_fundamentals-master/09_exceptions/books/war_and_peace.txt', 'r') as war_peace:
    for w in war_peace:
        w = w.rstrip()
        war_list.append(w)


# overwrite crime_and_punishment file
empty_string = ""
with open('/Users/cianikaingram/Documents/CodingNomads/labs/python_fundamentals-master/09_exceptions/books/crime_and_punishment.txt', 'w') as crime_pun:
    crime_pun.write(empty_string)
    crime_pun.close()

# read in pride_and_predjudice.txt
pride_list = []
with open('/Users/cianikaingram/Documents/CodingNomads/labs/python_fundamentals-master/09_exceptions/books/pride_and_prejudice.txt', 'r') as pride:
    for p in pride:
        p = p.rstrip()
        pride_list.append(p)


crime_list = []
with open('/Users/cianikaingram/Documents/CodingNomads/labs/python_fundamentals-master/09_exceptions/books/crime_and_punishment.txt', 'r') as crime_two:
    for c in crime_two:
        c = c.rstrip()
        crime_list.append(c)
        crime_two.close()


# print out first word

try:
    print(war_list[0][0:4])
    print(pride_list[0][0:3])
    print(crime_list[0][0])
except IndexError:
    print('theres no text on one of your files')

