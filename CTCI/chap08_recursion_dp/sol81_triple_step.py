from typing import Optional

def sol(n) -> Optional[int]:
    memo = [None]*(n+1)
    memo[0] = 1
    def numWaysToStep(n) -> Optional[int]:
        if n < 0:
            return None
        if memo[n] is None:
            possibilities = [numWaysToStep(n-i) for i in [1,2,3]]
            memo[n] = sum(p for p in possibilities if p is not None) 
        return memo[n]
    return numWaysToStep(n)


def test():
    for i in range(10):
        print(sol(i))
