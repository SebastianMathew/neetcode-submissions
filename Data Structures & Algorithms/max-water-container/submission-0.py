class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)

        left,right = 0,n-1
        while left<right:
            ar = min(heights[left],heights[right])*(right - left)

            max_area = max(ar,max_area)

            if heights[left]<heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            else:
                left+=1
                right-=1

        return max_area