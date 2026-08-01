class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            val = nums[i]
            if val in seen:
                return True
            seen.add(val)
        return False