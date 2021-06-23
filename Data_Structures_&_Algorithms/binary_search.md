# Binary Search

``` python
# must be sorted
def binary_search(list, target):
    first = 0
    last = len(list) - 1
# constant time operations -> log runtime
    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print("target found at index: ", index)
    else:
        print("target is not found in the list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 8)
verify(result)






"""Basic binary search algorithm"""

haystack = [7, 7, 22, 37, 47, 55, 57, 57, 86, 91]
needle = int(input("Enter the number you are searching for: "))
length = len(haystack)
lower_bound = 0
upper_bound = length - 1
found = False

while found == False and lower_bound <= upper_bound:
    mid_point = (lower_bound + upper_bound) // 2
    if haystack[mid_point] == needle:
        print("You number has been found.")
        found = True
    elif haystack[mid_point] < needle:
        lower_bound = mid_point + 1
    else:
        upper_bound = mid_point - 1
if found == False:
    print("Your number is not in the list.")

```
