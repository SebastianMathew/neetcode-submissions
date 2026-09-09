class Solution:

    def encode(self, strs: List[str]) -> str:
        o = ""
        for word in strs:
            o+=str(len(word))+"#"+word

        print(o)
        return o
    def decode(self, s: str) -> List[str]:
        o = []
        i = 0
        while(i<len(s)):
            j = i
            while(s[j]!='#'):
                j+=1
            
            length = int(s[i:j])
            j+=1
            word = s[j:j+length]
            o.append(word)
            i = j+length
        return o