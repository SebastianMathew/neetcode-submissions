class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for i in row:
                if i !=".":
                    if i in seen:
                        return False
                    seen.add(i)


        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])

        
        for i in range(3,9,3):
            for j in range(3,9,3):
                seen = set()
                for k in range(i-3,i):
                    for l in range(j-3,j):
                        if board[k][l] != '.':
                            if board[k][l] in seen:
                                return False
                        seen.add(board[k][l])
        return True

        