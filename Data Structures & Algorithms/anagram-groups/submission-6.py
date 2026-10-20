from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        b = defaultdict(list)

        for s in strs:
            c = [0]*26
            for ch in s:
                c[ord(ch)-ord('a')]+=1
            b[tuple(c)].append(s)
            

        return [*b.values()]



        