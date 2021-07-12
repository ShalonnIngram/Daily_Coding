numbers = [4, 5, 12, 45, 2, 47, 55, 78, 102]

# Selection sort
# find minimum value in a list
# sets first number as the minimum and compares every number to its right
# when we come across a number that is less than the current minimum we set it as the new minimum and continue the process
# once we find the minimum in the entire list we divide the list into two sub lists: to the left is sorted to the right is unsorted
# prevents us from doing comparisons on items already sorted
# STEPS
# 1. set the length of the list minus one
# 2. for loop to iterate over list and set the minimum value
# 3. iterate over the first iterations and look at all of the elements to the right, if any item is smaller than our current value, then replace the min_value
# 4. if statment to find absolute smallest value and swap


def selection_sort(numbers):
    total_length = range(0, len(numbers) - 1)
    for i in total_length:
        min_value = i

# all elements to the right, if number is less move to the right
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_value]:
                min_value = j

        if min_value != i:
            numbers[min_value], numbers[i] = numbers[i], numbers[min_value]

    return numbers

print(selection_sort([4, 5, 12, 45, 2, 47, 55, 78, 102]))
