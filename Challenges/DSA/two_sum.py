# BRUTE FORCE APPROACH
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


                
nums = [2, 1, 9, 22, 41, 52, 12]
target = 13


Time Complexity: O(n)
Space Complexity:  O(n)
# create an empty hash map
# iterate over the list, we need the index & value
# create a difference variable that returns the difference between the target & the value
# if the difference is in the hashmap, return the indicies
# else update the hashmap


def twosum(nums, target):
    mymap = {}     # mapping value: index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in mymap:
            return [mymap[diff], i]   # pair of indicies
        mymap[n] = i      # update hashmap

print(twosum(nums, target))
