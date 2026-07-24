from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        return [x for x,_ in sorted(a.items(), key = lambda a:a[1], reverse = True)][:k]