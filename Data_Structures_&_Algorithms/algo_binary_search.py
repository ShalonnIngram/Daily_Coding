# Binary Search (must be sorted)
# search to see if an item is in a list
# looks at mid point search > midpoint go right, if not go left

# STEPS
# 1. set beginning and ending index
# 2. set midpoint while beginning index is less than end index
# 3. compare midpoint to item we are looking for, do comparisons
# 4. if item is less than midpoint move to the right else move to the left

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1

    return None

sequence = [1, 5, 12, 15, 25, 35, 89, 99, 101]
item = 15
print(binary_search(sequence, item))
