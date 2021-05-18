'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
my_name = "shalonn"
my_year = 1987
def cap_name(name1):
    name1 = my_name.capitalize()
    return name1

def char_count(name2):
    for x in range(1):
        return cap_name(name2) + "," + "is awesome!" * 3

def cal_yob(year):
    return 2021 - my_year

print(cap_name(my_name))
print(char_count(my_name))
print(cal_yob(my_year))


