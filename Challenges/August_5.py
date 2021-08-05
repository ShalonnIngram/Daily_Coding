520. Detect Capital
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word:
            return True
        if word[0].upper() == word:
            return True
        if word.lower() == word:
            return True
        else:
            return False

        
1. Two Sumclass Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
