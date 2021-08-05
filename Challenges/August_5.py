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
