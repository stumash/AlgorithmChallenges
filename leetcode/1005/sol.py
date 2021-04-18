from typing import List
import sys

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        assert(len(A) != 0)
        assert(K >= 0)

        A = sorted(A)

        negs = 0
        stop_negs = False
        abs_min = A[-1]

        for a in A:
            abs_a = abs(a)
            if a >= 0 or negs == K:
                stop_negs = True
            if not stop_negs:
                negs += 1
            if abs_a < abs_min:
                abs_min = abs_a

        res = -sum(A[:negs])
        res += sum(A[negs:])

        rem = K - negs
        if rem > 0 and rem % 2 == 1:
            res -= 2 * abs_min

        return res

sol = Solution()

tests = [
    (sorted([4, 3, 2]), 1, 5),
    (sorted([3,-1,0,2]), 3, 6),
    (sorted([2,-3,-1,5,-4]), 2, 13),
    (sorted([-8,3,-5,-3,-5,-2]), 6, 22)
]
for (A, K, expected) in tests:
    actual = sol.largestSumAfterKNegations(A, K)
    if actual != expected:
        print('Fail:')
        print(' A: {}'.format(A))
        print(' K: {}'.format(K))
        print(' actual {} != {} expected'.format(actual, expected))
