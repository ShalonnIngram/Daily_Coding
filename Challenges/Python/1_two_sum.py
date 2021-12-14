1. Two Sumclass Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

                
                
                
def pair_sum(numbers, target_sum):
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] + numbers[j] == target_sum:
        return (i, j)
