from typing import List
import sys

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        assert(len(A) != 0)
        assert(K >= 0)

        A = sorted(A)

        negs = 0
        stop_negs = False
        abs_min = max(abs(A[0]), A[-1])

        for a in A:
            if a >= 0 or negs == K: # reached the end of negative numbers flipped to positive
                stop_negs = True
            if not stop_negs:
                negs += 1
            abs_a = abs(a)
            if abs_a < abs_min:
                abs_min = abs_a

        res = -sum(A[:negs]) # sum the flipped negatives
        res += sum(A[negs:]) # and the non-flipped everything else

        rem = K - negs
        if rem > 0 and rem % 2 == 1: # if odd number of flips remains
            res -= 2 * abs_min # smallest available positive number flips to negative

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
