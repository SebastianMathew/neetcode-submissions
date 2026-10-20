from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        
        num_count = Counter(nums)

        for num, occ in num_count.items():
            bucket[occ].append(num)

        result = []

        for i in range(n, -1, -1):
            for nu in bucket[i]:
                result.append(nu)
                k-=1
                if k==0:
                    return result
                