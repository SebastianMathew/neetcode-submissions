class Solution:

    def encode(self, strs: List[str]) -> str:
        a = ""
        for word in strs:
            a+=str(len(word))+"#"+word
        return a

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i<len(s):
            j = i
            while s[j]!='#':
                j+=1

            length = int(s[i:j])

            j+=1

            word = s[j:j+length]
            res.append(word)
            i = j+length
        return res

