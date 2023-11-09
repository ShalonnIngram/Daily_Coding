
1. because we need to move zeros to one size, create a variable and set it to zero
2. iterate over the entire list
3. if right pointer: (we know this bc the other pointer/variable will be set to zero), then switch positions
4. increment pointer & return nums

    def moveZeroes(self, nums):

        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums
