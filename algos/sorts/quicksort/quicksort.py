from random import randint
from itertools import permutations

def quicksort(items):
    '''
    In-place quicksort. Rightmost element used as pivot in partition stage.
    '''
    _quicksort(items, 0, len(items)-1)

def _quicksort(items, left, right):
    if not left < right:
        return

    i_pivot = _partition(items, left, right)

    _quicksort(items, left, i_pivot-1)
    _quicksort(items, i_pivot, right)

def _partition(items, left, right):
    p = items[right]
    lo = left

    for i in range(left, right):
        if items[i] < p:
            _swap(items, i, lo)
            lo += 1
    _swap(items, lo, right)

    return lo

def _swap(items, left, right):
    items[left], items[right] = items[right], items[left]
