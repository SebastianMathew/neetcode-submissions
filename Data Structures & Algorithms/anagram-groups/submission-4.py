from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)
        for word in strs:
            a = [0]*26
            for c in word:
                a[ord(c)-ord('a')]+=1
            grp[tuple(a)].append(word)
 

        return list(grp.values()) 
