from typing import Tuple, List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        boards = []
        q_coords = [(i,0) for i in range(n)]
        
        def make_board() -> List[str]:
            board = []
            for row in range(n):
                r,c = q_coords[row]
                board.append("".join("." if c!=col else "Q" for col in range(n)))
            return board
        
        def same_diag(xy1: Tuple[int,int], xy2: Tuple[int,int]) -> bool:
            (x1,y1),(x2,y2) = xy1,xy2
            return x1-y1 == x2-y2 or x1+y1 == x2+y2
        
        def same_diags(xy: Tuple[int,int], xys: List[Tuple[int,int]]) -> bool:
            return any(map(lambda _xy: same_diag(xy,_xy), xys))
        
        def produce_boards(queen_num):           
            if queen_num == 0:
                possible_cols = list(range(n))
            else:
                earlier_q_coords = q_coords[:queen_num]
                _,earlier_q_cols = zip(*earlier_q_coords)
                possible_cols = [
                    col for col in range(n)
                    if col not in earlier_q_cols and not same_diags((queen_num,col), earlier_q_coords)
                ]
                #print(queen_num, earlier_q_cols, possible_cols)
            
            for col in possible_cols:
                #print(col)
                q_coords[queen_num] = (queen_num,col)
                if queen_num == n-1:
                    boards.append(make_board())
                else:
                    produce_boards(queen_num+1)
                    
        produce_boards(0)
        return boards
