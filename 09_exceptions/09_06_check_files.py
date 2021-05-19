'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

nums = []

file_name = 'integers.txt'
with open(file_name, 'r') as integers:
    for i in integers.readlines():
        i = i.rstrip()
        nums.append(i)

dividend = int(nums[0])
divisor = 0

try:
    calc = dividend / divisor
    print(calc)
except (IOError, ValueError, ZeroDivisionError):
    print("there is an issue with your file or calculation ")

