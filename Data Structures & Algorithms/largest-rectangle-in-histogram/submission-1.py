class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        stack = []
        max_area = 0

        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                idx = stack.pop()
                height = heights[idx]
                width = i if not stack else i - stack[-1]-1
                area = height*width
                max_area = max(max_area,area)
            stack.append(i)

        return max_area
