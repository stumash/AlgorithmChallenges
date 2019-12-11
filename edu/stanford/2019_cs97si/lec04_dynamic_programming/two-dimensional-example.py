def sol(xs1, xs2, top_down_NOT_bottom_up=True):
    """
    Compute the Longest Common Subsequence of xs1 and xs2

    E.g. xs1=['x', 'A', 'x', 'B', 'x'],
         xs2=['A', 'y', 'y', 'B'],
      -> size=2, LCS=['A', 'B']
    """

    memo = [[None for _ in range(len(xs2))] for _ in range(len(xs1))]

    def backtrack():
        i, j = len(xs1)-1, len(xs2)-1
        rev_path = []
        while True:
            next_i, next_j = max(
                (((memo[i-1][j-1] if i-1>=0 and j-1>=0 else 0) + (1 if xs1[i]==xs2[j] else 0)), (i-1,j-1)),
                ((memo[i-1][j] if i-1>=0 else 0),                                               (i-1,j)),
                ((memo[i][j-1] if j-1>=0 else 0),                                               (i,  j-1)),
            key=lambda tup: tup[0])[1]

            if (next_i, next_j) == (i-1, j-1):
                print(i)
                rev_path.append(xs1[i])

            if i==0 or j==0:
                break
            i, j = next_i, next_j

        return list(reversed(rev_path))

    if top_down_NOT_bottom_up:
        def dp(xs1, i, xs2, j):
            if i < 0 or j < 0:
                return 0
            if memo[i][j] is None:
                memo[i][j] = max(
                    dp(xs1, i-1, xs2, j-1) + (1 if xs1[i]==xs2[j] else 0),
                    dp(xs1, i-1, xs2, j),
                    dp(xs1, i, xs2, j-1)
                )
            return memo[i][j]
        return dp(xs1, len(xs1)-1, xs2, len(xs2)-1), backtrack()

    else:
        def dp(xs1, xs2):
            for i in range(len(xs1)):
                for j in range(len(xs2)):
                    memo[i][j] = max(
                        (0 if i-1 < 0 or j-1 < 0 else memo[i-1][j-1]) + (1 if xs1[i]==xs2[j] else 0),
                        (0 if i-1 < 0 else memo[i-1][j]),
                        (0 if j-1 < 0 else memo[i][j-1])
                    )
            return memo[len(xs1)-1][len(xs2)-1]
        return dp(xs1, xs2), backtrack()


def test():
    xs1, xs2 = "ABCBDAB", "BDCABC"
    print(sol(xs1, xs2))
    print(sol(xs1, xs2, top_down_NOT_bottom_up=False))
