from quicksort import quicksort
from itertools import permutations


def test_quicksort():

    for size in [4, 5]:
        nums = list(range(size))

        for ns in permutations(nums):
            ns = list(ns)
            copy = ns[:]
            quicksort(ns)
            print(copy, ns, sorted(ns))
            assert(ns == sorted(ns))
