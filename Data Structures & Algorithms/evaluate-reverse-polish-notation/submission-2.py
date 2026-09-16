class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for t in tokens:
            if t not in ["+","-","*","/"]:
                stack.append(int(t))
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                
                if t == "+":
                    stack.append(num2 + num1)

                elif t == "-":
                    stack.append(num2 - num1)
                
                elif t == "*":
                    stack.append(num2 * num1)

                elif t == "/":
                    stack.append(num2 / num1)

        return int(stack[-1])

