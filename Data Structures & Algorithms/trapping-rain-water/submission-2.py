class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        left, right = 0, len(height)-1
        leftmax = 0
        rightmax = 0

        while left<right:
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])

            if leftmax<rightmax:
                result+= leftmax-height[left]

                left+=1
            else:
                result+= rightmax-height[right]

                right-=1

        return result

