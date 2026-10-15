class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        minn = float("inf")
        maxdiff = float("-inf")
        for price in prices:
            if price<minn:
                minn = min(minn, price)
            else:
                diff = price-minn
                maxdiff = max(maxdiff,diff)

        return maxdiff if maxdiff>=0 else 0
            
            

        