
search_list = [1, 3, 6, 7, 8, 9]
target = 7

def binary_search(array, target):
    first_index = 0
    last_index = len(array) - 1

# while the first index is less than the last index find the first midpoint
# create midpoint then find the value to compare it to
    while first_index <= last_index:
        midpoint = first_index + (last_index - first_index) // 2
        midpoint_value = array[midpoint]

# compare the midpoint value to the target, if the value is the target then return the midpoint index
# if the target is less than midpoint value, change the ending index to move it to the left
# if the target is greater then the midpoint value, increase the first index by one to check the numbers to the right
# if the target is not in the array return None
        if target == midpoint_value:
            return midpoint
        elif target < midpoint_value:
            last_index = midpoint - 1
        elif target > midpoint_value:
            first_index = midpoint + 1
    return None
