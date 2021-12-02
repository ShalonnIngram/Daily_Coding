# set a variable thats very small to capture negative numbers
# iterate over every element in the list
# compare each element to the variable to see which one is that highest
# if the element is higher then set it as the variable value
# return the variable value


nums = [2, 6, 4, 13, 99, 1201]

def maxnum(nums):
    maximum = float('-inf')

    for num in nums:
        if num > maximum:
            maximum = num
    return maximum

print(maxnum(nums))
