class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        if not nums or k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * n
        right = [0] * n

        # Fill left array (Block Prefix Max)
        left[0] = nums[0]
        for i in range(1, n):
            # If we cross a block boundary (i % k == 0), reset max to current element
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])

        # Fill right array (Block Suffix Max)
        right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            # If we cross a block boundary from the right, reset max to current element
            if (i + 1) % k == 0:
                right[i] = nums[i]
            else:
                right[i] = max(right[i + 1], nums[i])

        # Calculate result for each window in O(1) time
        res = []
        for i in range(n - k + 1):
            window_max = max(right[i], left[i + k - 1])
            res.append(window_max)

        return res