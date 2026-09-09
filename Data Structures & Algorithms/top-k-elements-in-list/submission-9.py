from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numcount = Counter(nums)

        bucket = [[] for _ in range(len(nums)+1)]

        for num,freq in numcount.items():
            bucket[freq].append(num)


        o = []

        for fr in range(len(nums),-1,-1):
            for num in bucket[fr]:
                o.append(num)
                if len(o)>=k:
                    return o
