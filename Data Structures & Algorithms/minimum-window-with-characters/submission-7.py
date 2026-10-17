from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sring = ""

        if len(s)<len(t):
            return sring

        l,r = 0,0
        minn = float("+inf")

        check = Counter(t)
        missing = len(t)

        while len(s)-l>=len(t):

            if r >= len(s): 
                break
            if s[l] in check:
                if check[s[l]] > 0:
                    missing -= 1
                check[s[l]]-=1
                while len(s)-l>=len(t) and r<len(s):
                    if missing == 0:
                        minn = r+1-l
                        sring = s[l:r+1]
                        if minn==len(t):
                            return sring
                        while r+1-l>=len(t) and r<len(s):
                            if r+1-l == len(t):
                                sring = s[l:r+1]
                                return sring

                            elif check[s[l]]<0:
                                check[s[l]]+=1
                                if check[s[l]] > 0:
                                    missing += 1
                                l+=1
                                while not s[l] in check and r+1-l>=len(t):
                                    l+=1
                                if r+1-l<minn:
                                    minn = r+1-l
                                    sring = s[l:r+1]

                            else:
                                r+=1
                                while r<len(s) and not s[r]==s[l]:
                                    if s[r] in check:
                                        if check[s[r]] > 0:
                                            missing -= 1
                                        check[s[r]]-=1
                                    r+=1
                                if r<len(s):
                                    if s[r]==s[l]:
                                        l+=1
                                        while not s[l] in check:
                                            l+=1
                                        if r+1-l<minn:
                                            minn = r+1-l
                                            sring = s[l:r+1] 
                    else:
                        r+=1
                        if r<len(s):
                            if s[r] in check:
                                if check[s[r]] > 0:
                                    missing -= 1
                                check[s[r]]-=1
            else:
                r+=1
                l+=1

        return sring
        