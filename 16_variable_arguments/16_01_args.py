'''
Write a script with a function that demonstrates the use of *args.

'''
# from my coursework notes

def print_args(*args):
    for a in args:
        print(a)
print_args('barcelona', 'malta', 'ubud')