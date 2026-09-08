

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):

            a = target - nums[i]

            if a in seen:
                return [seen[a],i]

            seen[nums[i]] = i