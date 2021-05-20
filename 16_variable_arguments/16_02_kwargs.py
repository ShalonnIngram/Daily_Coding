'''
Write a script with a function that demonstrates the use of **kwargs.

'''

# from the coursework notes

def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

print_kwargs(country = 'indonesia', city = 'ubud')