from typing import List
import sys

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        assert(len(A) != 0)
        assert(K >= 0)

        if len(A) == 0:
            return 0

        A = sorted(A)

        total = 0
        negs = 0
        abs_min = max(abs(A[0]), A[-1])

        for a in A:
            abs_a = abs(a)

            if abs_a < abs_min:
                abs_min = abs_a

            # add all numbers to total, flipping at most the first K negative numbers
            if a < 0 and negs < K:
                total += abs_a
                negs += 1
            else:
                total += a

        # if odd number of flips remains, flip the smallest number counted as positive 
        if (K - negs) % 2 == 1:
            total -= (abs_min + abs_min)

        return total


# test
sol = Solution()
for (A, K, expected) in [
    (sorted([4, 3, 2]), 1, 5),
    (sorted([3,-1,0,2]), 3, 6),
    (sorted([2,-3,-1,5,-4]), 2, 13),
    (sorted([-8,3,-5,-3,-5,-2]), 6, 22)
]:
    actual = sol.largestSumAfterKNegations(A, K)
    if actual != expected:
        print('Fail:')
        print(' A: {}'.format(A))
        print(' K: {}'.format(K))
        print(' actual {} != {} expected'.format(actual, expected))
