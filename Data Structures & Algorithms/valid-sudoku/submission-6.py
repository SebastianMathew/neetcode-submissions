class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            c = set()
            for num in row:
                if num != ".":
                    if num in c:
                        return False
                    c.add(num)
        
        for i in range(9):
            c = set()
            for j in range(9):
                if board[j][i]!=".":
                    if board[j][i] in c:
                        return False
                    c.add(board[j][i])
        
        for i in range(3,9,3):
            for j in range(3,9,3):
                c = set()
                for k in range(i-3,i):
                    for l in range(j-3,j):
                        if board[k][l]!=".":
                            if board[k][l] in c:
                                return False
                            c.add(board[k][l])

        return True

        