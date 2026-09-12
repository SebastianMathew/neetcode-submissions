class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {'[':']','{':'}','(':')'}
        stack = []
        for c in s:
            if c in mappings.keys():
                stack.append(c)

            elif c in mappings.values():
                if len(stack)>=1:
                    if mappings[stack[-1]] == c:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        return len(stack) == 0