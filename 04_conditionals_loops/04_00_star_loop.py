'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = 3

stars_list = []

for i in range(1, n + 1):
    stars_list.append("*" * i)
print("\n".join(stars_list))

# number of