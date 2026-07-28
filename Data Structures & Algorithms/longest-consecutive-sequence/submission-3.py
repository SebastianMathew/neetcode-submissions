class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        print(numSet)
        for num in numSet:
            print(num)
            if num - 1 not in numSet:
                length = 1

                while num+length in numSet:
                    length+=1
                    print(length)

                longest = max(longest, length)
        return longest
        