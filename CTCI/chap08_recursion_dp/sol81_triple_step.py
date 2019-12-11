def sol(n):
    memo = [None]*(n+1)
    memo[0] = 1
    def numWaysToStep(n):
        if n < 0:
            return None
        if memo[n] is None:
            memo[n] = sum(
                numWaysToStep(n-i) for i in [1,2,3] if numWaysToStep(n-i) is not None
            )
        return memo[n]
    return numWaysToStep(n)

def test():
    for i in range(10):
        print(sol(i))
