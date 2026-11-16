class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ['+','-','*','/']:
                stack.append(int(token))
            else:
                op = token
                o2 = stack.pop()
                o1 = stack.pop()

                match token:
                    case '+':
                        stack.append(o1+o2)
                    case '-':
                        stack.append(o1-o2)

                    case '*':
                        stack.append(o1*o2)

                    case '/':
                        stack.append(int(o1/o2))

        return stack[0]

