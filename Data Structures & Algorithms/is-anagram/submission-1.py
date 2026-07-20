class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        a.sort()
        print(a)
        b= list(t)
        b.sort()
        print(b)
        if a==b:
            return True
        return False
