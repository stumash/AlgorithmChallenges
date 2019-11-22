from typing import List
from collections import Counter

def sol(arr: List[int]) -> int:
    d = Counter(arr)
    most_viewings = max(d.values())
    return min(a for a in d if d[a] == most_viewings)

input()
print(sol2(list(map(int, input().split(' ')))))
