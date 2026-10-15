class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not len(prices)>=2:
            return 0

        left, right = 0, 1
        mdiff = 0
        while right<len(prices):

            diff = prices[right]-prices[left]

            if diff<0:
                left = right
                right+=1
            else:
                mdiff = max(mdiff,diff)
                right+=1

        return mdiff