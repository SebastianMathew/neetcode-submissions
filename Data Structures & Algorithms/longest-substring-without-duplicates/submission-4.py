from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left,right = 0,0
        longest = 0
        seen = defaultdict(int)
        while right<len(s):


            if not s[right] in seen or seen[s[right]]<left:
                seen[s[right]] = right
                right+=1
                longest = max(longest,right-left)
            else:
                left = seen[s[right]]+1
                seen[s[right]] = right
                right+=1


        return longest



        