'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

num_int = 5
num_float = 75.2

float_input = float(input("Please input a float. "))
int_input = int(input("Please input a int. "))


print(int(num_float))
print(float(num_int))
print(num_float // num_int)
print(float_input * int_input)








