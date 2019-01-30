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

class Inf:
    def __lt__(self, other): return False
    def __gt__(self, other): return True

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

        memo = [1] +     [0]*len(nums)
        nums = [Inf()] + nums

        def opt(i):
            if memo[i]:
                return memo[i]
            
            res = 1 + max(x if nums[j]<nums[i] else 0 for j,x in enumerate(map(opt, range(i))))
            memo[i] = res

            return res

        opt(len(nums)-1)
        return max(memo)

    # dynamic programming solution -- bottom up
    def dp_lengthOfLIS_bottom_up(self, nums):

        memo = [None]*len(nums)

        for i in range(0, len(nums)):
            if i == 0:
                memo[i] = 1
            else:
                memo[i] = 1 + max(memo[j] if nums[j]<nums[i] else 0 for j in range(i))

        return max(memo)
