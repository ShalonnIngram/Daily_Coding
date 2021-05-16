'''
CHALLENGE: Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

NOTE: Check out the Python docs and see whether you can come up with a solution, even if you don't yet
      completely understand _why_ it works the way it does:
      https://docs.python.org/3/howto/sorting.html#key-functions
      Feel free to discuss any questions you have with your mentor and on the forum!

'''
input_dict = {"item1": 5, "item2": 6, "item3": 1}


# sort dictionary by values
input_dict_sorted = dict(sorted(input_dict.items(), key=lambda item: item[1]))


# convert pairs to list of tuples
input_dict_tuple = list(input_dict_sorted.items())
print(input_dict_tuple)
print(type(input_dict_tuple[0]))


