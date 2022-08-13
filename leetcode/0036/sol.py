from typing import List
from collections import defaultdict

class Solution:
    def isValidSudokuGroup(self, cells: List[str]) -> bool:
        d = defaultdict(int)
        for cell in cells:
            d[cell] += 1
        for k,v in d.items():
            if k != '.' and v > 1:
                return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        if not all(self.isValidSudokuGroup(row) for row in board):
            return False
        # cols
        if not all(self.isValidSudokuGroup([board[i][j] for i in range(len(board))]) for j in range(len(board[0]))):
            return False
        # squares
        for square_i in range(9):
            i_range = range((square_i // 3) * 3, (square_i // 3) * 3 + 3)
            j_range = range((square_i % 3) * 3, (square_i % 3) * 3 + 3)
            if not self.isValidSudokuGroup([board[i][j] for i in i_range for j in j_range]):
                return False

        return True

tests = [
    ([["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]],
    True),
    ([["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]],
    False),
]
for board, expected in tests:
    actual = Solution().isValidSudoku(board)
    if actual != expected:
        print(board)
        print(f'expected isValidSudoku={expected} but got {actual}\n')
