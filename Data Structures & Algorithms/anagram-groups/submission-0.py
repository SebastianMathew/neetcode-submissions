from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str])-> List[List[str]]:
        grp = defaultdict(list)
        for i in strs:
            word = list(i)
            word.sort()
            grp["".join(word)].append(i)
        
        return list(grp.values())
        