from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        b = [[] for _ in range(len(nums)+1)]

        for num,freq in a.items():
            b[freq].append(num)
        
        ans = []

        for i in range(len(nums),0,-1):
            for n in b[i]:
                ans.append(n)
                if len(ans)== k:
                    return ans
        