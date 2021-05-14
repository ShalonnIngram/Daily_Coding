'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
# 10 5 14 21 34 56 11 22 70 41

nums = input("Please input 10 numbers: ")
nums_list = nums.split()
nums_sorted = sorted(nums_list)

print(nums_sorted[-1])



# nums_list = nums.split()
# print(type(nums_list))
# nums_list = int(nums_list)
# print(max(nums_list))