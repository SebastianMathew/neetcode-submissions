from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.ts = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ts[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.ts[key]:
            return ""

        if self.ts[key][-1][0]<=timestamp:
            return self.ts[key][-1][1]

        if self.ts[key][0][0]>timestamp:
            return ""

        else:
            left, right = 0, len(self.ts[key])-2
            closest =0
            while left<=right:
                mid = (left+right)//2

                if self.ts[key][mid][0]==timestamp:
                    return self.ts[key][mid][1]
                elif self.ts[key][mid][0]>timestamp:
                    right = mid-1
                else:
                    closest = mid
                    left = mid+1
                    

        return self.ts[key][closest][1]
        

        
