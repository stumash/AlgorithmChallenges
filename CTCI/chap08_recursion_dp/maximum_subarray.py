from typing import List

def maximumSubarraySum(ns: List[int]):
    """
    [−2, 1, −3, 4, −1, 2, 1, −5, 4] -> [4, -2, 2, 1] (sum: 6)
    """
    if len(ns) < 1:
        return ns # do nothing for empty subarrays

    memo = [None]*(len(ns))
    memo[0] = ns[0]
    best_sum = memo[0]

    def dp(i):
        nonlocal best_sum
        if i < 0:
            return 0
        if memo[i] is None:
            memo[i] = ns[i]
            if dp(i-1) > 0:
                memo[i] += dp(i-1)
        if memo[i] > best_sum:
            best_sum = memo[i]
        return memo[i]

    def backtrack():
        return max(memo)

    dp(len(ns)-1)
    return backtrack()

def test():
    ns = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert(maximumSubarraySum(ns) == 6)

