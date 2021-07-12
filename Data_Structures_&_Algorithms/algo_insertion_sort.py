numbers = [4, 5, 12, 45, 2, 47, 55, 78, 102]

# Insertion Sort
# divide list into sorted and unsorted
# take the item to the left of the unsorted item, move it to the sorted side then compares it and change position
# continues process until the items are sorted

# STEPS
# 1. set total length of the list
# 2. set the indexing value as the smallest in the list
# 3. create while loop, if the item to the left is larger than the value_to_sort we switch & look at the next item, prevent negative indexing
# 4. do the swap, continue to iterations


def insertion_sort(numbers):
    total_length = range(1, len(numbers) - 1)
    for i in total_length:
        value_to_sort = numbers[1]

        while numbers[i-1] > value_to_sort and i > 0:
            numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
            i = i - 1

    return numbers



print(insertion_sort([4, 5, 12, 45, 2, 47, 55, 78, 102]))
