from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 0
        l = 0
        occ = defaultdict(int)
        for r in range(len(s)):
            occ[s[r]] +=1

            while (r-l+1)- max(occ.values())>k:
                occ[s[l]]-=1
                l+=1

            longest = max(longest, r-l+1)

        return longest

        