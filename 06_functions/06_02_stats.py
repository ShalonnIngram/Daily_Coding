'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list):
  # define the function here
  max_num = max(list)
  min_num = min(list)
  avg_num = sum(list) / len(list)
  sum_num = sum(list)

  return max_num, min_num, avg_num, sum_num

example_list = [1, 2, 3, 4, 5, 6, 7]

# call the function below here
print(stats(example_list))