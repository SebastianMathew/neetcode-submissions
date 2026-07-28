from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = defaultdict(bool)
            for num in row:
                if num !='.':
                    if num in seen:
                        return False

                    seen[num] = True

        for j in range(9):
            seen = defaultdict(bool)
            for i in range(9):
                if board[i][j]!='.':
                    if board[i][j] in seen:
                        return False
                    seen[board[i][j]] = True

        for i in range(3,9,3):
            for j in range(3,9,3):
                seen = defaultdict(bool)
                for col in range(i-3,i):
                    for row in range(j-3,j):
                        if board[col][row]!='.':
                            if board[col][row] in seen:
                                return False
                            seen[board[col][row]] = True


        return True