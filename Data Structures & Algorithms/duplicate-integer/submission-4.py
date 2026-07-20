class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = False
        nums.sort()
        prev = -1
        for i in nums:
            cur  = i
            if cur == prev:
                a = True
                return a
            prev = i
        return a         