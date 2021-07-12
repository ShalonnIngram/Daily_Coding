# Quick Sort
# sorts in asc or desc order
# takes pivot number which is the number (last item in the unsorted list)
# compares all numbers to the pivot number, if the number is less. goes to less than column if greater than goes to the left column
# sort the two list by creating a number pivot

# STEPS
# 1. find length of sequence
# 2. skip over sequences that have a length less than or equal to one
# 3. define pivot, & pop --> remove last element and return it
# 4. create the two lists
# 5. do a comparison on each item in sequence
# 6. repeat process


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lesser = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lesser.append(item)

    return quick_sort(items_lesser) + [pivot] + (items_greater)

print(quick_sort([4, 5, 12, 45, 2, 47, 55, 78, 102]))
