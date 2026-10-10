class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right

        while left<=right:
            k = (left+right)//2

            hn = sum((-(-p//k)) for p in piles)

            if hn<=h:
                ans = k
                right = k-1
            else:
                left = k+1

        return ans