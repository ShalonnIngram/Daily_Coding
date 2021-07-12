# Bubble sort
# takes unsorted list and sorts & orders in ascending values
# compares two values and moves highest value to the right
# STEPS
# 1. get the total length of the list
# 2. create a boolean value to break out of loop when list has been sorted
# 3. while loop because we don't know how may iterations we will need before it is completed
# 4. while sorted is false, iterate (the number of total_length times)
# 5. if the number to the left is greater than the number to the right, switch numbers
# 6. return the list & call the function

numbers = [4, 5, 12, 45, 2, 47, 55, 78, 102]

def bubble_sort(numbers):
    total_length = len(numbers) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, total_length):
            if numbers[i] > numbers[i + 1]:
                sorted = False
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

    return numbers

print(bubble_sort([4, 5, 12, 45, 2, 47, 55, 78, 102]))
