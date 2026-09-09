class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numss = set(nums)
        longest = 0
        for num in numss:
            if num-1 not in numss:
                curr = num
                length = 1

                while curr+1 in numss:
                    curr+=1
                    length+=1

                longest = max(longest,length)

        return longest