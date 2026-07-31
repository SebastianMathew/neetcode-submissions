from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nf = Counter(nums)

        ca = [[] for _ in range(len(nums)+1)]
        for n,f in nf.items():
            ca[f].append(n)
        
        res = []

        for freq in range(len(nums),-1,-1):
            for num in ca[freq]:
                res.append(num)

                if len(res) == k:
                    return res