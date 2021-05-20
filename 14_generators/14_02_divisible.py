'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''
my_list = [1111, 8, 7777, 4]
gen = (x for x in my_list if x % 1111 == 0)
for i in gen:
    num = i
    print(num)