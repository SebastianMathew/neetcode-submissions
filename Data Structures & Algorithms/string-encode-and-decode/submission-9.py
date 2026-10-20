class Solution:

    def encode(self, strs: List[str]) -> str:
        a = ""
        for s in strs:
            n = len(s)
            a+= str(n)+"#"+s

        print(a)
        return a

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j = i
            while not s[j] == "#":
                j+=1
            j+=1
            leng = int(s[i:j-1])
            i = j
            while leng>0:
                j+=1
                leng-=1
            word = s[i:j]
            res.append(word)
            i = j
        return res

