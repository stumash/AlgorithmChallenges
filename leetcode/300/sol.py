from typing import List, Any

# binary flag version (iterative)
def powerset(things: List[Any]):

    # 'increment' a list of booleans as if each was a bit in an integer
    def incr(bs: List[bool]) -> None:
        c_in = True # add 1
        for i,b in enumerate(bs):
            bs[i] = c_in ^ b
            c_in =  c_in and b

    yield []

    bs    = [True] + [False]*(len(things)-1)
    final =          [False]*(len(things))

    while bs != final:
        yield [t for t,b in zip(things,bs) if b]
        incr(bs)

# recursive version
def powerset_v2(things: List[Any]):
    all_subsets = []
    if len(things) == 0:
        return all_subsets

    # helpers
    def f(ls, i):
        return [ ls, ls[:]+[things[i]] ]

    def flatten(list_of_lists):
        return [x for ls in list_of_lists for x in ls]

    # recursive function
    def _powerset(things, size):
        nonlocal all_subsets
        if size == 0:
            all_subsets.extend([ [], [things[0]] ])
        else:
            _powerset(things, size-1)
            all_subsets = flatten(list(map(lambda ls: f(ls, size), all_subsets)))

    _powerset(things, len(things)-1)
    return all_subsets

class Solution:

    def lengthOfLIS(self, nums):
        return self.powerset_lengthOfLIS(nums)

    # naive solution
    def powerset_lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def is_increasing(nums):
            if nums == []:
                return False
            elif len(nums) == 1:
                return True
            else:
                for n1,n2 in zip(nums,nums[1:]):
                    if not n2 > n1:
                        return False
                return True

        best_length = 0
        for subset in powerset(nums):
            if is_increasing(subset) and len(subset) > best_length:
                best_length = len(subset)

        return best_length

    # dynamic programming solution
    def dp_lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        class Inf:
            def __lt__(self, other): return False
            def __gt__(self, other): return True
            def __eq__(self, other): return type(self) == type(other)
        inf = Inf()

        memo = [None] * len(nums)

        nums = [inf] + nums
        memo = [1] + memo

        def opt(i):
            if memo[i] is None:
                memo[i] = 1 + max(opt(j) if nums[j]<nums[i] else 0 for j in range(i))
            return memo[i]

        retval = opt(len(nums)-1)
        return retval

    # dynamic programming solution -- bottom up
    def dp_lengthOfLIS_bottom_up(self, nums):
        if len(nums) == 0: return 0

        memo = [0]*len(nums)
        memo[0] = 1

        for i,num in enumerate(nums):
            if i == 0: continue # skip first iteration
            memo[i] = 1 + max(memo[j] if nums[j]<num else 0 for j in range(i))
                
        return memo[-1]

    def dp_lengthOfLIS_2D_bottom_up(self, nums):
        if len(nums) < 2: return len(nums)

        memo = [[] for _ in range(len(nums))]
        memo[0] = [1] * len(nums)

        for i in range(1, len(nums)):
            memo_prev, memo_curr = memo[i-1], memo[i]

            for j in range(i, len(nums)):
                # nums[j] is being considered, nums[i-1] is last added

                m = max(memo_prev[j-(i-1)], 1 + (memo_prev[0] if nums[i-1]<nums[j] else 0))
                memo_curr.append(m)

        return memo[-1][-1]
