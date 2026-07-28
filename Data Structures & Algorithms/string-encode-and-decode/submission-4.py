class Solution:

    def encode(self, strs: List[str]) -> str:  
        a = ""
        for i in strs:
            a+=str(len(i))+"#"+i
        return a


    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i<len(s):
            j = i
            while s[j]!= "#":
                j+=1
            length = int(s[i:j])
            j+=1
            word = s[j:j+length]
            ans.append(word)
            i = j+length
        return ans