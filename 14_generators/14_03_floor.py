'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
my_list = [1111, 8, 7777, 4]
gen = (x for x in my_list)
for i in gen:
    num = i // 1111
