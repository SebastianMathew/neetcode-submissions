from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b = Counter(nums)
        for i in b.values():
            if i>1:
                return True
        return False
               