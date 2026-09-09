class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        o = [1]*len(nums)
        left = 1
        for i in range(len(nums)):
            o[i]*=left
            left*=nums[i]

        right = 1
        for i in range(len(nums)-1,-1,-1):
            o[i]*=right
            right*=nums[i]

        return o