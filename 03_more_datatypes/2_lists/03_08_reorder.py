'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

# 1 2 3 4 5 6 7 8 9 10

nums = input("Please input 10 numbers: ")
nums_list = nums.split()

second = nums_list[1]
fourth = nums_list[3]
sixth = nums_list[5]
eighth = nums_list[7]
tenth = nums_list[9]
ninth = nums_list[8]
seventh = nums_list[6]
fifth = nums_list[4]
third = nums_list[2]
first = nums_list[0]

print(second, fourth, sixth, eighth, tenth, ninth, seventh, fifth, third, first)



#nums_list = nums.split()

