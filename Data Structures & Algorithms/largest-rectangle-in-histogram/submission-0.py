class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # Stores (index, height) pairs
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx # The current bar can extend backwards to where the popped bar started
            stack.append((start, h))
            
        # Process remaining bars extending to the end of the histogram
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
            
        return max_area