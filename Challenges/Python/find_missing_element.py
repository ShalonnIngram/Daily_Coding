'''
FIND THE MISSING ELEMENTS
Consider a array of non negative integers. A second array is formed by
shuffling the elements of the first array and deleting a random element.
Given these two arrays, find the which element is missing from the second
array.
'''
list1 = [1,2,3,4,5,6,7]
list2 = [3,7,2,1,4,6]

def finder(list1, list2):
    list1.sort()
    list2.sort()

    for num1, num2 in zip(list1, list2):
        if num1 != num2:
            return num1
    return list1[-1]


print(finder(list1, list2))

'''
O(nlog(n))
1. sort each list
2. zip the lists together
3. iterate over zipped lists
4. if num1 doesnt equal num2 return number of the first array because it was missing
otherwise return the last element of the first array
'''
