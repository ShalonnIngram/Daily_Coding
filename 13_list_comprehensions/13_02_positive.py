'''
Using list comprehension, create a list "positive" from the list
"numbers" that contains only the positive numbers from the list "numbers".

'''

numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]

convert_positive = [i * -1 for i in numbers if i < 0]

positive_numbers = [num for num in numbers if num > 0]

add_lists = [y for x in [convert_positive, positive_numbers] for y in x]

add_lists.sort()

print(add_lists)
