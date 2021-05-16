'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''
mydict = {}
keys = range(1, 11)
values = range(11)

for i in keys:
    mydict[i] = values[i] * i
print(mydict)





