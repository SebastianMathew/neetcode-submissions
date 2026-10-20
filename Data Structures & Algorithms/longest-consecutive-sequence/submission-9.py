class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        qan = set(nums)
        lcm = 0
        for n in nums:
            lc = 0
            if n-1 not in qan:
                lc+=1
                curr = n
                while curr+1 in qan:
                    lc+=1
                    curr = curr+1
                lcm = max(lcm, lc)

        return lcm
                    
        