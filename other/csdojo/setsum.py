from typing import List

d = None

# give an unordered list of integers, find the number of subsets whose sum is k
def setsum(nums: List[int], k: int) -> int:
    global d
    d = {}
    return _setsum(nums, k, len(nums)-1)

def _setsum(nums, k, i):
    global d
    if (k,i) in d: return d[(k,i)]

    extra = 0
    if i < 0:
        return 0
    if k == nums[i]:
        extra = 1
    retval = _setsum(nums, k-nums[i], i-1) + _setsum(nums, k, i-1) + extra
    d[(k,i)] = retval
    return retval

print(setsum([2,4,6,10], 16))
print(setsum([-10, 20, 10, -5, 15], 10))
