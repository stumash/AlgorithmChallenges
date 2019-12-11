def sol(s1, s2):
    if min(len(s1), len(s2)) == 0:
        return abs(len(s1) - len(s2))

    memo = [[None]*len(s2) for _ in range(len(s1))]
    memo[0][0] = 0 if s1[0] == s2[0] else 1

    def dp(i, j):
        if memo[i][j] is None:
            memo[i][j] = min(filter(lambda x: x is not None, [
                ((0 if s1[i]==s2[j] else 1) + dp(i-1,j-1) if i-1>=0 and j-1>=0 else None),
                (1 + dp(i-1,j) if i-1>=0 else None),
                (1 + dp(i,j-1) if j-1>=0 else None)
            ]))
        return memo[i][j]

    return dp(len(s1)-1, len(s2)-1)

def test_sol():
    test_cases = [
        (("bake","pale"), 2),
        (("abx","cdxx"), 3),
    ]

    for (s1,s2),b in test_cases:
        print(sol(s1,s2)==b)
