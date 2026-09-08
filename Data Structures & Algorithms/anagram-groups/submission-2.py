from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        
        for word in strs:
            b = [0]*26
            for c in word:
                b[ord(c)-ord('a')]+=1

            a[tuple(b)].append(word)

        return list(a.values())