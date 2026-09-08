from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)

        b = [[] for _ in range(len(nums)+1)]

        for num,i in a.items():
            b[i].append(num)


        o = []
        for i in range(len(nums), -1,-1):
            for j in b[i]:
                o.append(j)
                if len(o)>=k:
                    return o