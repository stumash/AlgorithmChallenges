from itertools import permutations
from mergesort import mergesorted, _merged

def test_merged():
    [nums1, nums2] = [list(range(i)) for i in [3,4]]
    for ns1 in permutations(nums1):
        for ns2 in permutations(nums2):
            ns1, ns2 = sorted(list(ns1)), sorted(list(ns2))
            assert(_merged(ns1, ns2) == sorted(ns1 + ns2))

def test_mergesorted():
    for size in 4,5:
        nums = list(range(size))
        for ns in permutations(nums):
            ns = list(ns)
            assert(mergesorted(ns) == sorted(ns))
