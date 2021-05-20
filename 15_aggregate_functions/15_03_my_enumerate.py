'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''


def my_enumerate(list):
    for i, j in enumerate(list):
        print(i, j)


fruits = [ "Apple","Berry","Cherry"]
print(my_enumerate(fruits))