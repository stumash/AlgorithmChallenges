from typing import List, Optional

def tic_tac_win(board: List[List[Optional[str]]]) -> Optional[str]:
    def f(c, c2):
        c1 = board[c[0]][c[1]]
        if c1 is None: return None
        return c1.lower() == c2

    for row in [
        # horizontal
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # vertical
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        # diagonal
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)],
    ]:
        for c2 in ['x', 'o']:
            if all(f(c, c2) for c in row):
                return c2
    return None

print(tic_tac_win([
    ['x', None, 'x'],
    ['o', 'o', 'o'],
    [None, None, 'x'],
]))
