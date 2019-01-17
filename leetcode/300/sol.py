from typing import List, Any

def incr(bs: List[bool]) -> None:
    c_in = True # add 1
    for i,b in enumerate(bs):
        bs[i] = c_in ^ b
        c_in =  c_in and b

# binary flag version (iterative)
def powerset(things: List[Any]):
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

    # naive solution
    def lengthOfLIS(self, nums):
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

        pass