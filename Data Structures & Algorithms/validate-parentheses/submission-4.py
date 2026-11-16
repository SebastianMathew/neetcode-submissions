class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rule = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in rule.keys():
                stack.append(c)
            elif stack:
                if rule[stack[-1]]==c:
                    stack.pop()
                else:
                    return False
            else:
                return False

        if stack:
            return False
        return True
        