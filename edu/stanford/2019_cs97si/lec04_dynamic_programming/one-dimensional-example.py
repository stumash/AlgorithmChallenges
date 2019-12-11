from typing import List

def sol(xs: List[int], n: int, top_down_NOT_bottom_up=True):
    """
    How manys combos of numbers in xs sum to n?

    E.g. n=5, xs=[1,3,4]:
      5 =
        = 1 + 1 + 1 + 1 + 1   |     1
        = 1 + 1 + 3           |   + 1
        = 1 + 3 + 1           |   + 1
        = 3 + 1 + 1           |   + 1
        = 1 + 4               |   + 1
        = 4 + 1               |   + 1
                              |   ----
                              |     6 <- there are six combos
    """
    memo = [0]*(n+1)
    memo[0] = 1

    if top_down_NOT_bottom_up:
        def dp(n):
            if n < 0:
                return 0
            if memo[n]:
                return memo[n]
            return sum(dp(n-x) for x in xs)
    else:
        def dp(n):
            for i in range(1,n+1):
                for x in xs:
                    if i-x < 0:
                        continue
                    memo[i] += memo[i-x]
            return memo[n]

    return dp(n)

def test():
    xs = [1,3,4]
    n = 10

    print(f"xs: {xs}, n: {n}, top_down_NOT_bottom_up=True")
    for i in range(0, n):
        print(f"{i}: {sol(xs, i, top_down_NOT_bottom_up=True)}")

    print()

    print(f"xs: {xs}, n: {n}, top_down_NOT_bottom_up=False")
    for i in range(0, n):
        print(f"{i}: {sol(xs, i, top_down_NOT_bottom_up=False)}")
