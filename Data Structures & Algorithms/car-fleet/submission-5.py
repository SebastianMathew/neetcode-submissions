class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pospe = []
        n = len(position)
        for i in range(n):
            time = (target - position[i])/speed[i]
            pospe.append((position[i],speed[i],time))

        pospe.sort(reverse = True)
        stack = []
        cf = 0

        for i in range(n):
            cs = pospe[i][2]

            stack.append(cs)

            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)